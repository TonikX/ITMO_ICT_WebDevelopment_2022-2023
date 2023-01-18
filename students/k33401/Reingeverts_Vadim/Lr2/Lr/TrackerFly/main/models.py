from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass

    # def __str__(self):
    #     return f"{self.username} ({self.first_name} {self.last_name})"

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)
