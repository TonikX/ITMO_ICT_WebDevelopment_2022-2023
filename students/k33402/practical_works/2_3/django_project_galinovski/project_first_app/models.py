from django.db import models
from django.contrib.auth.models import AbstractUser


class Owner(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    passport = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nation = models.CharField(max_length=20, null=True, blank=True)

class Car(models.Model):
    number = models.CharField(max_length=15)
    brand= models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

class Ownership(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class DriversLicense(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()