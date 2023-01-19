from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


AIR_TRAVEL_TYPES = [
        ('1', 'Arrival'),
        ('2', 'Departure'),
    ]


class Airline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Air_travel(models.Model):
    flight_number = models.CharField(max_length=200)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=AIR_TRAVEL_TYPES, default=AIR_TRAVEL_TYPES[0])
    gate_number = models.CharField(max_length=200)

    date = models.DateTimeField(null=True)


class Passenger(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE,related_name="passenger")
    ticket = models.CharField(max_length=200, null=True)
    Air_travel = models.ForeignKey(Air_travel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.start_time)
    
    

    creator = models.ForeignKey(User, on_delete=models.CASCADE,related_name="creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    text = models.CharField(max_length=500)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    air_travel = models.ForeignKey(Air_travel, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
