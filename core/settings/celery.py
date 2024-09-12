from core.settings.base import *  # noqa: F403

INSTALLED_APPS.insert(-1, 'django_celery_beat')  # noqa: F405
INSTALLED_APPS.insert(-1, 'django_celery_results')  # noqa: F405


# -----> RABBITMQ
BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@localhost:5672')


# -----> CELERY
CELERY_BROKER_URL = BROKER_URL
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_CACHE_BACKEND = 'django-cache'
# CELERY_CACHE_BACKEND = "default"
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_IGNORE_RESULT = True
CELERY_ACKS_LATE = True
CELERYD_CONCURRENCY = 10
CELERYD_FORCE_EXECV = True
CELERYD_MAX_TASKS_PER_CHILD = 100
CELERYD_TASK_TIME_LIMIT = 12 * 30

CELERY_RESULT_BACKEND = 'django-db'
# CELERY_RESULT_BACKEND = BROKER_URL
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = os.getenv('CELERY_BEAT_SCHEDULER', 'django_celery_beat.schedulers.DatabaseScheduler')
from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    "mail_today_new_user": {
        "task": "notification.tasks.mail_today_new_user",
        # "schedule": crontab(minute="*/1"),
        # "schedule": timedelta(seconds=10),
        "schedule": timedelta(days=1),
        "args": (),
    },
}
