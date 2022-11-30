from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser



class Owner(AbstractUser):
    owner_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField(null=True)
    passport = models.CharField(max_length=20, blank=False, null=False, unique=True)
    address = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=30, blank=True, null=False)


class Car(models.Model):
    id_number = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    official_number = models.CharField(max_length=30)


class Owning(models.Model):
    owner = models.ForeignKey(Owner, related_name='owning_car', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField(default=date(2010, 1, 1))
    end_date = models.DateField(default=date(2020, 1, 1))


class DrivingLicense(models.Model):
    LICENCE_TYPES = (
        ('A', 'Motorcycles'),
        ('B', 'Cars'),
        ('D', 'Buses'),
    )
    number = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    date_of_issue = models.DateField(default=date(2010, 1, 1))
    type = models.CharField(max_length=3, choices=LICENCE_TYPES)
# Create your models here.
