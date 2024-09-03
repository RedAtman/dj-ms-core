from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from rbac.init import Init


class Command(BaseCommand):
    help = "Initializes RBAC system."

    def handle(self, *args, **options):
        Init().run()
