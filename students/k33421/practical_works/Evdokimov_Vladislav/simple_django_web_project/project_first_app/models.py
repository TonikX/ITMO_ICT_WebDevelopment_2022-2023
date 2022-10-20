from django.db import models
from django.contrib.auth import get_user_model


class transport_Owner(models.Model):
    User = get_user_model()
    id_owner = models.IntegerField(primary_key=True)
    second_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    DOB = models.DateField(null=True)
    passport_data = models.IntegerField(null=False)
    email = models.CharField(max_length=30)
    nationality = models.CharField(max_length=20, null=True)
    home_adress = models.CharField(max_length=50, null=True)


class Drivers_license(models.Model):
    id_license = models.IntegerField(primary_key=True, null=False)
    id_owner = models.ForeignKey(transport_Owner, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10, null=False)
    type_license = models.CharField(max_length=10, null=False)
    date_start_license = models.DateField(null=False)


class Transport(models.Model):
    id_car = models.IntegerField(primary_key=True, null=False)
    registration_plate = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    car_model = models.CharField(max_length=20, null=False)
    colour = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_owner_transport = models.IntegerField(primary_key=True, null=False)
    id_owner = models.ForeignKey(transport_Owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True)


