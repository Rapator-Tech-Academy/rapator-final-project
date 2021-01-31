from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView

from .models import Category, City, Product
from .forms import NewProductForm
from .stories import CreateProduct



class NewProductFormView(FormView):
    template_name = 'pages/new_product.html'
    form_class = NewProductForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context = {
            'categories': Category.objects.filter(level=0),
        }

        return context

    def form_valid(self, form):
        print(form.cleaned_data.get('title'))

        CreateProduct().create(
            form=form
        )
        return super().form_valid(form)

class ProductView(DetailView):
    template_name = 'pages/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_slug_field(self):
        return 'slug'

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        obj = self.get_object()
        obj.view_count += 1
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

    def get_products_price_range(self):
        return Product.objects.filter(price_range(min_price, max_price))


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
    template_name = 'pages/basic_card.html'


class UserProfilePageView(TemplateView):
    template_name = 'pages/user_profile.html'


class UserAccountSettingsView(TemplateView):
    template_name = 'pages/profile_settings.html'

