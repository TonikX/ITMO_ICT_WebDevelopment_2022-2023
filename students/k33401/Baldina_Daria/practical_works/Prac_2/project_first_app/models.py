from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Car_owner(AbstractUser):
    id_owner = models.IntegerField(primary_key = True)
    last_name = models.CharField(max_length = 30, null = False)
    first_name = models.CharField(max_length = 30, null = False)
    birth_day = models.DateField(null = True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

class Car(models.Model):
    id_car = models.IntegerField(primary_key = True)
    state_number = models.CharField(max_length = 15, null = False)
    mark_car = models.CharField(max_length = 20, null = False)
    model_car = models.CharField(max_length = 20, null = False)
    color =  models.CharField(max_length = 30, null = True)

class Ownerdhip(models.Model):
    id_owner_car = models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE, related_name='owner')
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name='car')
    start_date = models.DateField()
    end_date = models.DateField(null = True)

class Driver_license(models.Model):
    id_license =  models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE, related_name='car_owner')
    license_number = models.CharField(max_length = 10, null = False)
    type = models.CharField(max_length = 10, null = False)
    date_of_license= models.DateField()