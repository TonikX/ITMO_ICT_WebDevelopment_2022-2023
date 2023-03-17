# Лабораторная работа 2

## Структура проекта

- `laboratory_work_2` - основная директория проекта
- `avia` - приложение
- `avia/templates` - директория с templates

## Настройки

- `laboratory_work_2/settings.py`  

_Настройки авторизации_

```python
AUTH_USER_MODEL = "avia.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

_Установленные приложения_

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "avia",
]
```

- `avia/urls.py`  

_Эндпоинты приложения 

```python
urlpatterns = [
    path('', flights, name="flights_url"),
    path('flight/<str:slug>/', get_flight, name="get_flight_url"),
    path('flight/<str:slug>/passengers', get_passengers, name="get_passengers_url"),
    path('book', book, name="book_url"),
    path('reviews', get_reviews, name="get_reviews_url"),
    path('register', register, name="register_url"),
    path('login', login_req, name="login_url"),
    path('logout', logout_req, name="logout_url"),
    path('bookings', get_bookings, name="get_bookings_url"),
    path('bookings/<int:slug>', get_certain_book, name="get_certain_book_url"),
    path('bookings/<int:slug>/delete', delete_certain_book, name='delete_certain_book_url'),
    path('bookings/<int:slug>/review', send_review, name='send_review_url')
]

```

## Приложение

- Исходный код форм `forms.py`

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'passport', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'passport': forms.NumberInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    username.widget.attrs.update({'class': 'form-input'})
    password.widget.attrs.update({'class': 'form-input'})

    class Meta:
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class ReviewForm(forms.Form):
    RATE_CHOICES = [i for i in Comment.rate_choices]
    text = forms.CharField()
    rating = forms.MultipleChoiceField(choices=RATE_CHOICES)
    rating.widget.attrs.update({'class': 'form-input'})
    text.widget.attrs.update({'class': 'form-input'})

```


- Исходный код моделей `models.py`
 
```python
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    passport = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Plane(models.Model):
    plane_name = models.CharField(max_length=30)
    seats_count = models.IntegerField(max_length=525)

    def __str__(self):
        return self.plane_name


class Flight(models.Model):
    flight_type = [("Arrival", "Arrival"),
                   ("Departure", "Departure")]
    gate_number = [(f"A0{i}", f"A0{i}") for i in range(0, 10)]
    city_choices = [("Moscow", "Moscow"),
                    ("Saint-Petersburg", "Saint-Petersburg"),
                    ("Kaliningrad", "Kaliningrad"),
                    ("Sochi", "Sochi"),
                    ("Nalchik", "Nalchik"),
                    ("Grozny", "Grozny"),
                    ("Mahachkala", "Mahachkala"),
                    ("Krasnodar", "Krasnodar"),
                    ("Anapa", "Anapa")]
    flight_number = models.CharField(max_length=10, unique=True)
    gate_number = models.CharField(max_length=3, choices=gate_number)
    out_place = models.CharField(max_length=20, choices=city_choices)
    arrival_place = models.CharField(max_length=20, choices=city_choices)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    airline = models.CharField(max_length=50)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    type_of_flight = models.CharField(max_length=9, choices=flight_type)

    def get_seats(self):
        if self.ticket_set.count() != 0:
            occ_seats = list(map(int, self.ticket_set.values_list("seat")[0]))
            available_seats = [i for i in range(1, self.plane.seats_count+1) if i not in occ_seats]
            return available_seats
        else:
            return range(1, self.plane.seats_count +1)

    def get_absolute_url(self):
        return reverse('get_flight_url', kwargs={'slug': self.flight_number})

    def get_passengers_url(self):
        return reverse('get_passengers_url', kwargs={'slug': self.flight_number})

    def is_done(self):
        print(self.arrival_date.date() <= datetime.date.today())
        return self.arrival_date.date() <= datetime.date.today()

    def __str__(self):
        return self.flight_number


class Ticket(models.Model):
    ticket_number = models.IntegerField(max_length=30)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('get_certain_book_url', kwargs={'slug': self.ticket_number})

    def __str__(self):
        return "{}".format(self.ticket_number)


class Comment(models.Model):
    comment_number = models.IntegerField()
    rate_choices = [(1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10)]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rate_choices)

    def __str__(self):
        return "{}".format(self.comment_number)

```
-Код view view.py

```python
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegisterUserForm, LoginForm, ReviewForm
from .models import *


# Create your views here.

def flights(request):
    flights_list = Flight.objects.all()

    if request.method == "GET":
        return render(request, "avia/index.html", context={"flights": flights_list})


def get_flight(request, slug):
    flight = Flight.objects.get(flight_number__exact=slug)

    if request.method == "GET":
        return render(request, "avia/certain_flight.html", context={"flight": flight})


def book(request):
    flight = Flight.objects.get(flight_number__exact=request.POST['flight_number'])
    next_page = request.POST['next']
    seat = request.POST['seat']
    passenger = User.objects.get(id__exact=request.user.id)
    try:
        ticket = Ticket.objects.get(flight_number__exact=flight, passenger_id__exact=passenger.id)
        ticket.seat = seat
        ticket.save()
    except Ticket.DoesNotExist:
        print("Doesnt exist")
        Ticket.objects.create(ticket_number=random.randint(100000, 999999),
                              flight_number=flight,
                              passenger=passenger,
                              seat=seat
                              )

    return redirect(next_page)


def get_passengers(request, slug):
    tickets = Flight.objects.get(flight_number__exact=slug).ticket_set.get_queryset()

    return render(request, "avia/passengers_list.html", context={"tickets": tickets, "flight_n": slug})


def get_reviews(request):
    reviews = Comment.objects.all()

    return render(request, 'avia/reviews.html', context={'reviews': reviews})


def register(request):
    if request.method == "GET":
        register_form = RegisterUserForm()
        print(register_form)
        return render(request, 'avia/registration.html', context={'form': register_form})

    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect("flights_url")


def login_req(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'avia/login.html', context={'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('flights_url')
            else:
                return render(request, 'avia/login.html', {'form': form,
                                                           'err': 'Incorrect username/password'})
        else:
            return render(request, 'avia/login.html', {'form': form})


def logout_req(request):
    logout(request)
    return redirect('flights_url')


def get_bookings(request):
    tickets = Ticket.objects.filter(passenger_id__exact=request.user.id)

    return render(request, 'avia/bookings.html', context={'tickets': tickets})


def get_certain_book(request, slug):
    ticket = Ticket.objects.get(ticket_number__exact=slug)
    flight = Flight.objects.get(flight_number__exact=ticket.flight_number)
    passenger = User.objects.get(id__exact=request.user.id)

    return render(request, 'avia/get_certain_book.html', context={'ticket': ticket,
                                                                  'flight': flight,
                                                                  'passenger': passenger})


def delete_certain_book(request, slug):
    ticket = Ticket.objects.get(ticket_number__exact=slug)
    ticket.delete()

    return get_bookings(request)


def send_review(request, slug):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'avia/review.html', context={'form': form})

    if request.method == "POST":
        form = ReviewForm(request.POST)
        rate = request.POST['rating']
        text = request.POST['text']

        if form.is_valid():
            ticket = Ticket.objects.get(ticket_number__exact=slug)
            flight = ticket.flight_number
            passenger = User.objects.get(id__exact=request.user.id)
            Comment.objects.create(comment_number=random.randint(10000, 99999),
                                   author=passenger,
                                   flight=flight,
                                   rating=rate,
                                   text=text
                                   )

            return redirect('get_reviews_url')

        else:
            return render(request, 'avia/reviews.html', context={'form': form})
```
