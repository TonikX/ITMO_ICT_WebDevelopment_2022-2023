from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

class Location(models.Model):
    title = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

class EventType(models.Model):
    title = models.CharField(max_length=50, unique=True)

class Event(models.Model):
    organizer = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    datetime = models.DateField()
    event_type = models.ForeignKey(EventType,on_delete=models.CASCADE)

class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

