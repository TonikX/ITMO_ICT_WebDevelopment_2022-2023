from django.contrib.auth.models import User
from django.db import models

from apps.subjects.models import Subject


class Group(models.Model):
    name = models.CharField(
        max_length=10
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='groups'
    )
    students = models.ManyToManyField(
        User,
        related_name='groups'
    )

    def __str__(self):
        return self.name
