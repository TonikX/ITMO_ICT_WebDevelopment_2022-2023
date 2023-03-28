# Лабораторная работа 2
## Список отелей
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
### Модели
Описание моделей:
* Отели
* Тип комнаты
* Комната
* Резервация
* Комментарий

`models.py`
```python
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    amenities = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


ROOM_STATUS = (
    ('занято', 'занято'),
    ('свободно', 'свободно'),
    ('закрыто', 'закрыто')
)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    availability = models.CharField(
        max_length=50, choices=ROOM_STATUS, default=ROOM_STATUS[1])

    def __str__(self):
        return str(self.id)


STATUSES = (
    ('бронь', 'бронь'),
    ('заехал', 'заехал'),
    ('выехал', 'выехал'),
    ('отменено', 'отменено'),
)


class Reservation(models.Model):
    date_check_in = models.DateField()
    date_check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUSES)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=500)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(0, 11)], default=(0, 0))
    reservation = models.ForeignKey(
        Reservation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.reservation.id + ' ' + self.reservation.guest.first_name
```
### Шаблоны
Для краткости и удобства приведем пример только одного шаблона.
* main.html - основной шаблон
* hotel_detail.html - шаблон описания отеля
* hotels_list.html - список отелей
* login.html - страница для входа в учетную запись
* logout.html - страница для выхода из учетной записи
* register.html - страница создания учетной записи
* reservation.html - страница для создания резервации
* reservation_confirm_delete.html - страница отмены резервации
* reservations.html - страница со всеми резервациями
* room.html - шаблон комнаты
```python
{% extends 'hotels/main.html' %}

{% block content %}

<div class="room">
    <div class="header-bar">
      <h2 class="author">{{room.type.name|title}}</h2>
      <h3 class="rating">{{room.type.price}} руб.</h3>
      <h4 class="availability">{{room.availability}}</h4>
      <h4><a href={% url "room_reservation" room.hotel.id room.id%}>Зарезервировать</a></h4>
    </div>
    <div class="header-bar">
      <p class="text">Кол-во человек: {{room.type.capacity}}</p>
      <p class="text">Удобства: {{room.type.amenities}}</p>
    </div>
    <h4>Комментарии: </h4>
    {% if request.user.is_authenticated %}
        <form class='comment-form' method="post">
            {% csrf_token %}
            <p class="rating">Рейтинг: {{ comment_form.rating }}</p>
            <p class="text">Текст: <br /> {{comment_form.text}}</p>
            {{comment_form.reservation}}
            <input class="button" type="submit" value="Добавить">
        </form>
    {% endif %}

    {% for comment in comments %}
        <div class="comment">
        <div class="header-bar">
            <h4 class="author">{{comment.reservation.guest|title}}</h4>
            <h3 class="rating">{{comment.rating|title}}</h3>
            <p>даты пребывания: {{comment.reservation.date_check_in}} - {{comment.reservation.date_check_out}}</p>
        </div>
        <p class="text">{{comment.text}}</p>
        </div>
    {% endfor %}
    
</div>



{% endblock content %}
```
### Представления
`views.py`
```python
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Hotel, RoomType, Room, Reservation, Comment
from .forms import CommentForm, ReservationForm


class CustomLoginView(LoginView):
    template_name = 'hotels/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('hotels')


class RegisterPage(FormView):
    template_name = 'hotels/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('hotels')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('hotels')
        return super(RegisterPage, self).get(*args, **kwargs)


class HotelsList(ListView):
    model = Hotel
    template_name = 'hotels/hotels_list.html'
    context_object_name = 'hotels'


def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    rooms = Room.objects.filter(hotel__pk=hotel_id)
    context = {'hotel': hotel, 'rooms': rooms}
    return render(request, 'hotels/hotel_detail.html', context)


def room_detail(request, hotel_id, room_id):
    hotel = Hotel.objects.get(pk=hotel_id)
    room = Room.objects.get(pk=room_id)
    if request.user.is_authenticated:
        reservations = Reservation.objects.filter(
            room__id=room_id, guest=request.user)
    else:
        reservations = None
    comments = Comment.objects.filter(reservation__room__id=room_id)
    initial = {'reservation': reservations}
    comment_form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form. save()
        else:
            comment_form = c_form
    context = {'hotel': hotel, 'room': room,
               'comment_form': comment_form, 'comments': comments}
    return render(request, 'hotels/room.html', context)


@login_required
def reservation_view(request, hotel_id, room_id,):
    room = Room.objects.get(pk=room_id)
    initial = {'room': room, 'guest': request.user}
    form = ReservationForm(initial=initial)
    if request.method == 'POST':
        c_form = ReservationForm(request.POST)
        if c_form.is_valid():
            c_form. save()
            return redirect(f'/hotel/{hotel_id}/room/{room_id}')
        else:
            form = c_form
    context = {'room': room, 'form': form}
    return render(request, 'hotels/reservation.html', context)


class ReservationList(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'hotels/reservations.html'
    context_object_name = 'reservations'


class DeleteReservationView(LoginRequiredMixin, DeleteView):
    model = Reservation
    context_object_name = 'reservation'
    success_url = reverse_lazy('reservations')
```
### Маршрутизация
Описание путей:
* /login/ - вход в учетную запись
* /logout/ - выход из учетной записи 
* /register/ - создать учетную запись
* /hotels/ - список отелей
* /hotel/<int:hotel_id>/ - конкретный отель
* /hotel/<int:hotel_id>/room/<int:room_id>/ - конкретная комната
* /hotel/<int:hotel_id>/room/<int:room_id>/reservation/ - резервация комнаты
* /reservation/ - резервации
* /reservation/delete/<int:pk>/ - удаление резервации
`urls.py`
```python
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(
        next_page='hotels'), name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('', views.HotelsList.as_view(), name='hotels'),
    path('hotel/<int:hotel_id>', views.hotel_detail, name='hotel'),
    path('hotel/<int:hotel_id>/room/<int:room_id>',
         views.room_detail, name='room'),
    path('hotel/<int:hotel_id>/room/<int:room_id>/reservation',
         views.reservation_view, name='room_reservation'),
    path('reservation', views.ReservationList.as_view(), name='reservations'),
    path('reservation/delete/<int:pk>',
         views.DeleteReservationView.as_view(), name='reservation_delete'),

]
```
