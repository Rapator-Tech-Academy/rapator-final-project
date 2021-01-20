from django.contrib import admin
from django.urls import path, include

from .views import RegisterView, LoginView, ForgetPasswordView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset")
    #path('login/email', , name='login-email'),
    #path('login/email/confirmation/', , name='email-confirmation'),


]