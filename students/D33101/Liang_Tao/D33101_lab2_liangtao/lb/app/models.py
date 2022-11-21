from django.db import models

# Create your models here.

from django.db import models


class Car(models.Model):
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)


class Owner(models.Model):
    pass_number = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=30, null=True)
    nat = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.birth_date}'


class Possession(models.Model):
    id_owner = models.ManyToManyField(Owner)
    id_car = models.ManyToManyField(Car)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True)


class DriverLicense(models.Model):
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()
