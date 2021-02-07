from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    


