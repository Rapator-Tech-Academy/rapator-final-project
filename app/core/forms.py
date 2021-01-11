from django import forms

from .models import Product

class NewProductForm(forms.Form):
    title = forms.CharField()
    delivery = forms.CheckboxInput()
    is_new = forms.CheckboxInput()
    category = forms.CharField()
    city = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField()

    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()


    