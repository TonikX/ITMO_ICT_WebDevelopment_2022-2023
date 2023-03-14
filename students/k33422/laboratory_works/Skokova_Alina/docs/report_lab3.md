# Лабораторная работа № 3. Реализация серверной части приложения средствами Django и DjangoRestFramework

## Вариант 1. Создать программную систему, предназначенную для администратора гостиницы

Cистема должна обеспечивать хранение сведений об имеющихся в гостинице номерах, о проживающих в гостинице клиентах и о служащих, убирающихся в номерах. Количество номеров в гостинице известно, и имеются номера трех типов: одноместный, двухместный и трехместный, отличающиеся стоимостью проживания в сутки. В каждом номере есть телефон.

О каждом проживающем должна храниться следующая информация: номер паспорта, фамилия, имя, отчество, город, из которого он прибыл, дата поселения в гостинице, выделенный гостиничный номер.

О служащих гостиницы должна быть известна информация следующего содержания: фамилия, имя, отчество, где (этаж) и когда (день недели) он убирает. Служащий гостиницы убирает все номера на одном этаже в определенные дни недели, при этом в
разные дни он может убирать разные этажи.

Работа с системой предполагает получение следующей информации:

- о клиентах, проживавших в заданном номере, в заданный период времени;
- о количестве клиентов, прибывших из заданного города,
- о том, кто из служащих убирал номер указанного клиента в заданный день недели,
- сколько в гостинице свободных номеров;
- список клиентов с указанием места жительства, которые проживали в те же дни, что и заданный клиент, в определенный период времени.

Администратор должен иметь возможность выполнить следующие операции:

- принять на работу или уволить служащего гостиницы;
- изменить расписание работы служащего;
- поселить или выселить клиента.

Необходимо предусмотреть также возможность автоматической выдачи отчета о работе гостиницы за указанный квартал текущего года. Такой отчет должен содержать следующие сведения:

- число клиентов за указанный период в каждом номере;
- количество номеров не каждом этаже;
- общая сумма дохода за каждый номер;
- суммарный доход по всей гостинице.

## Файловая архитектура проекта

- `models.py`:

```python
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
```

- `views.py`:

```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *


class BookingRoomDatesListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        id_room = self.kwargs['id_room']
        room_chosen = Room.objects.get(id_room=id_room)
        date_start = self.kwargs['date_start']
        date_end = self.kwargs['date_end']
        queryset = Booking.objects.filter(
            id_room=room_chosen, date_start__range=[date_start, date_end]) | Booking.objects.filter(
            id_room=room_chosen, date_end__range=[date_start, date_end]) | Booking.objects.filter(
            id_room=room_chosen, date_start__lte=date_start, date_end__gte=date_end) | Booking.objects.filter(
            id_room=room_chosen, date_start__lte=date_start, date_end__isnull=True)
        return queryset
    
class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        queryset = Client.objects.filter(city=city)
        return queryset

class CleanerGetAPIView(generics.ListAPIView):
    serializer_class = ScheduleAndCleanerSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        id_room = self.kwargs['id_room']
        room_chosen = Room.objects.get(id_room=id_room)
        queryset = Schedule.objects.filter(day=day, id_floor=room_chosen.id_floor)
        return queryset

class RoomVacantListAPIView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        booked_ids = []
        for i in Booking.objects.filter(date_end__isnull=True):
            booked_ids.append(i.id_room.id_room)
        return Room.objects.exclude(id_room__in=booked_ids)

class BookingAndClientListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        passport = self.kwargs['passport']
        client_chosen = Client.objects.get(passport=passport)
        return Booking.objects.filter(id_client=client_chosen)

class BookingDatesListAPIView(generics.ListAPIView):
    serializer_class = BookingAndClientSerializer

    def get_queryset(self):
        date_start = self.kwargs['date_start']
        date_end = self.kwargs['date_end']
        queryset = Booking.objects.filter(
            date_start__range=[date_start, date_end]) | Booking.objects.filter(
            date_end__range=[date_start, date_end]) | Booking.objects.filter(
            date_start__lte=date_start, date_end__gte=date_end) | Booking.objects.filter(
            date_start__lte=date_start, date_end__isnull=True)
        return queryset

class CleanerCreateView(generics.CreateAPIView):
    serializer_class = CleanerCreateSerializer
    queryset = Cleaner.objects.all()

class CleanerDeleteView(generics.RetrieveDestroyAPIView):
    serializer_class = CleanerSerializer
    queryset = Cleaner.objects.all()

class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingCreateSerializer
    queryset = Booking.objects.all()

class BookingUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = Schedule.objects.all()

class ScheduleGetView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleAndCleanerSerializer
    queryset = Schedule.objects.all()

class CleanerAndScheduleListAPIView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        id_cleaner = self.kwargs['id_cleaner']
        cleaner_chosen = Cleaner.objects.get(id_cleaner=id_cleaner)
        return Schedule.objects.filter(id_cleaner=cleaner_chosen)

class RoomsPerFloor(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        id_floor = self.kwargs['id_floor']
        floor_chosen = Floor.objects.get(id_floor=id_floor)
        return Room.objects.filter(id_floor=floor_chosen)
```

- `serializers.py`:

```python
from rest_framework import serializers
from .models import *

class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):

    room_type = PriceSerializer()

    class Meta:
        model = Room
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"

class BookingAndClientSerializer(serializers.ModelSerializer):

    id_client = ClientSerializer()
    id_room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"

class CleanerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaner
        fields = "__all__"

class ScheduleAndCleanerSerializer(serializers.ModelSerializer):

    id_cleaner = CleanerSerializer()

    day = serializers.CharField(source="get_day_display", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"

class CleanerCreateSerializer(serializers.Serializer):
    last_name_cleaner = serializers.CharField(max_length=120)
    first_name_cleaner = serializers.CharField(max_length=120)
    patronymic_cleaner = serializers.CharField(max_length=120)

    def create(self, validated_data):
        cleaner = Cleaner(**validated_data)
        cleaner.save()
        return Cleaner(**validated_data)

class BookingCreateSerializer(serializers.Serializer):
    id_client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='passport')
    id_room = serializers.SlugRelatedField(queryset=Room.objects.all(), slug_field='id_room')
    date_start = serializers.DateField()
    date_end = serializers.DateField()

    def create(self, validated_data):
        booking = Booking(**validated_data)
        booking.save()
        return Booking(**validated_data)

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

class ScheduleCreateSerializer(serializers.Serializer):
    id_cleaner = serializers.SlugRelatedField(queryset=Cleaner.objects.all(), slug_field='id_cleaner')
    id_floor = serializers.SlugRelatedField(queryset=Floor.objects.all(), slug_field='id_floor')
    day = serializers.CharField(max_length=3)

    def create(self, validated_data):
        schedule = Schedule(**validated_data)
        schedule.save()
        return Schedule(**validated_data)

class ScheduleSerializer(serializers.ModelSerializer):

    day = serializers.CharField(source="get_day_display", read_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
```

- `urls.py`:

```python
from django.urls import path
from .views import *


app_name = "hotel_app"


urlpatterns = [
    path('clients/<id_room>/<date_start>/<date_end>', BookingRoomDatesListAPIView.as_view()),
    path('clients/<city>', ClientListAPIView.as_view()),
    path('client/<passport>', BookingAndClientListAPIView.as_view()),
    path('cleaner/<id_room>/<day>', CleanerGetAPIView.as_view()),
    path('vacant/', RoomVacantListAPIView.as_view()),
    path('clients/<date_start>/<date_end>', BookingDatesListAPIView.as_view()),
    path('cleaner-create/', CleanerCreateView.as_view()),
    path('cleaner-delete/<pk>', CleanerDeleteView.as_view()),
    path('booking-update/<pk>', BookingUpdateView.as_view()),
    path('booking-create/', BookingCreateView.as_view()),
    path('schedule-create/', ScheduleCreateView.as_view()),
    path('schedule-update/<pk>', ScheduleGetView.as_view()),
    path('schedule/<id_cleaner>', CleanerAndScheduleListAPIView.as_view()),
    path('floor/<id_floor>', RoomsPerFloor.as_view()),
]
```