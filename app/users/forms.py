from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import User as UserModel
from .models import *

class RegisterForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'name'}))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'surname'}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'phone_number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password2'}))

    class Meta:
        model = UserModel
        fields = ('name', 'surname', 'email',
                  'phone', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserModel
        fields = ['email', 'password']


class ResetPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))


class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'New password1'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New password2'}))

    class Meta:
        fields = ("new_password1", 'new_password2', )
