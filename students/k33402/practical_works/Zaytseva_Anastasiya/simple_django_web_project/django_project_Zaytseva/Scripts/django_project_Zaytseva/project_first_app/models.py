from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CarOwner(AbstractUser):
    id_owner = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    passport_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30, default='Russian')

class DrivingLicense(models.Model):
    id_license = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField()

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    gov_number = models.CharField(max_length=15)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

class Ownership(models.Model):
    id_owner_car = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_start = models.DateTimeField()
    date_of_end = models.DateTimeField(null=True, blank=True)