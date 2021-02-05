from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


from .models import Product
from .tasks import send_review_mail

@receiver(signals.post_save, sender=Product, dispatch_uid="product_create_log")
def send_message(sender, instance, created, **kwargs):
    send_review_mail.apply_async(args=(instance.id,))