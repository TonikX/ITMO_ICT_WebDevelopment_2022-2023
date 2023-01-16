from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    plate_number = models.CharField(max_length=20)


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()


class OwnedCars(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class DrivingLicense(models.Model):
    TYPES = (
        ('M', 'Quadrocycles'),
        ('A', 'Motorcycles'),
        ('B', 'Car'),
        ('C', 'Light Trucks'),
        ('E', 'Trailers')
    )
    id_number = models.CharField(max_length=30)
    date_of_giving = models.DateField()
    category = models.CharField(max_length=5, choices=TYPES)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
