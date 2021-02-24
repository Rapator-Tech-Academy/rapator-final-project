from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Category, City, Product
from .forms import NewProductForm, UserAccountUpdateForm
from .stories import CreateProduct, UpdateAccount, EditProduct


@login_required(login_url='/users/login/')
def delete_product(request, slug):
    user = request.user
    product = Product.objects.filter(slug=slug).first()

    if product and product.user==user:
        product.delete()
        return HttpResponseRedirect("/")
    else:
        raise Http404


class NewProductFormView(FormView):
    template_name = 'add_product.html'
    form_class = NewProductForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if request.is_ajax():
            CreateProduct().create(
                title=request.POST['title'],
                delivery=request.POST['delivery'],
                is_new=request.POST['is_new'],
                price=request.POST['price'],
                description=request.POST['description'],
                city=request.POST['city'],
                category=request.POST['category'],
                email=request.POST['user_email'],
                image = request.FILES['image'],
            )

            return HttpResponse(status=201)

        else:
            return HttpResponse(status=503)


class UserAccountUpdateFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/profile_settings.html'
    form_class = UserAccountUpdateForm
    login_url = '/users/login/'

    def form_valid(self, form):
        UpdateAccount().create(
            form=form,
            user=self.request.user
        )
        return super().form_valid(form)
    

    def get_success_url(self):
        return self.request.path


class ProductView(DetailView):
    template_name = 'pages/product_detail.html'
    model = Product
    context_object_name = 'product'

    # def get_slug_field(self):
    #     return 'slug'

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        obj = self.get_object()
        obj.view_count += 1
        obj.daily_view_count += 1
        obj.save()
        return result

    def get_object_categories(self):
        obj = self.get_object()
        return obj.category

    def get_related_products(self):
        category = self.get_object_categories()
        obj = self.get_object()
        return self.model.objects.filter(
            category=category).order_by('-updated_at').exclude(id=obj.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_related_products()
        return context


class EditProductView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    login_url = '/users/login/'
    template_name = 'pages/edit_product.html'

    def get(self, request, *args, **kwargs):
        product_user = self.get_object().user
        if product_user == request.user:
            return super().get(request, *args, **kwargs)
        else:
            raise Http404
    
    def post(self, request, *args, **kwargs):
        
        if request.is_ajax():
            EditProduct().update(
                product = self.get_object(),
                title = request.POST['title'],
                price = request.POST['price'],
                description = request.POST['description'],
            )

            return HttpResponse(status=201)
        else:
            return HttpResponse(status=503)


class CategoryView(ListView):
    template_name = "/pages/product_detail.html"
    model = Product

    def get_category(self):
        return Category.objects.filter(slug=self.kwargs.get('slug')).first()

    def get_queryset(self):
        category = self.get_category()
        return Product.objects.filter(category=category).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageView(TemplateView):
    # TODO: Implement Home Page View (get latest products, total product count etc.)
    template_name = 'home_page.html'


class SearchResultPageView(TemplateView):
    template_name = 'pages/result_page.html'


class UserProfilePageView(LoginRequiredMixin, TemplateView):
    login_url = '/users/login/'
    template_name = 'pages/user_profile.html'

    def get_logged_user(self):
        user = self.request.user

        return user
    
    def get_pending_products(self):
        user = self.get_logged_user()
        products = Product.objects.filter(user=user, status=0)

        return products
    
    def get_published_products(self):
        user = self.get_logged_user()
        products = Product.objects.filter(user=user, status=1)

        return products
    
    def get_time_finished_products(self):
        user = self.get_logged_user()
        products = Product.objects.filter(user=user, status=2)

        return products
    
    def get_rejected_products(self):
        user = self.get_logged_user()
        products = Product.objects.filter(user=user, status=3)

        return products
    
    def get_sum_of_total_product(self):
        user = self.get_logged_user()
        sum_of_products = Product.objects.filter(user=user).count()

        return sum_of_products


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        condition = self.kwargs['condition']

        if condition == 'expired':
            context = {
                'products': self.get_time_finished_products()
            }
        elif condition == 'published':
            context = {
                'products': self.get_published_products()
            }
        elif condition == 'pending':
            context = {
                'products': self.get_pending_products()
            }
        elif condition == 'rejected':
            context = {
                'products': self.get_rejected_products()
            }

        context['total_count_of_products'] = self.get_sum_of_total_product()

        return context
    




