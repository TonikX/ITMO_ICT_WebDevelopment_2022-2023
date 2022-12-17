from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15, null=False)
    make_car = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    colour = models.CharField(max_length=30, null=True)

    # def __str__(self):
    #     return self.car_id.__str__()


class CarOwner(AbstractUser):
    owner_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=30, null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return self.owner_id.__str__()


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name='owner')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateField()
    expiration_date = models.DateField(null=True)

    def __str__(self):
        return "{}_{}".format(self.owner_id.__str__(), self.car_id.__str__())


class DriverLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name='carOwner')
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_of_license = models.DateField()
