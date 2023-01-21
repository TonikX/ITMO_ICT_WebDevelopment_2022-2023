from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField


class Ticket(models.Model):
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):

    api_url = models.CharField(
        max_length=100, default="https://airlabs.co/api/v9/airports?", blank=True)
    api_key = models.CharField(
        max_length=100, default="4a84701d-216b-4db5-a5f6-5b69f85fe6d7", blank=True)

    # def __str__(self):
    #     return f"{self.username} ({self.first_name} {self.last_name})"


class Flight(models.Model):
    FLIGHT_TYPES = (
        ('Departure', 'Departure'),
        ('Arrival', 'Arrival'),
    )

    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    flight_type = models.CharField(
        max_length=20, choices=FLIGHT_TYPES, default='Departure')

    gate = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    fligt_number = models.CharField(max_length=10)

    # iata_codes
    source_airport_code = models.CharField(max_length=10)
    destination_airport_code = models.CharField(max_length=10)

    max_reservations = models.IntegerField(default=120)
    reservators = models.ManyToManyField('User', blank=True)

    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )

    def __str__(self):
        return self.airline + " " + self.fligt_number

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                arrival__gt=models.F('departure')), name='departure_arrival_check', violation_error_message='Departure must be earlier than arrival.'),
        ]
