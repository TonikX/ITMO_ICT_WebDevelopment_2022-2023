from django.db import models
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FabianaUser(AbstractUser):
    email = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['email']