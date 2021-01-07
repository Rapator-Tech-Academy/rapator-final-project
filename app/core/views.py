from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .models import Category, City
from .forms import NewProductForm
from .stories import CreateProduct

# Create your views here.

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
        title = form.cleaned_data.get('title')
        delivery = form.cleaned_data.get('delivery')
        is_new = form.cleaned_data.get('is_new')
        price = float(form.cleaned_data.get('price'))
        description = form.cleaned_data.get('description')
        city = form.data.get('city')
        category = form.data.get('category')

        print(category)

        CreateProduct().create(
            title = title,
            delivery = delivery,
            is_new = is_new,
            price = price,
            description = description,
            city = city, 
            category = category
        )
        return super().form_valid(form)

