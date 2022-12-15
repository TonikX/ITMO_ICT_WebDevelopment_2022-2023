from django.contrib.auth.models import User
from django.db import models

from apps.homeworks.models import Homework


class Submission(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    content = models.CharField(
        max_length=1000
    )
    mark = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True
    )
    checked_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.student.username}:{self.homework.name}"
