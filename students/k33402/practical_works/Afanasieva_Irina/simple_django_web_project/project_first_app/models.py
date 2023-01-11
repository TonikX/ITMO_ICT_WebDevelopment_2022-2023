from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Car(models.Model):
    car_id = models.IntegerField(blank=False, primary_key=True)
    car_number = models.CharField(max_length=15, blank=False)
    car_make = models.CharField(max_length=20, blank=False)
    car_model = models.CharField(max_length=20, blank=False)
    car_color = models.CharField(max_length=30)


class Owner(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, default='123')

    owner_id = models.IntegerField(blank=False, primary_key=True)
    owner_surname = models.CharField(max_length=30, blank=False)
    owner_name = models.CharField(max_length=30, blank=False)
    owner_birth = models.DateField(default='1970-01-01')
    passport = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=20, null=True)
    cars = models.ManyToManyField(Car, through='Ownership')


class License(models.Model):
    license_id = models.IntegerField(blank=False, primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, blank=False)
    license_type = models.CharField(max_length=10, blank=False)
    issue_date = models.DateField(blank=False)


class Ownership(models.Model):
    car_owner_id = models.IntegerField(blank=False, primary_key=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
