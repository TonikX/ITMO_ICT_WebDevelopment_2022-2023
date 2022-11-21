from django.db import models

# Create your models here.

from django.db import models


class Car_Model(models.Model):
    vehicle_number = models.CharField(max_length=15)
    vehicle_brand = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=30, null=True)


class Owner_Model(models.Model):
    def __str__(self):
        return f'{self.surname} {self.name} {self.birthday}'

    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthday = models.DateTimeField(null=True)
    passport_number = models.CharField(max_length=10, null=True)
    home_address = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=10, null=True)


class Possession_Model(models.Model):
    id_owner = models.ManyToManyField('Owner_Model')
    id_vehicle = models.ManyToManyField('Car_Model')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)


class License_Model(models.Model):
    id_owner = models.ForeignKey(Owner_Model, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()
