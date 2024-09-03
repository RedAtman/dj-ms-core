from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task
from django.core.management import call_command

from core.celery import app


@shared_task
def shared_task_01():
    time.sleep(2)
    localtime = time.localtime()
    return localtime

@app.task()
def mail_today_new_user():
    call_command("mail_today_new_user", )
