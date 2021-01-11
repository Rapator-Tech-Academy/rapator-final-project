# from .celery import app
# from django.conf import settings
# from .models import activate_user_email
# from django.core.mail import send_mail

from django.contrib.auth import get_user_model
from celery import Celery, shared_task

from .models import User
from .helpers import send_mail_helper
app = Celery()

# @app.task
# def email_user(self, message, from_email=None, **kwargs):
# send_mail(message, from_email, [self.user.email], kwargs)



@shared_task
def send_welcome_email(user):
    if user == User.is_active is False:
        send_mail_helper(subject="Activate your account", to_email=[User.email])


#
# @app.task
# def send_welcome_email(user):
# if user.email:
# send_mail(
# "Welcome to tap.az"
# 'tap.az.elanlar@gmail.com',
# [user.email],
# fail_silently=False
# )
#
