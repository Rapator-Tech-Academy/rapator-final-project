from django.conf import settings
from django.core.mail import send_mail
from .utils import account_activation_token
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError

from django.urls import reverse
from django.shortcuts import render


from django.db import models
# from .tasks import email_user
from django.contrib.auth.models import (
    AbstractBaseUser, User,
    UserManager, PermissionsMixin
)


class UserManager(UserManager):

    def create_user(self, email, password=None):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, null=True)
    profile_img = models.ImageField(upload_to='images', null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
