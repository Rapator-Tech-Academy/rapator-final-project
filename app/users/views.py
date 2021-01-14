from django.shortcuts import render
from users.models import User
from django.views import View
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from users.forms import RegisterForm, LoginForm, ResetPasswordConfirmForm, ResetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.conf import settings

from .utils import account_activation_token

class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'accounts/register.html'
    success_url = 'accounts/login.html'


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = 'accounts/register.html'


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'accounts/forget_password.html'
    success_url = 'accounts/login.html'


class ResetPasswordView(PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name = "password_reset_confirm.html"
    # success_url

