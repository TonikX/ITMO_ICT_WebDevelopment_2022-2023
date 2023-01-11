from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
User = get_user_model()


class Hotel(models.Model):
    name = models.CharField(max_length=63)
    owner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Room(models.Model):
    number = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=127)
    cost = models.PositiveIntegerField()
    beds = models.PositiveSmallIntegerField()
    amenities = models.CharField(max_length=255, blank=True, null=True)


class Booking(models.Model):
    reservee = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    approved = models.BooleanField(default=False)


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
