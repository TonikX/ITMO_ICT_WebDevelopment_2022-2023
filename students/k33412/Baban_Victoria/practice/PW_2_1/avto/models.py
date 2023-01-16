from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Car_owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birthday = models.DateField()


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

class Ownership(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

class Drivers_license(models.Model):
    id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10)
    date_issue = models.DateField()

