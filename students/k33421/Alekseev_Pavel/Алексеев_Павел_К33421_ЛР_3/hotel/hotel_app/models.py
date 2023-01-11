from django.db import models
from django.contrib.auth.models import AbstractUser


class Room(models.Model):
    id_room = models.AutoField("id_room", primary_key=True)
    type = models.ForeignKey("TypeRoom", on_delete=models.CASCADE, verbose_name="Тип комнаты")
    room_number = models.IntegerField(verbose_name="Номер комнаты", null=False)


class TypeRoom(models.Model):
    id_type = models.AutoField("id_type", primary_key=True)
    TYPE_PEOPLE = [("1", "Одноместный"), ("2", "Двухместный"), ("3", "Трехместный")]
    TYPE_ROOM = [("1", "Стандарт"), ("2", "Полу-люкс"), ("3", "Люкс")]
    type_people = models.CharField(max_length=6, default='1', choices=TYPE_PEOPLE, verbose_name='Тип комнаты к-в людей')
    type_room = models.CharField(max_length=6, default='1', choices=TYPE_ROOM, verbose_name='Тип номера')
    comfort = models.TextField(verbose_name='Удобства')
    price = models.IntegerField(verbose_name="Цена", null=False)


class Client(AbstractUser):
    passport = models.CharField(max_length=11, verbose_name='pasport', primary_key=True)
    last_name = models.CharField(max_length=50, verbose_name='Отчество', null=False)
    first_name = models.CharField(max_length=50, verbose_name='Имя', null=False)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=False)
    email = models.CharField(max_length=50, verbose_name='эл.почта', null=False)
    phone = models.CharField(max_length=50, verbose_name='Телефон', null=False)
    address = models.CharField(max_length=500, verbose_name='Адрес проживания', null=False)


class Employee(models.Model):
    id_emp = models.AutoField("id_worker", primary_key=True)
    last_name = models.CharField(max_length=50, verbose_name='Отчество', null=False)
    first_name = models.CharField(max_length=50, verbose_name='Имя', null=False)
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=False)
    phone = models.CharField(max_length=50, verbose_name='Телефон', null=False)
    address = models.CharField(max_length=500, verbose_name='Адрес проживания', null=False)


class Booking(models.Model):
    number_booking = models.AutoField('id_booking', max_length=100, primary_key=True)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    id_worker = models.ForeignKey("Employee", on_delete=models.CASCADE)
    passport_client = models.ForeignKey("Client", on_delete=models.CASCADE)
    check_in = models.DateField(verbose_name="Дата заезда", null=False)
    check_out = models.DateField(verbose_name="Дата выезда", null=False)
    STATUS_BOOK = [("0", "Свободен"), ("1", "Занят")]
    status_book = models.CharField(verbose_name="Статус бронирования", choices=STATUS_BOOK, null=False, max_length=20)
    STATUS_PAYMENT = [("0", "Не оплачено"), ("1", "Оплачено")]
    status_payment = models.CharField(verbose_name="Статус оплаты", choices=STATUS_PAYMENT, null=False, max_length=20)

