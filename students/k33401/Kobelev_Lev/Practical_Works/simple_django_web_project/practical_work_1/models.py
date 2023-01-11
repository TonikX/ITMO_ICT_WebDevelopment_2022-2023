from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    @classmethod
    def as_view(cls):
        pass


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Ownership')
    passport = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)

    @classmethod
    def as_view(cls):
        pass


class DriverLicense(models.Model):
    license_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Ownership(models.Model):
    ownership_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ownership_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
