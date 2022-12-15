from django.db import models
from django.utils import timezone

from apps.groups.models import Group
from apps.subjects.models import Subject


class Homework(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    date_start = models.DateTimeField(
        default=timezone.now
    )
    date_end = models.DateTimeField(
        null=True,
        blank=True
    )
    task = models.CharField(
        max_length=300
    )
    punishment = models.CharField(
        max_length=300
    )
