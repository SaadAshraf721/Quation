from .models import chat
from django.core.mail import send_mail
from multichat import settings


def my_cron_job():
    rec = chat.objects.filter(to=0, sts=False).distinct('pa')
    for i in rec:
        subject = f'Hello admin some new messages from {i.pa.username}.'
        message = 'Hi There are new messages.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['saadashraf721@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
    rec.update(sts=True)
