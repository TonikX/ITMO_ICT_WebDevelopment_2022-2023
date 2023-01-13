# Laboratory work 3
 РЕАЛИЗАЦИЯ СЕРВЕРНОЙ ЧАСТИ ПРИЛОЖЕНИЯ СРЕДСТВАМИ DJANGO И DJANGORESTFRAMEWORK
## Описание работы

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

## Основные файлы с кодом 

* `models.py` - сущности базы данных

```python 
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
```

* `views.py` - основной функционал сайта

```python
from .serializers import *
from rest_framework.generics import *

# просмотр информации о гостиничных номерах
class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

# создание гостиничного номера
class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

# редактирование и удаление гостиничного номера
class RoomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

# просмотр информации определенного гостиничного номера
class RoomRetrieveAPIView(RetrieveAPIView):
    serializer_class = RoomRetrieveSerializer
    queryset = Room.objects.all()


# просмотр информации о постояльцах
class GuestListAPIView(ListAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

# создание постояльца
class GuestCreateAPIView(CreateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

# редактирование и удаление информации о постояльце
class GuestRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

# просмотр информации определенного постояльца
class GuestRetrieveAPIView(RetrieveAPIView):
    serializer_class = GuestRetrieveSerializer
    queryset = Guest.objects.all()


# просмотр информации о сотрудниках, убирающих номера
class CleanersListAPIView(ListAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

# создание сотрудника
class CleanersCreateAPIView(CreateAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

# редактирование и удаление информации о сотруднике
class CleanersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()

# просмотр информации определенного сотрудника
class CleanersRetrieveAPIView(RetrieveAPIView):
    serializer_class = CleanersSerializer
    queryset = Cleaners.objects.all()


# просмотр информации убранного номера
class CleaningListAPIView(ListAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()

# закрепление информации об убранном номере
class CleaningCreateAPIView(CreateAPIView):
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()


# просмотр информации о забронированных номерах
class BookingListAPIView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

# создание брони
class BookingCreateAPIView(CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

# просмотр информации о доступных номерах
class AvailableRoomAPIView(ListAPIView):
    serializer_class = AvailableRoomSerializer

    def get_queryset(self):
        return Room.objects.all().filter(status="+")
```

* `serializers.py` - преобразование данных в нативные типы данных Python

```python 
from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"


class CleanersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaners
        fields = "__all__"


class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class RoomRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class GuestRetrieveSerializer(serializers.ModelSerializer):
    #room_client = RoomSerializer(many=True)

    class Meta:
        model = Guest
        fields = "__all__"


class AvailableRoomSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display", read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'type', 'number', 'phone', 'price']
```

* `urls.py` - связь представлений и url адресов на сайте

```python
from django.urls import path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path('rooms/', RoomListAPIView.as_view()),
    path('rooms/create/', RoomCreateAPIView.as_view()),
    path('rooms/<int:pk>/', RoomRetrieveAPIView.as_view()),
    path('rooms/update/<int:pk>/', RoomRetrieveUpdateDestroyAPIView.as_view()),
    path('guests/', GuestListAPIView.as_view()),
    path('guests/create/', GuestCreateAPIView.as_view()),
    path('guests/<int:pk>/', GuestRetrieveAPIView.as_view()),
    path('guests/update/<int:pk>/', GuestRetrieveUpdateDestroyAPIView.as_view()),
    path('cleaners/', CleanersListAPIView.as_view()),
    path('cleaners/create/', CleanersCreateAPIView.as_view()),
    path('cleaners/<int:pk>/', CleanersRetrieveAPIView.as_view()),
    path('cleaners/update/<int:pk>/', CleanersRetrieveUpdateDestroyAPIView.as_view()),
    path('cleanings/', CleaningListAPIView.as_view()),
    path('cleanings/create/', CleaningCreateAPIView.as_view()),
    path('bookings/', BookingListAPIView.as_view()),
    path('bookings/create/', BookingCreateAPIView.as_view()),
    path('room/status/', AvailableRoomAPIView.as_view()),
]
```