from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

User = get_user_model()


class City(models.Model):
    name = models.CharField('City name', max_length=64, unique=True)
    slug = models.SlugField('City link', max_length=64, unique=True)

    def get_absolute_url(self):
        return reverse('city_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField('Airline name', max_length=64, unique=True)
    slug = models.SlugField('Airline link', max_length=64, unique=True)

    def get_absolute_url(self):
        return reverse('airline_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Flight(models.Model):
    number = models.CharField('Flight number', max_length=10, db_index=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    city_from = models.ForeignKey(City, related_name='flights_from', on_delete=models.CASCADE)
    city_to = models.ForeignKey(City, related_name='flights_to', on_delete=models.CASCADE)
    departure = models.DateTimeField('Departure datetime', null=False)
    arrival = models.DateTimeField('Arrival datetime', null=False)
    slug = models.SlugField(max_length=150, unique=True)
    can_buy = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number}: {self.city_from} - {self.city_to}. Departure at {self.departure}"

    def get_absolute_url(self):
        return reverse('flight_details_url', kwargs={'slug': self.slug})


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # to be filled in when purchasing the ticket
    passenger_name = models.CharField(max_length=32, null=False)
    passenger_surname = models.CharField(max_length=32, null=False)
    passenger_passport = models.CharField(max_length=10, null=False)
    # to be filled in at check-in
    seat = models.CharField(max_length=3, null=True, blank=True, default=None)

    review_text = models.TextField(null=True, default=None, blank=True)
    rate = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self):
        return f"[{self.flight}] {self.passenger_surname} {self.passenger_name}"
