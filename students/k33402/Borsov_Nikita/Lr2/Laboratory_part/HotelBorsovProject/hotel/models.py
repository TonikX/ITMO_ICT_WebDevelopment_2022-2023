from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Guest(AbstractUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'({self.pk}): {self.name} {self.surname}'


class Room(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    resident = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, blank=True)
    capacity = models.CharField(max_length=30, null=True)
    prestigue = models.CharField(max_length=30, null=True)
    cost = models.IntegerField(null=True)
    facilities = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'({self.pk}): {self.title}'


class Comment(models.Model):
    text = models.CharField(max_length=500)
    rating = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(Guest, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.pk})'
    # duration of living will be generated from author as last duration of living that user in that room


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
