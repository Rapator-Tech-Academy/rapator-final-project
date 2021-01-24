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


class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
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
