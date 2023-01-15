# Лабораторная работа №2 - Вариант 1

## Описание работы 

### Список отелей.
Необходимо учитывать название отеля, владельца отеля, адрес, описание, типы
номеров, стоимость, вместимость, удобства.
Необходимо реализовать следующий функционал:

* Регистрация новых пользователей.
*  Просмотр и резервирование номеров. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.
* Написание отзывов к номерам. При добавлении комментариев, должны
сохраняться период проживания, текст комментария, рейтинг (1-10),
информация о комментаторе.
* Администратор должен иметь возможность заселить пользователя в отель и
выселить из отеля средствами Django-admin.
* В клиентской части должна формироваться таблица, отображающая
постояльцев отеля за последний месяц.

-------------------------

## База данных 

![База данных отеля](https://sun9-west.userapi.com/sun9-47/s/v1/ig2/TFiWo23datzQKduhyz0-WHjdalKIosdy4s486VfdcU8fNeiDzHjU-FOuRxbQg9ZYrXV_jPt1-0oiPzqh8vf1WgN8.jpg?size=1183x1028&quality=96&type=album)

-------------------------

## Основные файлы с кодом

* `models.py`
```python
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Q
from datetime import timedelta


class Hotel(models.Model):
    name = models.CharField("Название отеля", primary_key = True, max_length=255)
    address = models.CharField("Адрес", max_length=255)
    stars = models.PositiveSmallIntegerField("Рейтинг", validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner = models.CharField("Владелец отеля", max_length=255)

    def __str__(self):
        return f"{self.stars}-star hotel {self.name}"

class Room(models.Model):
    number_room = models.IntegerField("Номер комнаты", primary_key = True)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, verbose_name = "Отель")
    type_room = models.CharField("Описание комнаты", max_length=100)
    beds = models.PositiveSmallIntegerField("Количество спальных мест", validators=[MinValueValidator(1)])  
    room_price = models.PositiveIntegerField("Стоимость номера")

    class Meta:
        # One hotel can't have two rooms with the same number
        unique_together = ('hotel', 'number_room')

    def __str__(self):
        return f"Room {self.number_room} of hotel {self.hotel.name}"

class Guest(models.Model):
    first_name = models.CharField("Имя", max_length=30, null=False)
    last_name = models.CharField("Фамилия", max_length=30, null=False)
    passport = models.CharField("Номер паспорта", primary_key=True, max_length=30)

    def __str__(self):
        return f"Гость {self.last_name} {self.first_name}"


class Reservation(models.Model):
    order_number = models.AutoField("Номер заказа", primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default = "Ромашка")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE,verbose_name = "Гость") 
    arrival_date = models.DateField("Дата заезда")
    departure_date = models.DateField("Дата выезда")
    price = models.PositiveIntegerField("Стоимость проживания")
    booking_date = models.DateTimeField("Дата бронирования", auto_now_add=True)

    @property
    def duration(self):
        return (self.departure_date - self.arrival_date).days

    def clean(self):
        # Check that start < end
        if self.arrival_date >= self.departure_date:
            raise ValidationError("Duration date must be greater than start date")

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        self.price = self.room.room_price * self.duration
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.pk} in hotel {self.room.hotel.name} from {self.arrival_date} to {self.departure_date}"

class Comment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, verbose_name = "Код бронирования")
    date_start = models.DateField("Дата заезда")
    date_end = models.DateField("Дата выезда")
    text = models.TextField("Комментарий", null=False)
    rate = models.IntegerField("Оценка", default=10,validators=[MaxValueValidator(10), MinValueValidator(1)])
    sing_author = models.CharField("Укажите ваш ник", max_length=30)

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        self.date_start  = self.reservation.arrival_date
        self.date_end = self.reservation.departure_date
        super(Comment, self).save(*args, **kwargs)
```
* `views.py`
```python
from django.shortcuts import render, redirect
from msilib.schema import ListView
from django.http import Http404 
from .models import Hotel, Reservation,Room, Guest, Comment
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import CreateComment, CreateReservation


#для главной страницы
def main_page(request):
    return render(request, 'main_page.html')

#создание нового пользователя
class RegGuests(CreateView):
    model = Guest
    fields = [
        "first_name",
        "last_name",
        "passport",
    ]
    template_name = "register_guests.html"

#просмотр всех номеров
class RoomsList(ListView):
    model = Room
    template_name = 'list_rooms.html'

#бронирование
def create_reservation(request):
    data = {}
    form = CreateReservation(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_reservation.html', data)

#просмотр бронирований пользователя
def user_book(request, guest_passport):
    need_book = Reservation.objects.filter(guest =  guest_passport) 
    current_book = {"object_list": need_book}
    return render(request, 'users_bookings.html', current_book)

#отбор паспорта для просмотра бронирований
def my_bookings(request):
    try:
        passport = int(request.POST.get('passport_user'))
        return redirect(f"/users_bookings/{passport}/")
    except:
        return render(request, "my_bookings.html")

#редактирование брони
class UpdateBooking(UpdateView):
    model = Reservation
    fields = ['room', 'arrival_date', 'departure_date']
    template_name = 'update_book.html'
    success_url = '/my_bookings/'

#удаление брони
class DeleteBooking(DeleteView):
    model = Reservation
    template_name = 'del_book.html'
    success_url = '/my_bookings/'

#написать комментарий
def create_comment(request):
    data = {}
    form = CreateComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_comment.html', data)

#посмотреть все комментарии
def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'all_comments.html', list_comments)

#таблица гостей отеля
def get_hotel(request):
    hotel = request.POST.get('hotel_name')
    if hotel:
        return redirect(f"/guests/{hotel}")
    else:
        return render(request, 'hotel.html')

def guests_list(request, hotel_name):
    guest_in_hotel = Reservation.objects.filter(hotel = hotel_name).values_list('guest')
    nedeed_guests = Guest.objects.filter(passport__in = guest_in_hotel )
    list_of_guests = {
        "object_list": nedeed_guests,
        "hotel_name" : hotel_name}
    return render(request, 'guests.html', list_of_guests)
```
* `urls.py`
```python
from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name = 'main_page'),
    path("registration/", RegGuests.as_view(), name = 'reg'),
    path("rooms/", RoomsList.as_view(),  name = 'rooms'),
    path("book/", create_reservation,  name = 'book'),
    path("my_bookings/", my_bookings, name = 'my_bookings'),
    path("users_bookings/<int:guest_passport>/", user_book),
    path("update_book/<int:pk>", UpdateBooking.as_view()),
    path("del_book/<int:pk>", DeleteBooking.as_view()),
    path("comment/", create_comment, name = 'comment'),
    path('all_comments/', all_comments, name = 'all_comments'),
    path('hotel/', get_hotel, name = 'hotel_info'),
    path('guests/<str:hotel_name>', guests_list)
]
```
* `forms.py`
```python
from django import forms
from .models import Reservation, Comment

class CreateReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room', 'guest', 'arrival_date', 'departure_date']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['reservation', 'text', 'rate', 'sing_author']
```

-------------------------

## Видео работы приложения
[Ссылка на первую часть видео](https://youtu.be/miTz_oHWtLM) 

[Ссылка на вторую часть видео](https://youtu.be/2pQmk4-HOkA)