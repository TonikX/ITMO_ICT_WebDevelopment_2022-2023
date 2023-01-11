from django.db import models
from django.contrib.auth.models import AbstractUser


class Vehicle(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.number


class Driver(AbstractUser):
    surname = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    vehicles = models.ManyToManyField(Vehicle, through='Ownership')

    passport = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Licence(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class Ownership(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()

    def __str__(self):
        return "{}_{}".format(self.driver.__str__(), self.vehicle.__str__())
