from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.conf import settings

from users.forms import RegisterForm, LoginForm, ResetPasswordConfirmForm, ResetPasswordForm
from .models import User
from django.views import View
from django.contrib.auth.tokens import default_token_generator


class RegisterView(CreateView):
    form_class = RegisterForm
    model = User
    template_name = 'accounts/register.html'
    # success_url = 'accounts/login.html'

    def signup(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('accounts/acc_activate.html',{
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })
                mail_subject = 'Activate your account.'
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def activate(request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


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
