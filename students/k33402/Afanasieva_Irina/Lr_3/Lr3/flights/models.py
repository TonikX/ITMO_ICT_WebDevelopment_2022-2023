from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

class Passenger(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=100)

    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return "{} - {} {}".format(self.username, self.first_name, self.last_name)

class AirCompany(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return "{} ({})".format(self.name, self.phone)

class Plane(models.Model):
    company = models.ForeignKey(AirCompany, on_delete=models.CASCADE,blank=True, null=True, default=1 )
    model = models.CharField(max_length=50)
    prod_date = models.DateField()

    def __str__(self):
        return "{}, {}".format(self.model, self.company)


class Flight(models.Model):
    number = models.CharField(max_length=10, unique=True)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, blank=True, null=True, default=1)
    departure = models.CharField(max_length=30, default="2022-03-12 11:30")
    arrival = models.CharField(max_length=30, default="2022-03-12 13:30")
    wherefrom = models.CharField(max_length=50)
    whereto = models.CharField(max_length=50)
    gate = models.CharField(max_length=10)

    def __str__(self):
        return "{}, {} -> {}".format(self.number, self.wherefrom, self.whereto)

class Ticket(models.Model):
    number = models.CharField(max_length=10, unique=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,blank=True, null=True, default=5)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE,blank=True, null=True, default=5)

    def __str__(self):
        return "№{} from {} to {}: {} {}".format(self.number, self.flight.wherefrom, self.flight.whereto,
                                                 self.passenger.first_name, self.passenger.last_name)


