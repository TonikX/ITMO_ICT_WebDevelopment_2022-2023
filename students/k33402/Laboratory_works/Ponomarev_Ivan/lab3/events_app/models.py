import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length=30)
    phone = models.BigIntegerField(default=79999999999, editable=True)
    user_image = models.ImageField(default="img/profile.png", upload_to="img")

    def __str__(self):
        return "{} {}".format(self.username, self.id, self.phone)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Location(models.Model):
    cities = [('Moscow', 'Москва'),
              ('Saint-Petersburg', 'Санкт-Петербург'),
              ('Kazan', 'Казань'),
              ('Tver', 'Тверь'),
              ('Vyborg', 'Выборг'),
              ('Kaliningrad', 'Калининград'),
              ('Sochi', 'Сочи')]
    city = models.CharField(max_length=20, choices=cities)
    street = models.CharField(max_length=40)
    max_count = models.IntegerField()
    place_name = models.CharField(max_length=40, default="none")

    def __str__(self):
        return "{}".format(self.place_name)


class Event(models.Model):
    organizer = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    place = models.ForeignKey(Location, on_delete=models.CASCADE)
    about = models.CharField(max_length=2000)
    intro = models.CharField(max_length=500)
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.time.max)
    name = models.CharField(max_length=500, default='none')
    participants = models.ManyToManyField(User, through="UserEventEnrollment")

    def __str__(self):
        return "{}".format(self.name)


class UserEventEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.user, self.event)