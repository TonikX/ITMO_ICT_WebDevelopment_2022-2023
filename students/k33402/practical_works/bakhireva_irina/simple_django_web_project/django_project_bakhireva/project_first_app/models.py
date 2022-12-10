from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=30, null=True)
    passport = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    number = models.CharField(max_length=15)
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)
    ownership = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Property')

    def __str__(self):
        return  f"{self.manufacturer} {self.model}"
    

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return "{} {} {}".format(self.car.model, self.car.manufacturer, self.start_date.date())


class License(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

    def __str__(self):
        return f"лицензия #{self.license_number}"
