import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Plane(models.Model):
    plane_name = models.CharField(max_length=30)
    seats_count = models.IntegerField(max_length=525)

    def __str__(self):
        return self.plane_name


class Flight(models.Model):
    flight_type = [("Arrival", "Arrival"),
                   ("Departure", "Departure")]
    gate_number = [(f"A0{i}", f"A0{i}") for i in range(0, 10)]
    city_choices = [("Moscow", "Moscow"),
                    ("Saint-Petersburg", "Saint-Petersburg"),
                    ("Kaliningrad", "Kaliningrad"),
                    ("Sochi", "Sochi"),
                    ("Nalchik", "Nalchik"),
                    ("Grozny", "Grozny"),
                    ("Mahachkala", "Mahachkala"),
                    ("Krasnodar", "Krasnodar"),
                    ("Anapa", "Anapa")]
    flight_number = models.CharField(max_length=10, unique=True)
    gate_number = models.CharField(max_length=3, choices=gate_number)
    out_place = models.CharField(max_length=20, choices=city_choices)
    arrival_place = models.CharField(max_length=20, choices=city_choices)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    airline = models.CharField(max_length=50)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    type_of_flight = models.CharField(max_length=9, choices=flight_type)

    def get_seats(self):
        if self.ticket_set.count() != 0:
            occ_seats = list(map(int, self.ticket_set.values_list("seat")[0]))
            available_seats = [i for i in range(1, self.plane.seats_count+1) if i not in occ_seats]
            return available_seats
        else:
            return range(1, self.plane.seats_count +1)

    def get_absolute_url(self):
        return reverse('get_flight_url', kwargs={'slug': self.flight_number})

    def get_passengers_url(self):
        return reverse('get_passengers_url', kwargs={'slug': self.flight_number})

    def is_done(self):
        print(self.arrival_date.date() <= datetime.date.today())
        return self.arrival_date.date() <= datetime.date.today()

    def __str__(self):
        return self.flight_number


class Ticket(models.Model):
    ticket_number = models.IntegerField(max_length=30)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('get_certain_book_url', kwargs={'slug': self.ticket_number})

    def __str__(self):
        return "{}".format(self.ticket_number)


class Comment(models.Model):
    comment_number = models.IntegerField()
    rate_choices = [(1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10)]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rate_choices)

    def __str__(self):
        return "{}".format(self.comment_number)
