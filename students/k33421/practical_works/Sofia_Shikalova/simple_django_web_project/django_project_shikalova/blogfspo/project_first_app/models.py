from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class Owner(models.Model):
    id_owner = models.IntegerField(primary_key = True)
    last_name = models.CharField(max_length = 30, null = False)
    first_name = models.CharField(max_length = 30, null = False)
    birth_day = models.DateField(null = True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Certificate(models.Model):
    #OwnerUser = get_user_model()
    id_owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    cert_number = models.CharField(max_length = 10, null = False)
    cert_type = models.CharField(max_length = 10, null = False)
    date_of_issue = models.DateField()

    def __str__(self):
        return self.number


class Car(models.Model):
    #OwnerUser = get_user_model()
    id_car = models.IntegerField(primary_key = True)
    state_number = models.CharField(max_length = 15, null = False)
    brand = models.CharField(max_length = 20, null = False)
    model = models.CharField(max_length = 20, null = False)
    color =  models.CharField(max_length = 30, null = True)
    owner = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.state_number


class Ownership(models.Model):
    id_ownership = models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null = True)

    def __str__(self):
        return f"{self.id_owner} | {self.id_car}"