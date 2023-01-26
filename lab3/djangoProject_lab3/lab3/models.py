from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

class Driver(AbstractUser):
    passport = models.CharField(max_length=30, db_column="passport", null=True)
    address = models.CharField(max_length=128, db_column="address", null=True)
    nationality = models.CharField(max_length=128, db_column="nationality", null=True)

    class Meta:
        db_table = "Driver"


class Car(models.Model):
    number = models.CharField(max_length=15)
    marka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    class Meta:
        db_table = "Car"


class Driver_license(models.Model):
    id_Driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    data_got = models.DateTimeField()

    class Meta:
        db_table = "driver license"


class Owner(models.Model):
    id_Driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_start = models.DateTimeField()
    data_end = models.DateTimeField()

    class Meta:
        db_table = "Ownership"
