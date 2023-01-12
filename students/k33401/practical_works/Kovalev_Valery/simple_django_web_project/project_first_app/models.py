from django.db import models


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthdate = models.DateField(blank=True, null=True)


class Car(models.Model):
    car_number = models.CharField(max_length=15, unique=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)


class Own(models.Model):
    start_own_date = models.DateField()
    end_own_date = models.DateField(blank=True, null=True)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


class License(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=10)
    reg_date = models.DateField()
