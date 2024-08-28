import logging

from django.test import TestCase

logger = logging.getLogger()


class NotificationTest(TestCase):
    databases = '__all__'

    def setUp(self):
        import os

        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        django.setup()

    def test_send_mail(self):
        from django.conf import settings
        from django.core.mail import send_mail

        # mail_admins('subject', 'message', html_message=None)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER,]
        logger.info((email_from, recipient_list))
        result = send_mail('subject', 'message', email_from, recipient_list)
        logger.info(result)

    def test_email_today_new_user(self):
        from django.core.management import call_command
        call_command('mail_today_new_user')
