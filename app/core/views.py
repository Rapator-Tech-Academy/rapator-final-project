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
        }

        return context

    def form_valid(self, form):
        print(form.cleaned_data.get('title'))

        CreateProduct().create(
            form = form
        )

        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = 'home_page.html'


class BasicTestView(TemplateView):
    template_name = 'pages/basic_card.html'


class UserProfilePageView(TemplateView):
    template_name='pages/user_profile.html'

    
class UserAccountSettingsView(TemplateView):
    template_name='pages/profile_settings.html'


class ProductDetailView(TemplateView):
    template_name='pages/product_detail.html'