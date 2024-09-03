import logging

from cuser.middleware import CuserMiddleware
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

logger = logging.getLogger(__name__)


def _pre_save(sender, instance, **kwargs):
    if instance.pk:
        instance.last_editor = CuserMiddleware.get_user()


def _post_save(sender, instance, created, **kwargs):
    logger.info(('_post_save', sender, created, instance, kwargs))


class CurrentUserModelMixin(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # models.DO_NOTHING,
        on_delete=models.CASCADE,
        default=CuserMiddleware.get_user,
        editable=False,
        null=True,
        related_name='%(app_label)s_%(class)s_creator',
    )
    last_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='%(app_label)s_%(class)s_last_editor',
    )

    class Meta:
        abstract = True

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        pre_save.connect(_pre_save, sender=cls)
        # post_save.connect(_post_save, sender=cls)
