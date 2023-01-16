from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
