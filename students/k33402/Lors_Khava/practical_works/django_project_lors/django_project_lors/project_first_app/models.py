from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)
    nationality = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class License(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issuance = models.DateField()
    
    def __str__(self):
        return self.license_num

class Car(models.Model):
    owner = models.ManyToManyField(Owner, through='Ownership') # в данной строке through='Ownership' указывает на таблицу, которая будет использоваться, как ассоциативная сущность.
    state_num = models.CharField(max_length=15)
    stamp = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.state_num

class Ownership(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.owner}: {self.car}"

