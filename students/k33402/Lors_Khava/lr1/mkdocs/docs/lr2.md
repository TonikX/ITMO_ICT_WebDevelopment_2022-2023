# Laboratory work 2
## Реализация простого сайта на django

Вариант1: Список отелей.
Необходимо учитывать название отеля, владельца отеля, адрес, описание, типы
номеров, стоимость, вместимость, удобства.
Необходимо реализовать следующий функционал:

* Регистрация новых пользователей.

* Просмотр и резервирование номеров. Пользователь должен иметь
возможность редактирования и удаления своих резервирований.

* Написание отзывов к номерам. При добавлении комментариев, должны
сохраняться период проживания, текст комментария, рейтинг (1-10),
информация о комментаторе.

* Администратор должен иметь возможность заселить пользователя в отель и
выселить из отеля средствами Django-admin.

* В клиентской части должна формироваться таблица, отображающая
постояльцев отеля за последний месяц.

---

* `models.py`

```python 

from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)
    passport = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Hotel(models.Model):
    clients = models.ManyToManyField(Client, through='Booking', related_name='clients')
    hotel_name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.hotel_name

class Room(models.Model):
    number = models.CharField(max_length=5)
    type = models.CharField(max_length=30, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='hotel_room')
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.number}"

class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='book_client')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='book_hotel')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='book_room')
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.client}: {self.check_in_date} - {self.check_out_date}"


class Comment(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='author')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, related_name='inf_author')
    rating = models.IntegerField(choices=[(i, i) for i in range(0, 11)])
    review_comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.author}: {self.rating}"

```

* `urls.py`

```python

from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home),
    path("client_list/", clients_list),
    path("client_create/", clients_create),
    path("room_list/", room_list),
    path("book/", book),
    path("book_list/", book_list),
    path("month/", last_month),
    path("book_update/<int:pk>/", BookUpdate.as_view()),
    path("book_delete/<int:pk>/", BookDelete.as_view()),
    path('hotel_list/', HotelList.as_view()),
    path('hotel/<str:pk>', hotel_view),
    path('hotel/review/<str:pk>', comment)
]
```

* `views.py`

```python

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import ListView, UpdateView, DeleteView
from .forms import ClientForm, BookingForm, CommentForm
from .models import Client, Hotel, Room, Booking, Comment
import datetime

# основная страница
def home(request):
    return render(request, "home.html")

# данные о клиентах
def clients_list(request):
    data = {"clients": Client.objects.all()}
    return render(request, "clients_list.html", data)

# создание нового клиента для регистрации
def clients_create(request):
    data = {}
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/client_list')
    data["form"] = form
    return render(request, "register.html", data)

# данные о номерах
def room_list(request):
    data = {"rooms": Room.objects.all()}
    return render(request, "room_list.html", data)

# бронирование
def book(request):
    data = {}
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
    data["form"] = form
    return render(request, "booking.html", data)

# данные о бронировании
def book_list(request):
    data = {"booking": Booking.objects.all()}
    return render(request, "book_list.html", data)

# cписок клиентов последнего месяца
def last_month(request):
    data = {}
    try:
        month = datetime.date.today() - datetime.timedelta(days=31)
        data["booking"] = Booking.objects.all().filter(check_in_date__gte=str(month),
        check_out_date__lte=str(datetime.date.today()))
        print(data)
    except Booking.DoesNotExist:
        raise Http404("No guests this month yet :(")
    return render(request, "book_list.html", data)

# редактирование брони
class BookUpdate(UpdateView):
    model = Booking
    template_name = "book_update.html"
    fields = ["check_in_date", "check_out_date", "client", "room"]
    success_url = "/book_list/"

# удаление брони
class BookDelete(DeleteView):
    model = Booking
    template_name = "book_delete.html"
    success_url = "/book_list/"

# таблица гостей отеля
class HotelList(ListView):
    model = Hotel
    template_name = 'hotel.html'
    all_hotels = Hotel.objects

# обзор на отели
def hotel_view(request, pk):
    hotel = Hotel.objects.get(id=pk)
    comments = Comment.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'comments': comments})

# написание комментария и просмотр 
def comment(request, pk):
    obj = get_object_or_404(Hotel, id=pk)
    author = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['review_comment'].value():
            if form['rating'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.client = author
                    com.hotel = obj
                    com.save()
    else:
        form = CommentForm()
    return render(request, 'review.html', {'form': form})
```


