from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.username

class Room(models.Model):
    ROOM_TYPE = (
        ('single', 'single'),
        ('double', 'double'),
        ('triple', 'triple'))
    type = models.CharField(max_length=10, choices=ROOM_TYPE, default='-', verbose_name='Type room', null=True)
    number = models.IntegerField(unique=True)
    phone = models.CharField(max_length=15, verbose_name='Phone number')
    price = models.IntegerField()
    STATUS_ROOM = (
        ('+', 'Available'),
        ('-', 'Occupied'))
    status = models.CharField(max_length=1, choices=STATUS_ROOM, default='-', verbose_name='Status room', null=True)
    guest_in = models.ManyToManyField('Guest', through='Booking', verbose_name='Guest')
    cleaners = models.ManyToManyField('Cleaners', through='Cleaning')

    def __str__(self):
        return f'Room #{self.number}'

class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE)
    check_in = models.DateField(verbose_name='Check-in')
    check_out = models.DateField(verbose_name='Check-out')

    def __str__(self):
        return f'{self.room} booked'    

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    room_book = models.ManyToManyField('Room', through='Booking', related_name='guests')

    def __str__(self):
        return f'Guest {self.first_name} {self.last_name}'

class Cleaners(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=10, unique=True)
    cleaner_id = models.IntegerField(primary_key=True)
    salary = models.IntegerField()

    def __str__(self):
        return f'Cleaner {self.first_name} {self.last_name}'

class Cleaning(models.Model):
    clean_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cleaning')
    cleaner_id = models.ForeignKey(Cleaners, on_delete=models.CASCADE, related_name='cleaning')
    date_time = models.DateTimeField(verbose_name='Cleaning day')

    def __str__(self):
        return f'Cleaning #{self.cleaner_id} in room {self.clean_room.number} at {self.date_time}'