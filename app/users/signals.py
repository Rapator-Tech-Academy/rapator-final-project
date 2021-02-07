from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import User
from .tasks import send_welcome_email

@receiver(signals.post_save, sender=User, dispatch_uid="user_create_log")
def send_message(sender, instance, created, **kwargs):
    if created and instance.is_superuser is not True:
        print(instance.email)
        send_welcome_email.apply_async(args=(instance.id,))
        
        
