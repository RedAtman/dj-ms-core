# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_migrate


class RbacConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'rbac'
    verbose_name = 'RBAC'

    # def ready(self):
    #     # post_migrate.connect(create_permissions,
    #     #     dispatch_uid='rbac.management.create_permissions'
    #     # )

    #     from rbac.signals import init

    #     post_migrate.connect(init, sender=self)
