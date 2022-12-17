from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    passport = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    middle_name = models.TextField()
    city = models.TextField(null=True, blank=True)
    is_cleaning_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
