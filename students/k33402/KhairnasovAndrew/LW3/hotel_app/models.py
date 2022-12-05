from django.db import models

from users_app.models import User


class Room(models.Model):
    ROOM_TYPES = (
        ("SINGLE", "Single"),
        ("DOUBLE", "Double"),
        ("TRIPLE", "Triple"),
    )

    number = models.TextField(default="")
    price = models.FloatField()
    floor = models.IntegerField()
    phone = models.IntegerField()
    room_type = models.TextField(choices=ROOM_TYPES)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE,
                              limit_choices_to={"is_cleaning_staff": False, "is_superuser": False})
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()


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

    staff = models.ForeignKey(User, related_name="cleaning", on_delete=models.CASCADE,
                              limit_choices_to={"is_cleaning_staff": True, "is_superuser": False})
    floor = models.IntegerField()
    week_day = models.TextField(choices=WEEK_DAYS)
