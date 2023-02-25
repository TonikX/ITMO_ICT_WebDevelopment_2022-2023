from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Passenger(models.Model):
#     passport = models.CharField(primary_key=True, max_length=30)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.passport

class Flight(models.Model):
    id_flight = models.CharField(primary_key=True, max_length=30)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField(blank=False)
    airline = models.CharField(max_length=50)
    COMFORT_CHOICES = [
        ("E", "Economy"),
        ("B", "Business"),
        ("F", "First"),
    ]
    comfort = models.CharField(max_length=2, choices=COMFORT_CHOICES)
    seat_number = models.IntegerField(blank=False)

    def __str__(self):
        return self.id_flight

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    passport = models.ForeignKey(User, on_delete=models.CASCADE)
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    LUGGAGE_CHOICES = [
        ("Y", "YES"),
        ("N", "NO"),
    ]
    luggage = models.CharField(max_length=2, choices=LUGGAGE_CHOICES)
    APPROVED_CHOICES = [
        ("Y", "YES"),
        ("N", "NO"),
    ]
    approved = models.CharField(max_length=2, choices=APPROVED_CHOICES, default="N")
    ticket_number = models.CharField(max_length=30, blank=True)


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date_reviewed = models.DateTimeField(default=timezone.now)
    RATING_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ]
    rating = models.CharField(max_length=2, choices=RATING_CHOICES)