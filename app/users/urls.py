from django.contrib import admin
from django.urls import path, include

from .views import RegisterView, LoginView, ForgetPasswordView, ResetPasswordView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),

]