from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.TextField(default='')
    middle_name = models.TextField(default='')
    last_name = models.TextField(default='')
    city = models.TextField(default='')
    passport = models.TextField(default='')
    is_admin = models.BooleanField(default=False)


class CleaningStaff(models.Model):
    first_name = models.TextField()
    middle_name = models.TextField()
    last_name = models.TextField()


class Room(models.Model):
    ROOM_TYPES = (
        ("SINGLE", "Single"),
        ("DOUBLE", "Double"),
        ("TRIPLE", "Triple"),
    )

    number = models.TextField()
    price = models.FloatField()
    floor = models.IntegerField()
    phone = models.IntegerField()
    room_type = models.TextField(choices=ROOM_TYPES)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name="bookings_guest", on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    approved = models.BooleanField(default=False)
    admin = models.ForeignKey(User, related_name="bookings_admin", on_delete=models.CASCADE)


class Cleaning(models.Model):
    WEEK_DAYS = (
        ("SUNDAY", "Sunday"),
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
    )

    staff = models.ForeignKey(CleaningStaff, related_name="cleaning", on_delete=models.CASCADE)
    floor = models.IntegerField()
    week_day = models.TextField(choices=WEEK_DAYS)
