from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators  import MaxValueValidator, MinValueValidator

class Passenger(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    passport_number = models.CharField(max_length=15,unique=True)

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Airline(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Flight(models.Model):
    TYPE_CHOICES = [
        ('IN', 'Arrival'),
        ('OUT', 'Departure'),
    ]
    passengers = models.ManyToManyField(Passenger, through='Ticket', related_name='passenger')
    reviewers = models.ManyToManyField(Passenger, through='Review', related_name='reviewer')
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
    flight_number = models.CharField(max_length=6,unique=True)
    hotel = models.CharField(max_length=30, null=True, blank=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    gate_number = models.CharField(max_length=3)

    def __str__(self):
        return self.flight_number

class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    ticket_number = models.CharField(max_length=10,unique=True)
    seat = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.ticket_number

class Review(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=1)
        ]
    )

