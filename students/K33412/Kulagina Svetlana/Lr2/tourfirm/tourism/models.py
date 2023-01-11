from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Tourist(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.first_name)

Tourist = get_user_model()

class Agency(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Tour(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    agency_id = models.ForeignKey(Agency, on_delete=CASCADE)
    beginning_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    country = models.ForeignKey(Country, on_delete=CASCADE, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)

class Reservation(models.Model):
    tourist_id = models.ForeignKey(Tourist, on_delete=CASCADE)
    tour_id = models.ForeignKey(Tour, on_delete=CASCADE)

    def __str__(self):
        return str(self.tour_id)

class Comment(models.Model):
    tourist_id = models.ForeignKey(Tourist, on_delete=CASCADE)
    tour_id = models.ForeignKey(Tour, on_delete=CASCADE)
    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    beginning_date = models.DateField(null=True)
    ending_date = models.DateField(null=True)
    rating = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))
    rate = models.CharField(max_length=30, choices=rating)

    def __str__(self):
        return str(self.title)
