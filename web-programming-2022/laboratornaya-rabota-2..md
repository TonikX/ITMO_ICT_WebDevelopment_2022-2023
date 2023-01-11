---
description: 'Цель работы: дать краткое представление о работе Django WEB фреймворка.'
---

# Лабораторная работа 2.

## Задание 1: Гостиница

Список отелей Необходимо учитывать название отеля, владельца отеля, адрес, описание, типы номеров, стоимость, вместимость, удобства. Необходимо реализовать следующий функционал:&#x20;

* Регистрация новых пользователей.&#x20;
* Просмотр и резервирование номеров. Пользователь должен иметь возможность редактирования и удаления своих резервирований.&#x20;
* Написание отзывов к номерам. При добавлении комментариев, должны сохраняться период проживания, текст комментария, рейтинг (1-10), информация о комментаторе.&#x20;
* Администратор должен иметь возможность заселить пользователя в отель и выселить из отеля средствами Django-admin.&#x20;
* В клиентской части должна формироваться таблица, отображающая постояльцев отеля за последний месяц.

## Основные файлы с кодом

* models.py

```
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Guest(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    Guest = get_user_model()
    number = models.IntegerField()
    type = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    capacity = models.IntegerField(null=True)
    amenities = models.CharField(max_length=30, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    guest = models.ManyToManyField(Guest, through='Accommodation')

    def __str__(self):
        return f"{self.number} | {self.hotel}"


class Accommodation(models.Model):
    Guest = get_user_model()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.guest} | {self.check_in_date} | {self.check_out_date}"


class Comment(models.Model):
    Guest = get_user_model()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(null=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.guest} | {self.rating}"

```

* views.py

```
from django.shortcuts import render
from django.http import Http404
from .models import Owner, Car
from .forms import OwnerForm
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView


def owner_show(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, "owner.html", {"owner": owner})


def owner_list(request):
    data = {"owners": Owner.objects.all()}
    return render(request, "owner_list.html", data)


def owner_create(request):
    data = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "owner_create.html", data)


class CarRetrieveView(DetailView):
    model = Car


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarCreateView(CreateView):
    model = Car
    template_name = "car_create.html"
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list"


class CarUpdateView(UpdateView):
    model = Car
    template_name = "car_update.html"
    fields = ["number", "brand", "model", "color"]
    success_url = "/car/list"


class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_delete.html"
    success_url = "/car/list"
```

* urls.py

```
from django.urls import path
from .views import *


urlpatterns = [
    path("guest/list/", guest_list),
    path("guest/create/", guest_create),
    path("room/list/", room_list),
    path("book/", book),
    path("book/list/", book_list),
    path("month/", last_month),
    path("accom/list/", accommodation_list),
    path("accom/<int:pk>/update/", AccomUpdate.as_view()),
    path("accom/<int:pk>/delete/", AccomDelete.as_view()),
    path("home/", home),
    path('hotel/list/', HotelList.as_view()),
    path('hotel/<str:pk>', hotel_view),
    path('hotel/review/<str:pk>', comment)
]
```

* forms.py

```
from django import forms
from .models import Guest, Accommodation, Comment


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = [
            "username", "password", "last_name",
            "first_name", "birth_date", "passport"
        ]


class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = [
            "check_in_date", "check_out_date",
            "guest", "room"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment", "rating",
            "guest", "hotel"
        ]
```
