from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    room = models.ManyToManyField('Room', through='Booking')


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=4)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

    class RoomType(models.TextChoices):
        s = 's', "Standard"
        st = 'st', "Studio"
        js = 'js', "Junior Suite"
        su = 'su', "Suite"
        dl = 'dl', "Deluxe"
        fr = 'fr', "Family Room"
        hr = 'hr', "Honeymoon Room"

    room_type = models.CharField(choices=RoomType.choices, max_length=2)
    price = models.CharField(max_length=10)
    num_persons = models.CharField(max_length=1)

    def __str__(self):
        return self.number


class Booking(models.Model):
    date_in = models.DateField()
    date_out = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    checked_in = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Rating(models.TextChoices):
        f = '1', "Awful"
        d = '2', "Bad"
        c = '3', "Okay"
        b = '4', "Good"
        a = '5', "Great"

    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    rating = models.CharField(choices=Rating.choices, max_length=2)
    date_in = models.DateField()
    date_out = models.DateField()
    body = models.CharField(max_length=500)
