# Лабораторная работа №2

## Описание

>Вариант 3: Табло отображения информации об авиаперелетах

Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе
(прилет, отлет), номере гейта.

Необходимо реализовать следующий функционал:

- Регистрация новых пользователей.
- Просмотр и резервирование мест на рейсах. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.
- Администратор должен иметь возможность зарегистрировать на рейс
пассажира и вписать в систему номер его билета средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая всех
пассажиров рейса.
- Написание отзывов к рейсам. При добавлении комментариев, должны
сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о
комментаторе.

<hr>

##Основные файлы проекта

* `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# модель пассажира
class Passenger(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True, blank=True)
    passport = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.passport


# модель авиакомпании
class Airline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# модель рейса
class Flight(models.Model):
    TYPE_CHOICES = [
        ('in', 'Arrival'),
        ('out', 'Departure'),
    ]
    flight_number = models.CharField(max_length=6,unique=True)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    gate_number = models.CharField(max_length=3)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.flight_number


# модель билета
class Ticket(models.Model):
    passport = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)


# модель отзыва
class Comment(models.Model):
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
```

* `views.py`
```python
from django.shortcuts import render, redirect
from .models import Passenger, Flight, Ticket, Comment
from .forms import RegisterForm, CreateBooking, CreateComment
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView


def main_page(request):
    return render(request, 'main.html')


def user_registration(request):
    data = {}
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'registration.html', data)


class FlightList(ListView):
    model = Flight
    template_name = 'flight_list.html'


def create_booking(request):
    data = {}
    form = CreateBooking(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, 'create_booking.html', data)


def my_bookings(request):
    if "passport" in request.POST:
        passport = int(request.POST["passport"])
        return redirect(f'/passenger_bookings/{passport}/')
    else:
        return render(request, 'my_bookings.html')


def passenger_bookings(request, passport):
    passenger = Passenger.objects.get(passport=passport)
    tickets = Ticket.objects.filter(passport=passenger.id)
    return render(request, 'passenger_bookings.html', {'tickets': tickets, 'passenger': passenger})


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['seat']
    success_url = '/bookings'
    template_name = 'ticket_update.html'


class TicketDelete(DeleteView):
    model = Ticket
    success_url = '/bookings'
    template_name = 'ticket_delete.html'


def all_passengers(request, flight_number):
    flight = Flight.objects.get(flight_number=flight_number)
    tickets = Ticket.objects.filter(flight_number=flight.id)
    passengers = Passenger.objects.filter(id__in=[ticket.passport.id for ticket in tickets])

    return render(request, 'all_passengers.html', {'passengers': passengers, 'flight': flight})


def all_comments(request):
    return render(request, 'all_comments.html', {'object_list': Comment.objects.all()})


def create_comment(request):
    data = {}
    form = CreateComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'create_comment.html', data)
```

* `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('registration/', views.user_registration, name='register'),
    path('flight_list/', views.FlightList.as_view(), name='flight_list'),
    path('booking/', views.create_booking, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('passenger_bookings/<int:passport>/', views.passenger_bookings),
    path('bookings/<int:pk>/update', views.TicketUpdate.as_view()),
    path('bookings/<int:pk>/delete', views.TicketDelete.as_view()),
    path('all_passengers/<str:flight_number>', views.all_passengers),
    path('all_comments/', views.all_comments, name='all_comments'),
    path('create_comment/', views.create_comment, name='create_comment'),
]
```


* `forms.py`
```python
from django import forms

from .models import Passenger, Ticket, Comment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            "username", "password", "last_name",
            "first_name", "birth_date", "passport"
        ]


class CreateBooking(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["flight_number", "passport", "seat"]


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["flight_number", "rating", "comment", "passenger"]

```