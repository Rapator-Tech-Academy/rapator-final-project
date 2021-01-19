from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from .views import RegisterView, LoginView, ForgetPasswordView, ResetPasswordView
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),
    url('register',RegisterView.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        RegisterView.activate, name='activate'),
]