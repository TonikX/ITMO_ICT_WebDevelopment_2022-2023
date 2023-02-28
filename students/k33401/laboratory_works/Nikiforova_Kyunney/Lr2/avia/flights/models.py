from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# модель пассажира
class Passenger(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    passport = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.passport


# модель авиакомпании
class Airline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# модель рейса
class Flight(models.Model):
    TYPE_CHOICES = [
        ('in', 'Arrival'),
        ('out', 'Departure'),
    ]
    flight_number = models.CharField(max_length=6,unique=True)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    gate_number = models.CharField(max_length=3)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.flight_number


# модель билета
class Ticket(models.Model):
    passport = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)


# модель отзыва
class Comment(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
