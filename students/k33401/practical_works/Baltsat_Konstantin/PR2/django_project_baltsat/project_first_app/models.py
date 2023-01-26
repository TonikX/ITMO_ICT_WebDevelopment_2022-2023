from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Car_owner(AbstractUser):
    id_owner = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=True)
    ####
    passport = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
         return '{} {}'.format(self.first_name, self.last_name)



class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    number_plate = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key=True)
    # id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class Driver_license(models.Model):
    id_license = models.IntegerField(primary_key=True)
    # id_owner = models.ForeignKey(Car_owner, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    issue_date = models.DateField()
