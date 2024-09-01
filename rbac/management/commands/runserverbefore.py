import logging
import os

from django.core.management.commands.runserver import Command

logger = logging.getLogger(__name__)
class Command(Command):

    def handle(self, *args, **kwargs):
        logger.info(('RUN_MAIN', os.environ.get('RUN_MAIN')))
        super().handle(*args, **kwargs)
