from django.conf import settings
from django.core.mail import send_mail
from .models import *

def send_email(recipient,email_message,email_subject):
    settings.EMAIL_HOST_PASSWORD = azure_key.objects.get(name="password").key
    subject = email_subject
    message = email_message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient]
    send_mail(subject,message,email_from,recipient_list)