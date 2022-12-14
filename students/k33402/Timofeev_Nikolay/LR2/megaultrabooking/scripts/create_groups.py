from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from megaultrabooking.models import UserType


class Command(BaseCommand):
    help = "Creates groups for the different user types."

    def handle(self, *args, **options):
        for user_type in UserType:
            Group.objects.create(name=user_type.label, code=user_type.value)
