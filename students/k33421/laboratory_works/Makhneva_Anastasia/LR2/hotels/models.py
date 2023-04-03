from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    amenities = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


ROOM_STATUS = (
    ('занято', 'занято'),
    ('свободно', 'свободно'),
    ('закрыто', 'закрыто')
)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    availability = models.CharField(
        max_length=50, choices=ROOM_STATUS, default=ROOM_STATUS[1])

    def __str__(self):
        return str(self.id)


STATUSES = (
    ('бронь', 'бронь'),
    ('заехал', 'заехал'),
    ('выехал', 'выехал'),
    ('отменено', 'отменено'),
)


class Reservation(models.Model):
    date_check_in = models.DateField()
    date_check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUSES)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=500)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(0, 11)], default=(0, 0))
    reservation = models.ForeignKey(
        Reservation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.reservation.id + ' ' + self.reservation.guest.first_name
