from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(AbstractUser):
    username = models.CharField("Username", max_length=30, null=False, unique=True)
    passport = models.CharField("Passport number", max_length=12, null=False)
    first_name = models.CharField("Name", max_length=30, null=False)
    lastname = models.CharField("Lastname", max_length=30, null=False)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class Flight(models.Model):
    flight_number = models.CharField("Flight number", max_length=20, unique=True)
    airline = models.CharField("Airline name", max_length=30, null=False)
    departure = models.DateTimeField("Departure date and time", null=False)
    arrival = models.DateTimeField("Arrival date and time", null=False)

    def __str__(self):
        return f"{self.airline}: {self.flight_number}"


class Ticket(models.Model):
    TYPE_FLIGHT = [('TO', 'Arrival'),
                   ('FROM', 'Departure')]
    ticket_id = models.CharField("Ticket number", primary_key=True, max_length=20, unique=True)
    seat = models.CharField("Place in plane", max_length=3, null=True)
    gate = models.CharField("Gate number", max_length=3, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    type = models.CharField("Flight type", max_length=30, choices=TYPE_FLIGHT)

    def __str__(self):
        return f"{self.flight} - {self.ticket_id}{self.seat == '' if '' else f'({self.seat})'}"


class Feedback(models.Model):
    comment = models.TextField("Comment", null=False)
    rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(limit_value=10),
                    MinValueValidator(limit_value=1)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField("Flight date")

    def __str__(self):
        return f"{self.flight}({self.user}) - {self.rate} - \'{self.comment[:10]}\' "
