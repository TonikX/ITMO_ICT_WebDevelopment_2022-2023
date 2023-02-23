from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CarOwner(AbstractUser):
    id_owner = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    passport = models.CharField(blank=True, max_length=11)
    home_address = models.CharField(blank=True, max_length=100)
    nationality = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class DriverLicense(models.Model):
    id_license = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField(blank=False)

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    state_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(blank=True, max_length=30)
    owners = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Ownership',
        through_fields=('id_car', 'id_owner'),
    )

    def __str__(self):
        return "{} {} {}".format(self.brand, self.model, self.state_num)


class Ownership(models.Model):
    id_owner_car = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car,on_delete=models.CASCADE)
    date_start = models.DateField(blank=False)
    date_end = models.DateField(blank=True, null=True)

