from django.db import models
from django.contrib.auth.models import AbstractUser


class Room(models.Model):
    number = models.IntegerField(unique=True)
    types = (
        ('single', 'single'),
        ('double', 'double'),
        ('triple', 'triple'),
    )
    type = models.CharField(max_length=20, choices=types, default='-', verbose_name='Type', null=True)
    phone = models.CharField(max_length=11, verbose_name='Phone number')
    price = models.IntegerField(verbose_name='Price', null=True)
    client_in = models.ManyToManyField('Client', through='Booking', verbose_name='Client', null=True)
    floor = models.IntegerField(verbose_name='Floor', null=True)

    def __str__(self):
        return f"{self.number}"


class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name='Room')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    check_in = models.DateField(verbose_name='Check-in')
    check_out = models.DateField(verbose_name='Check-out')


class Client(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    passport = models.CharField(max_length=11, verbose_name='Passport')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    town = models.CharField(max_length=50, verbose_name='Hometown')
    date = models.DateField(verbose_name='Check-in date')
    number = models.IntegerField(verbose_name='Hotel number')
    room_booked = models.ManyToManyField('Room', through='Booking', verbose_name='Room', null=True)
    REQUIRED_FIELDS = ['last_name', 'first_name', 'patronymic',
                       'passport', 'town', 'date', 'number']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Employee(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    floor = models.IntegerField(verbose_name='Floor')
    day = models.CharField(max_length=10, verbose_name='Weekday')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"