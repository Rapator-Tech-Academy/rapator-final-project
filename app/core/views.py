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
            'cities': City.objects.all().order_by('name')
        }

        return context

    def form_valid(self, form):

        CreateProduct().create(
            form=form
        )
        return super().form_valid(form)





class ProductView(DetailView):
    template_name = "pages/new_product.html"
    model = Product

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
        return obj.category.all()

    def get_related_posts(self):
        category = self.get_object_categories()
        obj = self.get_object()
        return self.model.objects.filter(
            category__in=category).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = self.get_related_posts()
        return context


class CategoryView(ListView):
    template_name = "pages/product_detail.html"
    model = Product

    def get_category(self):
        return Category.objects.filter(slug=self.kwargs.get('slug')).first()

    def get_queryset(self):
        category = self.get_category()
        return Product.objects.filter(category=category).order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
