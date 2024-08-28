import logging
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.utils import timezone

logger = logging.getLogger(__name__)

User = get_user_model()
today = timezone.now()
yesterday = today - timedelta(1)


class Command(BaseCommand):
    help = 'Send The Daily Count of New Users to Admins'

    def handle(self, *args, **options):
        user_count = User.objects.filter(date_joined__range=(yesterday, today)).count()
        message = 'You have got {} user(s) in the past 24 hours'.format(user_count)
        subject = f"New user count for {today.strftime('%Y-%m-%d')}: {user_count}"
        try:
            # mail_admins(subject=subject, message=message, html_message=None)

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER,]
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            logger.exception(e)
            error = f'Error: {e}'
            self.stdout.write(error)
            raise e
        msg = 'E-mail was sent.'
        self.stdout.write(msg)
        return msg
