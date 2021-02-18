from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, City, Product
from .forms import NewProductForm, UserAccountUpdateForm
from .stories import CreateProduct, UpdateAccount


class NewProductFormView(FormView):
    template_name = 'add_product.html'
    form_class = NewProductForm

    def post(self, request, *args, **kwargs):
        form = NewProductForm(request.POST)
        if request.is_ajax():
            print(request.POST['delivery'])
            print(request.POST['is_new'])
            CreateProduct().create(
                title=request.POST['title'],
                delivery=request.POST['delivery'],
                is_new=request.POST['is_new'],
                price=request.POST['price'],
                description=request.POST['description'],
                city=request.POST['city'],
                category=request.POST['category'],
                email=request.POST['user_email']
            )

            return HttpResponse(status=201)

        else:
            print("error")
            return HttpResponse(status=503)



class UserAccountUpdateFormView(FormView):
    template_name = 'pages/profile_settings.html'
    form_class = UserAccountUpdateForm

    def form_valid(self, form):
        print(form.cleaned_data.get('name'))
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
        print(obj.daily_view_count)
        obj.save()
        return result

    def get_object_categories(self):
        obj = self.get_object()
        return obj.category

    def get_related_products(self):
        category = self.get_object_categories()
        obj = self.get_object()
        return self.model.objects.filter(
            category=category).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_related_products()
        return context


class EditProductView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/edit_product.html'

    def get(self, request, *args, **kwargs):
        product_user = self.get_object().user
        if product_user == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponse(status=405)


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


class SearchResultPageView(ListView):
    template_name = 'pages/result_page.html'
    model = Product
    context_object_name = 'products'


class BasicTestView(TemplateView):
    template_name = 'accounts/email_confirmation_complete.html'


class UserProfilePageView(TemplateView):
    template_name = 'pages/user_profile.html'


class ProductDetailView(TemplateView):
    template_name = 'pages/user_product_detail.html'
