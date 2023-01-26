from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        if self.is_superuser:
            return 'superuser'
        return self.last_name + ' ' + self.first_name


class Flight(models.Model):
    passengers = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Reservation')
    number = models.CharField(max_length=30)
    airline = models.CharField(max_length=30)
    departure = models.DateField()
    arrival = models.DateField()
    gate = models.CharField(max_length=10)

    DEPARTURE = 'Departure'
    ARRIVAL = 'Arrival'
    type = models.CharField(
        max_length=30,
        choices=[(DEPARTURE, 'Departure'), (ARRIVAL, 'Arrival')]
    )

    def __str__(self):
        return self.airline + ' ' + self.number


class Reservation(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.CharField(max_length=15)
    ticket = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return 'Резервирование'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 10)])
    comment = models.CharField(max_length=400, blank=True, null=True)
