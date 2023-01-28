# Лабораторная работа №2

## Вариант 3 "Табло отображения информации об авиаперелетах."

Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе
(прилет, отлет), номере гейта.
Необходимо реализовать следующий функционал:


* Регистрация новых пользователей.
* Просмотр и резервирование мест на рейсах. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.
* Администратор должен иметь возможность зарегистрировать на рейс
пассажира и вписать в систему номер его билета средствами Django-admin.
* В клиентской части должна формироваться таблица, отображающая всех
пассажиров рейса.
* Написание отзывов к рейсам. При добавлении комментариев, должны
сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о
комментаторе.


* `models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    username = models.CharField("Username", max_length=30, null=False, unique=True)
    passport = models.CharField("Passport number", max_length=12, null=False)
    first_name = models.CharField("Name", max_length=30, null=False)
    lastname = models.CharField("Lastname", max_length=30, null=False)
    date_of_birth = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class Flight(models.Model):
    flight_number = models.CharField("Flight number", max_length=20, unique=True)
    airline = models.CharField("Airline name", max_length=30, null=False)
    departure = models.DateTimeField("Departure date and time", null=False)
    arrival = models.DateTimeField("Arrival date and time", null=False)

    def __str__(self):
        return f"{self.airline}: {self.flight_number}"


class Ticket(models.Model):
    TYPE_FLIGHT = [('TO', 'Arrival'),
                   ('FROM', 'Departure')]
    ticket_id = models.CharField("Ticket number", primary_key=True, max_length=20, unique=True)
    seat = models.CharField("Place in plane", max_length=3, null=True)
    gate = models.CharField("Gate number", max_length=3, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    type = models.CharField("Flight type", max_length=30, choices=TYPE_FLIGHT)

    def __str__(self):
        return f"{self.flight} - {self.ticket_id}{self.seat == '' if '' else f'({self.seat})'}"


class Feedback(models.Model):
    comment = models.TextField("Comment", null=False)
    rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(limit_value=10),
                    MinValueValidator(limit_value=1)]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField("Flight date")

    def __str__(self):
        return f"{self.flight}({self.user}) - {self.rate} - \'{self.comment[:10]}\' "
 ```

* `forms.py`

```python
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'lastname', 'first_name', 'date_of_birth', 'passport')


class FeedbackForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=100)
    rating = forms.IntegerField(label='Rating', validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    date = forms.DateField(label='Flight date')


class TicketUpdateForm(forms.Form):
    seat = forms.CharField(label='Seat', max_length=3)


class BookForm(forms.Form):
    type = forms.ChoiceField(choices=(('TO', 'Arrival'),
                                      ('FROM', 'Departure')))
    seat = forms.CharField(label="Seat", max_length=3)
```

* `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('logout', views.logout_view),
    path('register', views.registration),
    path('flights', views.flights),
    path('flight/<int:flight_id>/users', views.users_list),
    path('flight/<int:flight_id>/feedbacks', views.feedbacks),
    path('flight/<int:flight_id>/leave_feedback', views.create_feedback),
    path('tickets', views.tickets),
    path('ticket/<int:ticket_id>/delete', views.delete_ticket),
    path('ticket/<int:ticket_id>/update', views.update_ticket),
    path('flight/<int:flight_id>/book', views.book_flight)
]
```

* `views.py`

```python
import time
from flights_app.forms import *
from flights_app.models import User, Flight, Ticket, Feedback
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'auth.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth.html', {'error': 'Try again'})


def registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = NewUserForm()
    return render(request, "register.html", {"register_form": form})


def tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets.html', {'tickets': user_tickets})


def flights(request):
    return render(request, 'flights.html', {'flights': Flight.objects.all()})


def users_list(request, flight_id):
    user_ids = Ticket.objects.filter(flight_id=flight_id).values('user_id')
    users = User.objects.filter(id__in=user_ids)
    flight = Flight.objects.get(id=flight_id)
    return render(request, "users.html", {
        "users": users,
        "flight": flight,
    })


def feedbacks(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    feedbacks = Feedback.objects.filter(flight_id=flight_id)
    return render(request, "feedbacks.html", {
        "feedbacks": feedbacks,
        "flight": flight,
    })


def create_feedback(request, flight_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(comment=form.cleaned_data.get('comment'),
                                    rate=form.cleaned_data.get('rating'),
                                    date=form.cleaned_data.get('date'),
                                    user_id=request.user.id,
                                    flight_id=flight_id)

            return redirect('/flights')
    else:
        form = FeedbackForm()
    return render(request, 'leave_feedback.html', {'form': form})


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if ticket.user_id == request.user.id:
        ticket.delete()
    return redirect('/tickets')


def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if ticket.user_id != request.user.id:
        return redirect('/')
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST)
        if form.is_valid():
            ticket.seat = form.cleaned_data.get('seat')
            ticket.save()
            return redirect('/tickets')
    else:
        form = TicketUpdateForm()
    return render(request, 'update.html', {'form': form, 'ticket': ticket})


def book_flight(request, flight_id):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Ticket.objects.create(flight_id=flight_id,
                                  type=form.cleaned_data.get('type'),
                                  seat=form.cleaned_data.get('seat'),
                                  user_id=request.user.id,
                                  ticket_id=int(str(time.time_ns())[-7:]))
            return redirect('/tickets')
    else:
        form = BookForm()
    return render(request, 'book.html', {'form': form})
```