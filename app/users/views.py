from django.shortcuts import render
from users.models import User
from django.views.generic import TemplateView, FormView, RedirectView
from .forms import RegisterForm,  LoginForm
from django.contrib.auth import logout





class RegisterView(FormView):
    form_class = RegisterForm
    model = User
    template_name = 'accounts/register.html'
    success_url   = 'accounts/login.html'

class LoginEmailView(FormView):
    form_class    = LoginForm
    template_name = 'accounts/login_by_email.html'
    success_url   = 'accounts/register.html'

class LoginView(TemplateView):
    template_name = 'accounts/login.html'

class EmailConfirmView(TemplateView):
    template_name = 'accounts/confirmation.html'


    
