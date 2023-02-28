from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Guest(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    Guest = get_user_model()
    number = models.IntegerField()
    type = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    capacity = models.IntegerField(null=True)
    amenities = models.CharField(max_length=30, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    guest = models.ManyToManyField(Guest, through='Accommodation')

    def __str__(self):
        return f"{self.number} | {self.hotel}"


class Accommodation(models.Model):
    Guest = get_user_model()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.guest} | {self.check_in_date} | {self.check_out_date}"


class Comment(models.Model):
    Guest = get_user_model()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(null=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.guest} | {self.rating}"
