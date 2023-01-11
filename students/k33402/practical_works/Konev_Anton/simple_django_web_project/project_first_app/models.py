from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CarOwner(AbstractUser):
    owner_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=40, null=False, blank=True)
    nationality = models.CharField(max_length=20, null=False, blank=True)
    username = models.CharField(max_length=30, null=False, unique=True)


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    number_plate = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    car_owner_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey("CarOwner", on_delete=models.CASCADE)
    car_id = models.ForeignKey("Car", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class DriverLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey("CarOwner", on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    issue_date = models.DateField()
