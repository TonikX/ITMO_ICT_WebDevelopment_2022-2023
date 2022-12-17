from django.db import models

from users_app.models import User


class Hotel(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    desk = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.TextField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    type = models.TextField()
    room_description = models.TextField()
    conveniences = models.TextField()

    def __str__(self):
        return f"{self.number} {self.hotel}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} at {self.room}"


class Comment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField()
