from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

class Driver(AbstractUser):
    first_name = models.CharField(max_length=128, db_column="address", null=True)
    second_name = models.CharField(max_length=128, db_column="address", null=True)
    birthday = models.DateTimeField()


class License(models.Model):
    id_driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    data_got = models.DateTimeField()



class Car(models.Model):
    number = models.CharField(max_length=15)
    marka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)


class Owner(models.Model):
    id_driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_start = models.DateTimeField()
    data_end = models.DateTimeField()

