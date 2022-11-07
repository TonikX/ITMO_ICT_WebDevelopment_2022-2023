from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class Owner(models.Model):
    organization_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.organization_name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Facilities(models.Model):
    pets_allowed = models.BooleanField()
    parking = models.BooleanField()
    restaurant = models.BooleanField()
    free_wifi = models.BooleanField()
    spa = models.BooleanField()
    fitness_centre = models.BooleanField()
    facilities_for_disabled = models.BooleanField()


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.ManyToManyField(RoomType)
    capacity = models.IntegerField()
    price = models.FloatField()
    facilities = models.ManyToManyField(Facilities)

    def __str__(self):
        return self.hotel.name + " " + self.name


class Reservation(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + " " + self.room + " " + self.date_start + "-" + self.date_end


def validate_range(value):
    if value < 0 or value > 10:
        raise ValidationError(f"{value} is outside the range 0...10")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    rating = models.IntegerField(validators=[validate_range])
    created = models.DateTimeField(auto_now=True)
