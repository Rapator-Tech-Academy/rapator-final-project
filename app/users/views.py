from django.views.generic import FormView
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model

from users.forms import RegisterForm, ResetPasswordForm, LoginForm


User = get_user_model()


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = 'accounts/register.html'


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'accounts/forget_password.html'
    success_url = 'accounts/login.html'


class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = RegisterForm
    success_url = '/'

    def send_activation_email(self, email, user):
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('accounts/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')

    def create_new_user(self, form):
        email = form.cleaned_data.get('email')
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Email has already taken.')
        else:
            new_user = User.objects.create_user(
                email = email,
                password = form.cleaned_data.get('password')
            )
            new_user.name = name
            new_user.surname = surname 
            new_user.is_active = False
            new_user.save()

            self.send_activation_email(email=email, user=new_user)

    def activate(request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return TemplateResponse(request, template='accounts/email_confirmation_complete.html', context={'message': 'Sizin hesabınız təsdiqləndi', 'status': 'success'})
        else:
            return TemplateResponse(request, template='accounts/email_confirmation_complete.html', context={'message': 'Token-in yararlılıq müddəti başa çatıb', 'status': 'error'})
        

    def form_valid(self, form):
        self.create_new_user(form=form)

        return super().form_valid(form)