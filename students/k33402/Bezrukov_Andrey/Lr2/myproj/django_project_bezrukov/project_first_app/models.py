from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CarOwnerUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=30)
    home_address = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=30, blank=True)


class DriversLicense(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Car(models.Model):
    car_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=30, blank=True)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')


class Ownership(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
