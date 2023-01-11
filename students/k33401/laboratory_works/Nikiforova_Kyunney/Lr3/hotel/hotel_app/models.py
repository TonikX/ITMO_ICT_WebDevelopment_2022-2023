from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tel = models.CharField(max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class Guest(models.Model):
    first_name = models.CharField(max_length=70, verbose_name='Фамилия')
    last_name = models.CharField(max_length=70, verbose_name='Имя')
    patronymic = models.CharField(max_length=70, verbose_name='Отчество')
    passport = models.CharField(max_length=10, verbose_name='Номер пасспорта')
    city = models.CharField(max_length=30, verbose_name='Город, из которого прибыли')


class Employee(models.Model):
    first_name = models.CharField(max_length=70, verbose_name='Фамилия')
    last_name = models.CharField(max_length=70, verbose_name='Имя')
    patronymic = models.CharField(max_length=70, verbose_name='Отчество')


class Room(models.Model):
    ROOM_TYPE = (
        ('1', '1 bed'),
        ('2', '2 beds'),
        ('3', '3 beds')
    )
    STATE = (
        ("+", "Available"),
        ("-", "Occupied")
    )
    number = models.IntegerField(verbose_name='Номер комнаты')
    type = models.CharField(max_length=1, choices=ROOM_TYPE, verbose_name='Тип комнаты')
    price = models.IntegerField(verbose_name='Стоимость')
    floor = models.IntegerField(verbose_name='Этаж')
    state = models.CharField(max_length=1, choices=STATE, verbose_name='Статус')
    guest = models.ManyToManyField(Guest, verbose_name='Гость', through='Booking')
    employee = models.ManyToManyField(Employee, verbose_name='Сотрудник', through='Cleaning')


class Booking(models.Model):
    check_in_date = models.DateField(verbose_name='Дата заезда')
    check_out_date = models.DateField(verbose_name='Дата выезда')
    guest = models.ForeignKey(Guest, verbose_name='Гость', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='Комната', on_delete=models.CASCADE)


class Cleaning(models.Model):
    date = models.DateField(verbose_name='Дата уборки')
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='Комната', on_delete=models.CASCADE)
