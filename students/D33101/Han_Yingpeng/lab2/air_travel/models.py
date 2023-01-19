from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


AIR_TRAVEL_TYPES = [
        ('1', 'Arrival'),
        ('2', 'Departure'),
    ]

class Air_travel(models.Model):
    flight_number = models.CharField(max_length=200)
    airline = models.CharField(max_length=200,null=True)
    departure = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=AIR_TRAVEL_TYPES, default=AIR_TRAVEL_TYPES[0])
    gate_number = models.CharField(max_length=200)

    date = models.DateTimeField(null=True)
    
    

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Passenger(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.CharField(max_length=200, null=True)
    Air_travel = models.ForeignKey(Air_travel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.passenger.first_name,self.passenger.last_name, self.Air_travel.flight_number )


class Comment(models.Model):
    text = models.CharField(max_length=500)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    air_travel = models.ForeignKey(Air_travel, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
