from django.db import models
from django.conf import settings

class CarOwnerUser(models.Model):
    id_owner = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateField()

class DriversLicense(models.Model):
    id_lic = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(CarOwnerUser, on_delete=models.CASCADE)
    type_lic = models.CharField(max_length=10, null=False)
    exp_date = models.DateField()

class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    car_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_ownership = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(CarOwnerUser, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
