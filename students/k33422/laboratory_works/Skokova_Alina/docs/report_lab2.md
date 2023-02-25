# Лабораторная работа № 2. Реализация простого сайта средствами Django

## Вариант 3. Табло отображения информации об авиаперелетах

Необходимо реализовать следующий функционал:

- Регистрация новых пользователей.
- Просмотр и резервирование мест на рейсах. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
- Администратор должен иметь возможность зарегистрировать на рейс пассажира и вписать в систему номер его билета средствами Django-admin.
- В клиентской части должна формироваться таблица, отображающая всех пассажиров рейса.
- Написание отзывов к рейсам. При добавлении комментариев, должны сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о комментаторе.

## Файловая архитектура проекта

- Модели `models.py`:

```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Flight(models.Model):
    id_flight = models.CharField(primary_key=True, max_length=30)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField(blank=False)
    airline = models.CharField(max_length=50)
    COMFORT_CHOICES = [
        ("E", "Economy"),
        ("B", "Business"),
        ("F", "First"),
    ]
    comfort = models.CharField(max_length=2, choices=COMFORT_CHOICES)
    seat_number = models.IntegerField(blank=False)

    def __str__(self):
        return self.id_flight


class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    passport = models.ForeignKey(User, on_delete=models.CASCADE)
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    LUGGAGE_CHOICES = [
        ("Y", "YES"),
        ("N", "NO"),
    ]
    luggage = models.CharField(max_length=2, choices=LUGGAGE_CHOICES)
    APPROVED_CHOICES = [
        ("Y", "YES"),
        ("N", "NO"),
    ]
    approved = models.CharField(max_length=2, choices=APPROVED_CHOICES, default="N")
    ticket_number = models.CharField(max_length=30, blank=True)


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id_flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    date_reviewed = models.DateTimeField(default=timezone.now)
    RATING_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ]
    rating = models.CharField(max_length=2, choices=RATING_CHOICES)
```

- Представления `views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.contrib import messages


class UserRegister(CreateView):
    form_class = UserRegisterForm
    success_url = "/login"
    template_name = 'flights/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'flights/login.html'

    def get_success_url(self):
        return "/"


def logout_user(request):
    logout(request)
    return redirect('/login')


class FlightsList(ListView):
    template_name = 'flights/list_flights.html'
    queryset = Flight.objects.all()
    paginate_by = 10


@login_required
def book_flight(request, id_flight):
    c = Flight.objects.get(pk=id_flight)
    context = {}

    form = BookingForm(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.passport = request.user
        response.id_flight = c
        form.save()
        messages.success(request, f'Место зарезервировано!')
    context['form'] = form
    context['flight'] = c
    return render(request, "flights/book_flight.html", context)

class BookingsList(ListView):
    model = Booking
    template_name = 'flights/my_bookings.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(BookingsList, self).get_queryset()
        queryset = queryset.filter(passport=self.request.user)
        return queryset


class BookingUpdate(UpdateView):
    model = Booking
    fields = ['luggage']
    success_url = '/my_bookings/'


class BookingDelete(DeleteView):
    model = Booking
    success_url = '/my_bookings/'


class PassengersList(ListView):
    model = Booking
    template_name = 'flights/all_passengers.html'
    paginate_by = 10

    def get_queryset(self):
        return Booking.objects.filter(id_flight=self.kwargs['id_flight'], approved="Y")


class ReviewsList(ListView):
    template_name = 'flights/list_reviews.html'
    queryset = Review.objects.all()
    paginate_by = 10


@login_required
def review_create(request):
    context = {}

    form = ReviewForm(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.author = request.user
        form.save()
        messages.success(request, f'Отзыв добавлен!')
    context['form'] = form
    return render(request, "flights/review_create.html", context)
```

- Перенаправление запросов `urls.py`:

```python
from django.urls import path 
from .views import *
urlpatterns = [
    path('', FlightsList.as_view()),
    path('register/', UserRegister.as_view()),
    path('login/', LoginUser.as_view()),
    path('logout/', logout_user),
    path('book/<id_flight>', book_flight),
    path('my_bookings/', BookingsList.as_view()),
    path('my_bookings/<int:pk>/update/', BookingUpdate.as_view()),
    path('my_bookings/<int:pk>/delete/', BookingDelete.as_view()),
    path('passengers/<id_flight>', PassengersList.as_view()),
    path('reviews', ReviewsList.as_view()),
    path('reviews/create/', review_create),
]
```