# Лабораторная работа №2

## Задание 
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


* `Файл urls.py`
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('rooms', views.rooms, name='rooms'),
    path('room/<str:pk>', views.room, name='room'),
    path('reservation/<str:pk>', views.reservation, name='reservation'),
    path('profile', views.profile, name='book_list'),
    path('delete_res/<str:pk>', views.delete_reservation, name='delete_reservation'),
    path('edit_res/<str:pk>', views.edit_reservation, name='edit_reservation'),
    path('comment/<str:pk>', views.add_comment, name='add_comment'),
    path('lastmonth', views.show_last_month, name='last_month'),
    path('search_rooms', views.search_rooms, name='search_rooms')
]

```

* `Файл views.py`
``` python
rom django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords dont match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User doesnt exists')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


def rooms(request):
    free_rooms = Room.objects.filter(is_reserved=False)
    p = Paginator(free_rooms, 1)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'rooms.html', {'rooms': page})


def search_rooms(request):
    searched = request.POST['search_value']
    obj = Room.objects.filter(number=searched, is_reserved=False)
    return render(request, 'search_rooms.html', {'room': obj})


def room(request, pk):
    room = Room.objects.get(id=pk)
    comments = Comment.objects.filter(room=room)
    return render(request, 'room.html', {'room': room, 'comments': comments})


@login_required
def reservation(request, pk):
    obj = get_object_or_404(Room, id=pk)
    user = request.user
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form['arrival_date'].value() != form['departure_date'].value():
            if form.is_valid():
                res = form.save(commit=False)
                res.user = user
                obj.is_reserved = True
                res.room = obj
                obj.save()
                res.save()
                return redirect('/')
        else:
            messages.info(request, 'Arrival and departure date are equal')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form, 'room': obj})


@login_required
def profile(request):
    user = request.user
    reservations = Reservation.objects.all().order_by('-reserve_time')
    return render(request, 'profile.html', {'reservations': reservations, 'user': user})


@login_required
def delete_reservation(request, pk):
    obj = get_object_or_404(Reservation, id=pk)
    room = obj.room
    room.is_reserved = False
    room.save()
    obj.delete()
    return redirect('/profile')


@login_required
def edit_reservation(request, pk):
    obj = get_object_or_404(Reservation, id=pk)
    room = obj.room
    form = ReservationForm(request.POST or None, instance=obj)
    if form['arrival_date'].value() != form['departure_date'].value():
        if form.is_valid():
            res = form.save(commit=False)
            res.reserve_time = datetime.now()
            res.save()
            return redirect('/profile')
    else:
        messages.info(request, 'Arrival and departure date are equal')

    return render(request, 'reservation.html', {'form': form, 'room': room})


@login_required
def add_comment(request, pk):
    obj = get_object_or_404(Room, id=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['text'].value():
            if form['rate'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.user = user
                    com.room = obj
                    com.save()
                    return redirect('/rooms')
            else:
                messages.info(request, 'You must rate the room!')
        else:
            messages.info(request, 'You should type something!')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})


@login_required
def show_last_month(request):
    obj = Reservation.objects.filter(departure_date__gt=datetime.now() - timedelta(days=30))
    print(datetime.now() - timedelta(30))
    return render(request, 'lastmonth.html', {'objects': obj})
```
* `Файл models.py`
``` python
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    max_occupancy = models.IntegerField()
    is_reserved = models.FloatField(default=False)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserve_time = models.DateTimeField(default=datetime.now, blank=True)
    arrival_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    departure_date = models.DateTimeField(default=datetime.now, blank=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.now, blank=True)
    text = models.CharField(max_length=100000, blank=True)
    rate = models.IntegerField(default=1,
                               validators=[
                                   MaxValueValidator(10),
                                   MinValueValidator(1)
                               ])

```
* `Файл views.py`
``` python
from django import forms
from .models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['arrival_date', 'departure_date']
        exclude = ['user', 'room', 'reserve_time', 'comment']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {
            'text': forms.Textarea(attrs={'rows': 30, 'cols': 100, 'placeholder': 'Type your comment...'}),
        }
        fields = ['text', 'rate']
        exclude = ['user', 'create_time']
```
