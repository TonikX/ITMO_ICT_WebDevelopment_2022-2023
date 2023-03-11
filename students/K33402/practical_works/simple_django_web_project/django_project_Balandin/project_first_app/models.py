from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=10)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=32)


class Owner(AbstractUser):
    surname = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    passport = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)


class Licence(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class Ownership(models.Model):
    driver = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=False)
    expiry_date = models.DateTimeField()
