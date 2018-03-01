import logging

from django.core.management.base import BaseCommand

from ...listeners import reset_email_group

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """Reset groups generated by email suffix matching."""

    def handle(self, *args, **kwargs):
        reset_email_group()
