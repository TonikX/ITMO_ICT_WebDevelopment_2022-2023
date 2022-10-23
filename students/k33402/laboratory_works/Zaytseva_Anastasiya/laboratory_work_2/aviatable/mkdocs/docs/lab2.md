# Лабораторная работа №2

## Видеоматериалы
1. [Практическая работа №2](https://github.com/chiclassie/ITMO_ICT_WebDevelopment_2022-2023/blob/main/students/k33402/laboratory_works/Zaytseva_Anastasiya/laboratory_work_2/videos/pl2.mp4)
2. [Лабораторная работа №2 (демонстрация работы)](https://github.com/chiclassie/ITMO_ICT_WebDevelopment_2022-2023/blob/main/students/k33402/laboratory_works/Zaytseva_Anastasiya/laboratory_work_2/videos/lr2demo.mp4)
3. [Практическая работа №2 (исходный код)](https://github.com/chiclassie/ITMO_ICT_WebDevelopment_2022-2023/blob/main/students/k33402/laboratory_works/Zaytseva_Anastasiya/laboratory_work_2/videos/lr2code.mp4)

## Основные файлы исходного кода

* `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators  import MaxValueValidator, MinValueValidator

class Passenger(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    passport_number = models.CharField(max_length=15,unique=True)

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Airline(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Flight(models.Model):
    TYPE_CHOICES = [
        ('IN', 'Arrival'),
        ('OUT', 'Departure'),
    ]
    passengers = models.ManyToManyField(Passenger, through='Ticket', related_name='passenger')
    reviewers = models.ManyToManyField(Passenger, through='Review', related_name='reviewer')
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
    flight_number = models.CharField(max_length=6,unique=True)
    hotel = models.CharField(max_length=30, null=True, blank=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    gate_number = models.CharField(max_length=3)

    def __str__(self):
        return self.flight_number

class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    ticket_number = models.CharField(max_length=10,unique=True)
    seat = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.ticket_number

class Review(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(limit_value=10),
            MinValueValidator(limit_value=1)
        ]
    )

```

* `forms.py`
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Passenger

class NewUserForm(UserCreationForm):
	class Meta:
		model = Passenger
		fields = ('username', 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'passport_number')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
```

* `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('auth', views.auth),
    path('logout', views.logout_view),
    path('signup', views.register_request),
    path('table', views.FlightList.as_view()),
    path('flight/<int:flight_id>/order', views.order),
    path('flight/<str:flight_number>/review/create', views.review),
    path('flight/<str:flight_number>/review', views.reviews),
    path('flight/<str:flight_number>/passenger', views.passengers),
    path('ticket', views.tickets),
    path('ticket/<int:pk>/delete', views.TicketDelete.as_view()),
    path('ticket/<int:pk>/update', views.TicketUpdate.as_view()),
]
```

* `views.py`
```python
from table.models import Passenger, Flight, Ticket, Review
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import NewUserForm
import random
import string

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'auth.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth.html', {'error':'Неверный логин или пароль'})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = NewUserForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})

def tickets(request):
    tickets = Ticket.objects.filter(passenger=request.user.id)
    return render(request, 'tickets.html', {'tickets':tickets})

def order(request, flight_id):
    if request.method == "POST":
        fl = Flight.objects.get(flight_number=request.POST['flight'])
        try:
            tick = Ticket.objects.get(flight=fl.id,seat=request.POST['seat'])
        except Ticket.DoesNotExist:
            ticket = Ticket(
                passenger=Passenger.objects.get(username=request.user.username),
                flight=fl,
                seat=request.POST['seat'],
                ticket_number=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)),
            )
            ticket.save()
            return redirect('/ticket')
        return render(request, 'order.html', {'error': 'Выбранное место занято', 'flight': fl})

    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    return render(request, 'order.html', {'flight': flight})


def review(request, flight_number):
    if request.method == "POST":
        fl = Flight.objects.get(flight_number=request.POST['flight'])
        try:
            rev = Review.objects.get(flight=fl.id,passenger=request.user.id)
        except Review.DoesNotExist:
            revNew = Review(
                passenger=Passenger.objects.get(username=request.user.username),
                flight=fl,
                text=request.POST['text'],
                rating=request.POST['rating'],
            )
            revNew.save()
            return redirect('/ticket')
        return render(request, 'review.html', {'error': 'Вы уже оставляли отзыв на данный рейс.', 'flight': fl})

    try:
        flight = Flight.objects.get(flight_number=flight_number)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")

    try:
        rev = Review.objects.get(flight=flight.id,passenger=request.user.id)
    except Review.DoesNotExist:
        return render(request, 'review.html', {'flight': flight})

    return render(request, 'review.html', {'error': 'Вы уже оставляли отзыв на данный рейс.', 'flight': flight})

def reviews(request, flight_number):
    flight = Flight.objects.get(flight_number=flight_number)
    reviews = Review.objects.filter(flight=flight.id)
    return render(request, 'reviews.html', {'reviews': reviews, 'flight': flight})

def passengers(request, flight_number):
    if request.user.username != 'admin':
        raise Http403("Ошибка доступа")

    flight = Flight.objects.get(flight_number=flight_number)
    tickets = Ticket.objects.filter(flight=flight.id)
    passengers = Passenger.objects.filter(id__in=[t.passenger.id for t in tickets])
    return render(request, 'passengers.html', {'passengers': passengers, 'flight': flight})

class FlightList(ListView):
    model = Flight
    template_name = 'table.html'

class TicketDelete(DeleteView):
   model = Ticket
   template_name = 'ticket_delete.html'
   success_url = '/ticket'

class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['seat']
    success_url = '/ticket'
    template_name = 'ticket_update.html'

```