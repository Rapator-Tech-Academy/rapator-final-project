from django.shortcuts import render
from .models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm, LoginForm, ResetPasswordForm
from django.contrib.auth.views import LoginView, PasswordResetView
from django.conf import settings



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
    success_url='accounts/login.html'
    


