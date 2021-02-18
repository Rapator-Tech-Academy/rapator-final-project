from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Adınız...'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Soyadınız...'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'İstifadəçi adınız...'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(000)000-00-00'}), max_length=12)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email(exsamples@gmail.com)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Şifrə'}))



class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    


