from django import forms

from .models import Product

class NewProductForm(forms.Form):
    title = forms.CharField()
    delivery = forms.BooleanField()
    is_new = forms.BooleanField()
    category = forms.CharField()
    city = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField()

    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()


    