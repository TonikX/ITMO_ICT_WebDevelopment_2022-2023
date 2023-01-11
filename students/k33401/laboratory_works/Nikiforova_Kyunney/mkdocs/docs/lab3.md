# Лабораторная работа №3

## Описание

>Гостиница (вариант из курса «Основы баз данных»)

Создать программную систему, предназначенную для администратора гостиницы.

Такая система должна обеспечивать хранение сведений об имеющихся в гостинице
номерах, о проживающих в гостинице клиентах и о служащих, убирающихся в номерах.
Количество номеров в гостинице известно, и имеются номера трех типов: одноместный,
двухместный и трехместный, отличающиеся стоимостью проживания в сутки. В каждом
номере есть телефон.

О каждом проживающем должна храниться следующая информация: номер
паспорта, фамилия, имя, отчество, город, из которого он прибыл, дата поселения в
гостинице, выделенный гостиничный номер.

О служащих гостиницы должна быть известна информация следующего содержания:
фамилия, имя, отчество, где (этаж) и когда (день недели) он убирает. Служащий
гостиницы убирает все номера на одном этаже в определенные дни недели, при этом в
разные дни он может убирать разные этажи.

<hr>

##Основные файлы проекта

* `models.py`
```python
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
```

* `views.py`
```python
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class GuestListView(generics.ListAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestCreateView(generics.CreateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class GuestDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Guest.objects.all()


class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class CleaningListView(generics.ListAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningCreateView(generics.CreateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class CleaningDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
```

* `serializers.py`
```python
from rest_framework import serializers
from .models import *


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
```

* `urls.py`
```python
from django.urls import path
from .views import *


urlpatterns = [
   path('guest/list', GuestListView.as_view()),
   path('guest/create', GuestCreateView.as_view()),
   path('guest/<int:pk>/update', GuestUpdateView.as_view()),
   path('guest/<int:pk>/delete', GuestDestroyView.as_view()),

   path('employee/list', EmployeeListView.as_view()),
   path('employee/create', EmployeeCreateView.as_view()),
   path('employee/<int:pk>/update', EmployeeUpdateView.as_view()),
   path('employee/<int:pk>/delete', EmployeeDestroyView.as_view()),

   path('cleaning/list', CleaningListView.as_view()),
   path('cleaning/create', CleaningCreateView.as_view()),
   path('cleaning/<int:pk>/update', CleaningUpdateView.as_view()),
   path('cleaning/<int:pk>/delete', CleaningDestroyView.as_view()),

   path('room/list', RoomListView.as_view()),
   path('room/create', RoomCreateView.as_view()),
   path('room/<int:pk>/update', RoomUpdateView.as_view()),
   path('room/<int:pk>/delete', RoomDestroyView.as_view()),

   path('booking/list', BookingListView.as_view()),
   path('booking/create', BookingCreateView.as_view()),
   path('booking/<int:pk>/update', BookingUpdateView.as_view()),
   path('booking/<int:pk>/delete', BookingDestroyView.as_view()),
]
```