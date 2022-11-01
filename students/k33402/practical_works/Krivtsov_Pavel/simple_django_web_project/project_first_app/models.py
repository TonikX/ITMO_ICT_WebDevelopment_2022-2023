from django.db import models


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(null=True)


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)


class DriversLicense(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_of_issue = models.DateTimeField(null=False)


class Ownership(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateTimeField(null=False)
    finish_date = models.DateTimeField(null=True)
