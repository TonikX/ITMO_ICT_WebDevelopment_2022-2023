from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    passport = models.CharField(max_length=10, verbose_name='Паспортные данные', unique=True)
    full_name = models.CharField(max_length=120, null=False, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст', default=18)
    education = models.CharField(choices=[('СПО', 'среднее профессиональное'), ('ВО', 'высшее')], max_length=3,
                                 verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы в годах')
    in_crew = models.IntegerField(verbose_name='Состоит в экипаже под номером', default=0)

    REQUIRED_FIELDS = ['email', 'full_name', 'experience']

    def __str__(self):
        return "{}".format(self.full_name)


class Airplane(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    tail_number = models.CharField(max_length=8, verbose_name="Номер самолета", unique=True)
    type = models.CharField(max_length=20, verbose_name="Тип")
    seats = models.IntegerField(verbose_name="Число мест")
    velocity = models.IntegerField(verbose_name="Скорость полёта (км/ч)")
    airline = models.CharField(max_length=30, verbose_name="Авиакомпания")
    under_maintenance = models.BooleanField(default=False, verbose_name="В ремонте")

    def __str__(self):
        return "{}".format(self.tail_number)


class FlightAsScheduled(models.Model):
    number = models.IntegerField(unique=True, primary_key=True, verbose_name="Номер рейса")
    distance = models.IntegerField(verbose_name="Расстояние до пункта назначения в км")
    departure = models.CharField(max_length=25, verbose_name="Пункт вылета")
    arrival = models.CharField(max_length=25, verbose_name="Пункт назначения")
    transit = models.ForeignKey('Transit', verbose_name="Транзит", null=True, blank=True, on_delete=models.CASCADE)
    completed = models.IntegerField(verbose_name="Количество совершённых рейсов")

    def __str__(self):
        return "{}, {} -> {}".format(self.number, self.departure, self.arrival)


class Transit(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    destination = models.CharField(max_length=25, verbose_name="Пункт пересадки")

    def __str__(self):
        return "{}".format(self.destination)


class Flight(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.ForeignKey('FlightAsScheduled', verbose_name="Номер рейса", on_delete=models.CASCADE)
    plane_id = models.ForeignKey('Airplane', verbose_name="Самолёт", on_delete=models.CASCADE)
    crew = models.IntegerField(verbose_name="Экипаж на борту")
    tickets_sold = models.IntegerField(verbose_name="Количество проданных билетов")
    departure_date = models.DateField(verbose_name="Дата вылета")
    departure_time = models.TimeField(verbose_name="Время вылета")
    arrival_date = models.DateField(verbose_name="Дата прилета")
    arrival_time = models.TimeField(verbose_name="Время прилета")
    transit_arrival_date = models.DateField(verbose_name="Дата транзитной посадки", blank=True, null=True)
    transit_arrival_time = models.TimeField(verbose_name="Время транзитной посадки", blank=True, null=True)
    transit_departure_date = models.DateField(verbose_name="Дата вылета из транзита", blank=True, null=True)
    transit_departure_time = models.TimeField(verbose_name="Время вылета из транзита", blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.number, self.plane_id)


class AirlineAdministration(models.Model):
    employee = models.ForeignKey('Employee', verbose_name="ФИО сотрудника", on_delete=models.CASCADE)
    job = models.CharField(max_length=30, verbose_name="Должность")
    clearance = models.BooleanField(default=True, verbose_name="Допуск")
