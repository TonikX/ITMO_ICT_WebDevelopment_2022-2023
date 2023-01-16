from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
import random
import string


def get_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class Owner(AbstractUser):
    username = models.CharField(
        max_length=30, default=get_random_string, unique=True)
    password = models.CharField(max_length=230)
    last_login = models.DateField(default=datetime.now)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    date_of_birth = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=30, null=True)


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=20)


class OwnedCars(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class DrivingLicense(models.Model):
    TYPES = (
        ('M', 'Quadrocycles'),
        ('A', 'Motorcycles'),
        ('B', 'Car'),
        ('C', 'Light Trucks'),
        ('E', 'Trailers')
    )
    id_number = models.CharField(max_length=30)
    date_of_giving = models.DateField()
    category = models.CharField(max_length=5, choices=TYPES)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
