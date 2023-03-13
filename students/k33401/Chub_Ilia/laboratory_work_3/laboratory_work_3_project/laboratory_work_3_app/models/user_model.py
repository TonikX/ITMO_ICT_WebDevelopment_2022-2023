from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    phone_number = models.CharField(max_length=15)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
