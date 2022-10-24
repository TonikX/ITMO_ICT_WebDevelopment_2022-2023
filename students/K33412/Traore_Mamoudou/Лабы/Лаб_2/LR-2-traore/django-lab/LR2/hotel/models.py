from django.db import models
from django.contrib.auth.models import AbstractUser


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    address = models.CharField(max_length=60, default='SOME STRING')

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    number = models.CharField(max_length=4)

    class RoomType(models.TextChoices):
        std = 'STD', "Standard"
        bdr = 'BDR', "With bedroom"
        brt = '2BDR', "With 2 bedrooms"
        sui = 'SUI', "Suite"
        ksu = 'KSU', "King Suite"
        vll = 'VLL', "Villa"
        bgg = 'BGG', "Bungalo"

    room_type = models.CharField(choices=RoomType.choices, max_length=4)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Client(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birthday = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    room = models.ManyToManyField('Room', through='Booking')


class Booking(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    people = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    check_in = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)

    class Rating(models.IntegerChoices):
        very_bad = 1
        bad = 2
        neutral = 3
        good = 4
        excellent = 5

    rating = models.IntegerField(choices=Rating.choices, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    text = models.CharField(max_length=1000)