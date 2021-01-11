import random
import datetime

from django.contrib.auth import get_user_model
from celery import Celery, shared_task

from .models import Product
from .utils.helpers import send_mail_helper

app = Celery()


@shared_task
def send_review_mail(product_id):
    product = Product.objects.filter(id=product_id).first()

    if product and product.status == 0:
        send_mail_helper(subject='Your product is under review :) ', to_email_addresses=['ugurguliyev7@gmail.com'])
