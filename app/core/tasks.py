import random
from django.contrib.auth import get_user_model
from celery import Celery, shared_task
from .utils.helpers import send_mail_helper
 
from celery.schedules import crontab
from datetime import date, timedelta 
from .models import Product

app = Celery()


@shared_task
def send_review_mail(product_id):
    product = Product.objects.filter(id=product_id).first()

    if product:
        if product.status == 0:
            send_mail_helper(subject='Your product is under review 🧐 ', to_email_addresses=[product.user.email])
        elif product.status == 1:
            send_mail_helper(subject='Your product is accepted ✅ ', to_email_addresses=[product.user.email])
        elif product.status == 2:
            send_mail_helper(subject='Your product is finished 😔 ', to_email_addresses=[product.user.email])
        else:
            send_mail_helper(subject='Your product is rejected. Review it again 🔴 ', to_email_addresses=[product.user.email])

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        task_update_product_status.s()
        )

@app.task
def task_update_product_status():
    products = Product.objects.filter(status=1)
    for product in products:
        if((product.updated_at + timedelta(days=30)).date() < date.today()):# eger 30 gun kecibse
            product.status = 2
            product.save()

@app.task 
def reset_product_daily_view_count():
    products = Product.objects.all()
    products.update(daily_view_count=0)


'''
@periodic_task(
    run_every=crontab(minute=0, hour=0),
    name          = "task_update_product_status",
    ignore_result = True
    )
def task_update_product_status():
    products = Product.objects.filter(status=1)
    for product in products:
        if((product.updated_at + timedelta(days=30)).date() < date.today()):# eger 30 gun kecibse
            product.status = 2
            product.save()
'''          

