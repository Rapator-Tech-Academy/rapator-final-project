from django.db import models

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


class User(AbstractBaseUser, PermissionMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=10)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
