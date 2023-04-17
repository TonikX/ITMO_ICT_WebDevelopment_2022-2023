from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    POS = (('s', 'steward'), ('c', 'commander'), ('p', 'second pilot'), ('n', 'navigator'))
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=20, choices=POS)
    education = models.CharField(max_length=500)
    experience = models.IntegerField()
    passport = models.CharField(max_length=11, unique=True)


class Plane(models.Model):
    number = models.CharField(max_length=7, unique=True)
    type = models.CharField(max_length=10)
    num_seats = models.IntegerField()
    speed = models.IntegerField()
    company = models.CharField(max_length=50)


class TransitLanding(models.Model):
    airport = models.CharField(max_length=30)
    arr_dt = models.DateTimeField()
    dep_dt = models.DateTimeField()


class Flight(models.Model):
    numbers = models.IntegerField()
    distance = models.IntegerField()
    air_departure = models.CharField()
    air_arrival = models.CharField()
    dep_dt = models.DateTimeField()
    arr_dt = models.DateTimeField()
    plane = models.ForeignKey(Plane, related_name='flight', on_delete=models.SET_NULL, blank=True, null=True)
    transit_land = models.ManyToManyField(TransitLanding, related_name='flight', blank=True)
    employee = models.ManyToManyField(Employee, through='allowance', related_name='flight')


class Allowance(models.Model):
    employee = models.ForeignKey(Employee, related_name='allowance', on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='allowance', on_delete=models.CASCADE)
    status = models.BooleanField()
