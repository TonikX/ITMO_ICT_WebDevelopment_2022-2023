from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return f'{self.owner_id} ({self.first_name}): {self.last_name}'


class DrivingLicence(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)  # Also intersting options PROTECT, SET_NULL, SET_DEFAULT, RESTRICT
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10, null=True)


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.car_id}'


class Property(models.Model):
    car_owner_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


# TOFIX
# NULL and NOT NULL
# AUTO INC
