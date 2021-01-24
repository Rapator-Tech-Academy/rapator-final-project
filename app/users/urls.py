from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='register'),
    path('login/email', views.LoginEmailView.as_view(), name='login-email'),
    path('activate/<uidb64>/<token>/', views.SignUpView.activate, name='activate'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset"),
    path('login/', views.LoginView.as_view(), name='login'),
    #path('log-out/', LogoutView.as_view(), name='log-out'),
    path('login/email/confirmation/', views.EmailConfirmView.as_view(), name='email-confirmation'),


]
 