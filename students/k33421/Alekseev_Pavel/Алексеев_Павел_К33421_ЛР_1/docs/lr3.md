# Описание 3 лабораторной работы






- `model.py`

```python
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


```
<hr>

# Views

- `views.py`

```python
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import TypeRoom, Client, Room, Employee, Booking
from rest_framework import serializers, generics, status
from rest_framework.response import Response
from .serializers import *
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db.models import Count


class AllClients(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class CreateClient(generics.CreateAPIView, generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UpdateClient(generics.RetrieveUpdateAPIView):
      serializer_class = ClientSerializer
      queryset = Client.objects.all()


class DeleteClient(generics.RetrieveDestroyAPIView):
      serializer_class = ClientSerializer
      queryset = Client.objects.all()

###


class AllWorkers(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = WorkersSerializer
    permission_classes = [IsAuthenticated]


class CreateWorker(generics.CreateAPIView, generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = WorkersSerializer


class EmployeeUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = WorkersSerializer
    queryset = Employee.objects.all()


class EmployeeDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = WorkersSerializer
    queryset = Employee.objects.all()

###

class AllRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class CreateRoom(generics.CreateAPIView, generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomDelete(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

###


class AllBook(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class CreateBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateBook(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()


class DeleteBook(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Booking.objects.all()

###


class AllBookWithInfo(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializerWithInfoAboutRoomAndTypeRoom


class RoomCount(generics.ListAPIView):
    serializer_class = RoomCountSerializer

    def get_queryset(self):
        c = Room.objects.annotate(num_rooms=Count('id_room')).count()
        return [{'count': c}]


class ClientCount(generics.ListAPIView):
    serializer_class = ClientCountSerializer

    def get_queryset(self):
        c = Client.objects.annotate(num_clients=Count('passport')).count()
        queryset = [{'count': c}]
        return queryset




```
<hr>

# Urls

- `urls.py`

```python
from django.urls import path, include, re_path
from .views import *

app_name = "hotel_app"

urlpatterns = [

    path('all_clients/', AllClients.as_view()),
    path('create_client/', CreateClient.as_view()),
    path('client/<int:pk>/update', UpdateClient.as_view()),
    path('client/<int:pk>/delete', DeleteClient.as_view()),

    ###

    path('all_workers/', AllWorkers.as_view()),
    path('create_worker/', CreateWorker.as_view()),
    path('worker/<int:pk>/update', EmployeeUpdate.as_view()),
    path('worker/<int:pk>/delete', EmployeeDestroy.as_view()),

    ###

    path('room/', AllRooms.as_view()),
    path('create_room/', CreateRoom.as_view()),
    path('room/<int:pk>/update', RoomUpdate.as_view()),
    path('room/<int:pk>/delete', RoomUpdate.as_view()),

    ###

    path('all_book/', AllBook.as_view()),
    path('create_book/', CreateBook.as_view()),
    path('book/<int:pk>/update', UpdateBook.as_view()),
    path('book/<int:pk>/delete', DeleteBook.as_view()),

    ###

    path('all_books_with_room/', AllBookWithInfo.as_view()),
    path('count_of_room/', RoomCount.as_view()),
    path('count_of_client/', ClientCount.as_view()),


]

```
<hr>

# Serializers

- `serializers.py`

```python
from rest_framework import serializers

from .models import TypeRoom, Client, Room, Employee, Booking


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class TypeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookSerializerWithInfoAboutRoomAndTypeRoom(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"


class RoomCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['count']

    def get_count(self, obj):
        return obj["count"]


class ClientCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['count']

    def get_count(self, obj):
        return obj["count"]


```

<hr>

## API

Method   | HTTP method | Description
-----------|:-----------:| -------------|
AllClients       |     GET     | Вывод всех клиентов
CreateClient    |    POST     | Создание клиента
UpdateClient      |    PATCH    | Редактирование клиента
DeleteClient      |   DELETE    | Удаление клиента
ALlWorkers    |     GET     | Вывод всех работников
CreateWorker      |    POST     | Создание работника
EmployeeUpdate     |    PATCH    | Редактирование работника
EmployeeDelete    |   DELETE    | Удаление работника
Allrooms      |     GET     | Вывод всех комнат
CreateRoom      |    POST     | Создание новой комнаты
RoomUpdate    |    PATCH    | Редактировать комнату
RoomDelete      |   DELETE    | Удалить комнату
AllBook      |     GET     | Вывод всех бронирований
CreateBook      |    POST     | Создание бронирования
UpdateBook    |   UPDATE    | Редатирование брони
DeleteBook      |   DELETE    | Удаление брони
AllBookWithInfo      |     GET     | Информация о комнатах с их типом 
RoomCount      |     GET     | Кол-во комнат в отеле
ClientCount    |     GET     | Кол-во поситтителей на данный момент
