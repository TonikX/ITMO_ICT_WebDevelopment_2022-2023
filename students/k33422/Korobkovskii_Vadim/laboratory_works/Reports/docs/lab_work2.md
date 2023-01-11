# Лабораторная работа №2

## Задание
`Список отелей. Необходимо реализовать следующий функционал:`

  1. Регистрация новых пользователей.


  2. Просмотр и резервирование номеров. Пользователь должен иметь
  возможность редактирования и удаления своих резервирований.
 

  3. Написание отзывов к номерам. При добавлении комментариев, должны
  сохраняться период проживания, текст комментария, рейтинг (1-10),
  информация о комментаторе.


  4. Администратор должен иметь возможность заселить пользователя в отель и
  выселить из отеля средствами Django-admin.


  5. В клиентской части должна формироваться таблица, отображающая
  постояльцев отеля за последний месяц.

## Реализация 

* `Файл с моделями (базами данных) models.py`
``` python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import *
from .models import *
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from datetime import datetime


class User(AbstractUser):
    username = models.CharField("Имя пользователя/Username", max_length=30, unique=True)
    password = models.CharField("Пароль/Password", max_length=30)
    surname = models.CharField("Фамилия/Surname", max_length=30, null=False, blank=True)
    name = models.CharField("Имя/Name", max_length=30, null=False, blank=False)
    phone_number = models.CharField("Номер телефона/Phone number", max_length=15, null=True, blank=True)
    passport = models.CharField("Серия и номер пасспорта/Passport number", max_length=20, null=False, blank=False)
    email = models.EmailField("Электронная почта/Email address", unique=True)
    birthday_date = models.DateField("Дата рождения/Birthday date", null=True, blank=True)

    def __str__(self):
        if self.is_superuser:
            return f'{self.username} (superuser)'
        return f"{self.surname} {self.name}"


class Hotel(models.Model):
    hotel_name = models.CharField("Название отеля/Hotel name", max_length=100)
    address = models.CharField("Адресс/Address", max_length=255)
    rating = models.IntegerField("Рейтинг/Rating", validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner_surname = models.CharField("Фамилия владельца/Owner's surname", max_length=30, null=False, blank=True)
    owner_name = models.CharField("Имя владельца/Owner's name", max_length=30, null=False, blank=False)
    description = models.TextField("Описание/Description", max_length=1000, blank=True)

    def __str__(self):
        return f"{self.hotel_name}, {self.rating} star hotel"


class Room(models.Model):
    TYPES = [
        ("S", "Стандартный номер/Standard"),
        ("S+", "Улучшенный номер/Superior"),
        ("Su", "Номер с улучшенной планировкой/Suite"),
        ("F", "Семейный номер/Family room"),
        ("St", "Студия/Studio"),
        ("D", "Делюкс/Deluxe"),
        ("HR", "Номер для молодожёнов/Honeymoon room"),
        ("HS", 'Номер люкс для молодожёнов/Honeymoon suite'),
        ("Dpl", "Двухэтажный номер/Duplex"),
        ("BR", "Номер с балконом/Balcony room"),
        ("PA", "Номер с выходом к бассейну/Pool access room"),
        ("B+", "Номер бизнес-класса/Business room"),
        ("P", "Президентский номер/President"),
        ("CR", "Угловой номер/Corner room"),
        ("A", "Аппартаменты/Apartments")

    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель/Hotel")
    number = models.IntegerField("Номер комнаты/Room number", null=False, blank=False)
    floor = models.IntegerField("Этаж/Floor", validators=[MinValueValidator(1)])
    type = models.CharField(max_length=5, choices=TYPES, null=False, blank=False)
    persons = models.IntegerField("Количество кроватей/Number of beds", validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField("Стоимость за одну ночь/Price for one night", null=False, blank=False)
    description = models.TextField("Описание номера/Room description", max_length=1000, null=False, blank=True)

    class Meta:
        unique_together = ("hotel", "number")

    def __str__(self):
        return f"Hotel {self.hotel.hotel_name}, room №{self.number} ({self.floor} floor)"


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Номер комнаты/Room number")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Гость/Guest")
    check_in = models.DateField("Дата заселения/Check-in date", null=False, blank=False)
    check_out = models.DateField("Дата выселения/Check-out date", null=False, blank=False)
    price = models.PositiveIntegerField("Полная стоимость проживания/Full accommodation cost", null=False, blank=False)
    checked_in = models.BooleanField(default=False)

    @property
    def accommodation_duration(self):
        difference = (self.check_out - self.check_in)
        return difference.days

    def date_check(self):
        if self.check_out < self.check_in:
            raise ValidationError("Дата выселения должна быть больше даты заселения/Check-out date must be greater than"
                                  "check-in date")

    def save(self, *args, **kwargs):
        self.price = self.room.price * self.accommodation_duration
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.room.hotel.hotel_name}, room №{self.room.number} | {self.check_in} — {self.check_out}"


class Review(models.Model):
    RATINGS = [
        ("1", "Ужасно/Awful"),
        ("2", "Плохо/Bad"),
        ("3", "Удовлетворительно/Okay"),
        ("4", "Хорошо/Good"),
        ("5", "Отлично/Great")
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    check_in_date = models.DateField("Дата заселения/Check-in date")
    check_out_date = models.DateField("Дата выселения/Check-out date")
    review = models.TextField("Отзыв/Review", max_length=5000, null=False, blank=False)
    rating = models.CharField("Оцените ваше нахождение в отеле/Rate your stay at the hotel", choices=RATINGS,
                                 max_length=1)

    def save(self, *args, **kwargs):
        self.check_in_date = self.reservation.check_in
        self.check_out_date = self.reservation.check_out
        super(Review, self).save(*args, **kwargs)
```

* `Файл с представлениями views.py` 
``` python
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


class Homepage(TemplateView):
    template_name = 'index.html'


def register(request):
    if request.user.is_authenticated:
        return redirect('/main_page/')
    else:
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()

                return redirect('login')

        data = {'form': form}
        return render(request, 'register.html', data)


def login_(request):
    if request.user.is_authenticated:
        return redirect('/main_page/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/main_page/')

        data = {}
        return render(request, 'login.html', data)


def logout_(request):
    logout(request)
    return redirect('login')


class IndexView(TemplateView):
    template_name = "index1.html"


class HotelRetrieveView(DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'


class ListReservation(ListView):
    model = Reservation
    template_name = 'reservation.html'
    all_reservations = Reservation.objects
    paginate_by = 10


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_create.html'


def create_reservation(request):
    data = {}
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, "reservation_create.html", data)


class ReservationRetrieveView(DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_update.html'


class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'


class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects
    paginate_by = 10


class GuestsList(ListView):
    model = Reservation
    template_name = 'guests.html'
    all_guests = Reservation.objects
    paginate_by = 10


class ListRoom(ListView):
    model = Room
    template_name = "room_list.html"
    all_rooms = Room.objects
    paginate_by = 10


class RoomRetrieveView(DetailView):
    model = Room
    template_name = "room_detail.html"


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review_create.html"


class ReviewList(ListView):
    model = Review
    template_name = "review.html"
    all_review = Review.objects
    paginate_by = 10


class ReviewRetrieveView(DetailView):
    model = Review
    template_name = "review_detail.html"
```

* `Файл с формами forms.py`
``` python
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest', 'room', 'check_in', 'check_out']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'phone_number', 'passport', 'email', 'birthday_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reservation', 'review', 'rating']
```

* `Файл со ссылками urls.py`
``` python
from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view()),
    path('register/', register, name='register'),
    path('login/', login_, name='login'),
    path('logout/', logout_, name='logout'),

    path('main_page/', IndexView.as_view(), name='main_page'),
    path('hotels/', HotelList.as_view(), name='hotel_list'),
    path('hotels/<str:pk>', HotelRetrieveView.as_view()),

    path('reservations/', ListReservation.as_view(), name='my_reservation'),
    path('reservations/create/', ReservationCreateView.as_view(success_url='/reservations/'), name='reservation'),
    #path('reservations/create/', create_reservation, name='reservation'),
    path('reservations/<str:pk>', ReservationRetrieveView.as_view()),
    path('reservations/<str:pk>/update/', ReservationUpdateView.as_view(success_url='/reservations/')),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(success_url='/reservations/')),

    path('rooms/', ListRoom.as_view(), name='room_list'),
    path('rooms/<str:pk>', RoomRetrieveView.as_view()),

    path('reviews/', ReviewList.as_view(), name='review'),
    path('reviews/create/', ReviewCreateView.as_view(success_url='/reviews/'), name='review_create'),
    path('reviews/<str:pk>', ReviewRetrieveView.as_view()),

    path('guests/', GuestsList.as_view(), name='guests'),
    ]
```
