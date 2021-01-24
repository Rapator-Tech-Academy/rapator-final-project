# from .celery import app
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
from celery import Celery, shared_task

from .models import User
app = Celery()

User = get_user_model()





@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    if user.email:
        send_mail(
            subject="Welcome to tap.az",
            message="tap.az.elanlar@gmail.com",
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[user.email, settings.EMAIL_HOST_USER],
            fail_silently=False
        )
