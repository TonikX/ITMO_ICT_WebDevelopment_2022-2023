---
description: Реализация серверной части на django rest. Документирование API.
---

# Лабораторная работа 3

Цель работы: овладеть практическими навыками реализации серверной части (backend) приложений средствами Django REST framework.



Задание:

Вариант - Hotel

* models.py

```
from django.db import models
from django.contrib.auth.models import AbstractUser


class Room(models.Model):
    number = models.IntegerField(unique=True)
    types = (
        ('single', 'single'),
        ('double', 'double'),
        ('triple', 'triple'),
    )
    type = models.CharField(max_length=20, choices=types, default='-', verbose_name='Type', null=True)
    phone = models.CharField(max_length=11, verbose_name='Phone number')
    price = models.IntegerField(verbose_name='Price', null=True)
    client_in = models.ManyToManyField('Client', through='Booking', verbose_name='Client', null=True)
    floor = models.IntegerField(verbose_name='Floor', null=True)

    def __str__(self):
        return f"{self.number}"


class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name='Room')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    check_in = models.DateField(verbose_name='Check-in')
    check_out = models.DateField(verbose_name='Check-out')


class Client(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    passport = models.CharField(max_length=11, verbose_name='Passport')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    town = models.CharField(max_length=50, verbose_name='Hometown')
    date = models.DateField(verbose_name='Check-in date')
    number = models.IntegerField(verbose_name='Hotel number')
    room_booked = models.ManyToManyField('Room', through='Booking', verbose_name='Room', null=True)
    REQUIRED_FIELDS = ['last_name', 'first_name', 'patronymic',
                       'passport', 'town', 'date', 'number']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Employee(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    floor = models.IntegerField(verbose_name='Floor')
    day = models.CharField(max_length=10, verbose_name='Weekday')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

* serializers.py

```
from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class RoomRetrieveSerializer(serializers.ModelSerializer):
    client_room = ClientSerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"


class ClientRetrieveSerializer(serializers.ModelSerializer):
    room_client = RoomSerializer(many=True)

    class Meta:
        model = Client
        fields = "__all__"
```

* urls.py

```
from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
    path('clients/', ClientListAPIView.as_view()),
    path('clients/create/', ClientCreateAPIView.as_view()),
    path('clients/<int:pk>/', ClientRetrieveAPIView.as_view()),
    path('clients/update/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view()),
    path('employees/', EmployeeListAPIView.as_view()),
    path('employees/create/', EmployeeCreateAPIView.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveAPIView.as_view()),
    path('employees/update/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('bookings/', BookingListAPIView.as_view()),
    path('bookings/create/', BookingCreateAPIView.as_view()),
]
```

* view.py

```
from .serializers import *
from rest_framework.generics import *


class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveAPIView(RetrieveAPIView):
    serializer_class = RoomRetrieveSerializer
    queryset = Room.objects.all()


class ClientListAPIView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientCreateAPIView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientRetrieveAPIView(RetrieveAPIView):
    serializer_class = ClientRetrieveSerializer
    queryset = Client.objects.all()


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class BookingListAPIView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
```

* apps.py

```
from django.apps import AppConfig


class HotelAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hotel_app'
```
