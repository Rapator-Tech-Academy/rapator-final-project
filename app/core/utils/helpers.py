from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings

def send_mail_helper(subject, to_email_addresses, text_message=None):
    email_from = settings.EMAIL_HOST_USER
    send_mail(
        subject=subject,
        message=text_message,
        from_email=email_from,
        recipient_list=to_email_addresses,
        fail_silently=False
    )