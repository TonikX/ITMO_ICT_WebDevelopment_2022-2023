from django.db import models

class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    room_type = models.ForeignKey('Price', on_delete=models.CASCADE, verbose_name='Тип номера')
    phone = models.CharField(max_length=7, verbose_name='Номер телефона')
    id_floor = models.ForeignKey('Floor', on_delete=models.CASCADE, verbose_name='Этаж')
    clients = models.ManyToManyField('Client', verbose_name='Клиенты', through='Booking', related_name='client_room')

class Price(models.Model):
    id_price = models.AutoField(primary_key=True)
    room_types = (
       ('s', 'single'),
       ('d', 'double'),
       ('t', 'triple'),
    )
    room_type = models.CharField(max_length=1, choices=room_types, verbose_name='Тип номера')
    price_daily = models.FloatField(verbose_name='Стоимость за сутки')

class Client(models.Model):
    passport = models.CharField(primary_key=True, max_length=10, verbose_name='Номер паспорта')
    last_name_client = models.CharField(max_length=120, verbose_name='Фамилия проживающего')
    first_name_client = models.CharField(max_length=120, verbose_name='Имя проживающего')
    patronymic_client = models.CharField(max_length=120, verbose_name='Отчество проживающего')
    city = models.CharField(max_length=120, verbose_name='Родной город')

    def __str__(self):
        return self.passport

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Проживающий')
    id_room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name='Выделенный номер')
    date_start = models.DateField(verbose_name='Дата поселения')
    date_end = models.DateField(verbose_name='Дата выселения', blank=True, null=True)
    
class Cleaner(models.Model):
    id_cleaner = models.AutoField(primary_key=True)
    last_name_cleaner = models.CharField(max_length=120, verbose_name='Фамилия служащего')
    first_name_cleaner = models.CharField(max_length=120, verbose_name='Имя служащего')
    patronymic_cleaner = models.CharField(max_length=120, verbose_name='Отчество служащего')
    floors = models.ManyToManyField('Floor', verbose_name='Обслуживаемые этажи', through='Schedule', 
                                    related_name='floor_cleaner')
    
class Floor(models.Model):
    id_floor = models.AutoField(primary_key=True)
    floor_num = models.IntegerField(verbose_name='Этаж')

class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True)
    id_cleaner = models.ForeignKey('Cleaner', on_delete=models.CASCADE, verbose_name='Служащий')
    id_floor = models.ForeignKey('Floor', on_delete=models.CASCADE, verbose_name='Этаж для уборки')
    day_choices = (
       ('mon', 'monday'),
       ('tue', 'tuesday'),
       ('wed', 'wednesday'),
       ('thu', 'thursday'),
       ('fri', 'friday'),
       ('sat', 'saturday'),
       ('sun', 'sunday'),
    )
    day = models.CharField(max_length=3, choices=day_choices, verbose_name='День недели')