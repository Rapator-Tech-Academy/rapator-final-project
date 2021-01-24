from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Surname'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['email', 'password']


