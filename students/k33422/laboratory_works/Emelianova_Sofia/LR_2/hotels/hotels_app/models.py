from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import NOT_PROVIDED
from datetime import datetime    


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

    def __str__(self):
        if self.is_superuser:
            return 'superuser'
        return self.last_name + ' ' + self.first_name

class Hotel(models.Model):
    guests = models.ManyToManyField(User, through='Reservation')
    hotel_name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return ' "' + self.hotel_name + '", владелец отеля: ' + self.owner

class Reservation(models.Model):
    BASE = 'Простой'
    LUXE = 'Люкс'
    PRESIDENTIAL = 'Президентский'

    APPROVED = 'Подтверждена'
    NOT_APPROVED = 'Не рассмотрена'
    CHECKED_IN = 'Заселен'

    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(
        max_length=30,
        choices=[(BASE, 'Простой'), (LUXE, 'Люкс'), (PRESIDENTIAL, 'Президентский')])
    num_of_guests = models.IntegerField(choices=[(i, i) for i in range(1, 5)])
    approval = models.CharField(
        max_length=15,
        choices=[(APPROVED, 'Подтверждена'), (NOT_APPROVED, 'Не рассмотрена'), (CHECKED_IN, 'Заселен')], default=NOT_APPROVED)
    check_in_date = models.DateField(default=datetime.now)
    check_out_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.guest} | {self.check_in_date} | {self.check_out_date}"

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)])
    comment = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f" ( {self.author} ) | {self.rating}/10"