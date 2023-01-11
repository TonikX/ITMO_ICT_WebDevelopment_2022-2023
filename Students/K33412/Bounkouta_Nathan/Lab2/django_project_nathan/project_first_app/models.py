from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Owner(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Car(models.Model):
    Owner = get_user_model()
    number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    owner = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.number


class Ownership(models.Model):
    Owner = get_user_model()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)

    def __str__(self):
        return f"{self.owner} | {self.car}"


class License(models.Model):
    Owner = get_user_model()
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.number