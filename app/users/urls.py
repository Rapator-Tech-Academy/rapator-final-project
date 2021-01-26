from django.contrib import admin
from django.urls import path, include

from .views import *

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name="users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset"),
    path('signup/', SignUpView.as_view(), name="register"),  
    path('activate/<uidb64>/<token>/', SignUpView.activate, name='activate'),
]