# Лабораторная работа 2

## Структура проекта

- `megaultrabooking` - основная директория проекта
- `megaultrabooking` - приложение
- `megaultrabooking/templates` - директория с templates

## Настройки

- `megaultrabooking/settings.py`  

_Настройки авторизации_

```python
AUTH_USER_MODEL = "megaultrabooking.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
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
    "megaultrabooking",
]
```

- `megaultrabooking/urls.py`  

_URL-паттерны приложения megaultrabooking_

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("personal/", personal_page, name="personal"),
    path("register/", register_user, name="register"),
    path("hotels/", hotels_list, name="hotels_list"),
    path("hotels/add", add_hotel, name="add_hotel"),
    path("hotels/<int:hotel_id>/statistics/", hotel_statistics, name="hotel_statistics"),
    path("hotels/<int:hotel_id>/rooms/", rooms_list, name="rooms_list"),
    path("hotels/<int:hotel_id>/rooms/add", add_room, name="add_room"),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/reviews/", reviews_list, name="reviews_list"),
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/booking/", add_booking, name="add_booking"),
    path("bookings/<int:booking_id>", bookings_list, name="bookings_list"),
    path("bookings/<int:booking_id>/review", add_review, name="add_review"),
    path("bookings/<int:booking_id>/edit", edit_booking, name="edit_booking"),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
```

## Приложение

- Исходный код форм `forms.py`

```python
from django.forms import ModelForm, BooleanField, DateField, Form
from django.forms.widgets import DateInput, SelectDateWidget

from .models import User, Hotel, Room, Review, Booking

# Форма регистрации
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

# Форма создания отеля
class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "address", "description"]

# Форма создания комнаты в отеле
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ["room_type", "price", "facilities"]

# Форма добавления отзывов к бронированию
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]

# Форма создания бронирования (с виджетами для выбора даты начала и конца)
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["ts_start", "ts_end"]
        widgets = {
            "ts_start": DateInput(attrs={"type": "date"}),
            "ts_end": DateInput(attrs={"type": "date"}),
        }

# Форма редактирования бронирования (возможность сдвига дат и отмены)
class EditBookingForm(Form):
    cancel = BooleanField(required=False)
    ts_start = DateField(required=False, widget=DateInput(attrs={"type": "date"}))
    ts_end = DateField(required=False, widget=DateInput(attrs={"type": "date"}))

    class Meta:
        fields = ["cancel", "ts_start", "ts_end"]

```

- Исходный код URL-паттернов `urls.py`

```python
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin
from megaultrabooking.views import (
    hotels_list,
    rooms_list,
    reviews_list,
    register_user,
    add_hotel,
    add_room,
    add_review,
    add_booking,
    bookings_list,
    personal_page,
    edit_booking,
    hotel_statistics,
)

urlpatterns = [
    path("admin/", admin.site.urls), # панель администратора
    path("accounts/", include("django.contrib.auth.urls")), # подключение авторизации
    path("personal/", personal_page, name="personal"), # личный кабинет
    path("register/", register_user, name="register"), # регистрация
    path("hotels/", hotels_list, name="hotels_list"), # список отелей
    path("hotels/add", add_hotel, name="add_hotel"), # добавление отелей
    path("hotels/<int:hotel_id>/statistics/", hotel_statistics, name="hotel_statistics"), # статистика по отелю за последний месяц
    path("hotels/<int:hotel_id>/rooms/", rooms_list, name="rooms_list"), # список номеров отеля
    path("hotels/<int:hotel_id>/rooms/add", add_room, name="add_room"), # добавление номера
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/reviews/", reviews_list,  name="reviews_list"),# список отзывов
    path("hotels/<int:hotel_id>/rooms/<int:room_id>/booking/", add_booking, name="add_booking"), # создание бронирования
    path("bookings/<int:booking_id>", bookings_list, name="bookings_list"),
    path("bookings/<int:booking_id>/review", add_review, name="add_review"),
    path("bookings/<int:booking_id>/edit", edit_booking, name="edit_booking"),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
]
```

- Исходный код моделей `models.py`
 
```python
from __future__ import annotations

from dateutil.relativedelta import relativedelta
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Тип пользователя - арендатор или арендодатель
class UserType(models.TextChoices):
    LANDLORD = ("LL", "Landlord")
    RENTER = ("RR", "Renter")

# Тип комнаты - односпальная, двуспальная, люкс
class RoomType(models.TextChoices):
    SINGLE = ("S", "Single Person")
    TWOBEDS = ("TB", "Two Bedrooms")
    LUX = ("LUX", "President Residence")

# Модель пользователя (наследование от AbstractUser)
class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=3, choices=UserType.choices, default=UserType.RENTER)

    @property
    def landlord(self):
        return self.type == UserType.LANDLORD

    def __str__(self) -> str:
        return f"{self.username}"

# Модель отеля
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def get_last_month_booking_statistics(self):
        """Получение статистики отеля за последний месяц"""
        last_month_start = datetime.datetime.now() - relativedelta(months=1)
        last_month_end = datetime.datetime.now()

        bookings = Booking.objects.filter(
            room__hotel_id=self.id, ts_start__gte=last_month_start, ts_end__lt=last_month_end
        )

        revenue = 0
        for b in bookings:
            revenue += b.price

        return {"booking_count": bookings.count(), "total_revenue": revenue}

    def get_last_month_visitors(self):
        """Получение списка посетителей за последний месяц"""
        last_month_start = datetime.datetime.now() - relativedelta(months=1)
        last_month_end = datetime.datetime.now()

        bookings = Booking.objects.filter(
            room__hotel_id=self.id, ts_start__gte=last_month_start, ts_end__lt=last_month_end
        )

        visitor_ids = bookings.values_list("user_id", flat=True)
        visitors = User.objects.filter(id__in=visitor_ids)

        return bookings

    def __str__(self) -> str:
        return self.name

# Модель комнаты отеля
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=3, choices=RoomType.choices, default=RoomType.SINGLE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    facilities = models.TextField()

    @property
    def capacity(self):
        """Вместимость, в зависимости от типа номера"""
        match self.room_type:
            case RoomType.SINGLE:
                return 1
            case RoomType.TWOBEDS:
                return 2
            case RoomType.LUX:
                return 10
            case _:
                return 1

    def __str__(self) -> str:
        return f"{self.hotel.name}: {self.room_type} ({self.price})"

# Статус бронирования
class BookingState(models.TextChoices):
    PENDING = ("PD", "Ожидает")
    CANCELED = ("CL", "Отменено")
    FINISHED = ("FN", "Прошедшее")

# Модель бронирования отеля
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2, choices=BookingState.choices, default=BookingState.PENDING)
    ts_start = models.DateField()
    ts_end = models.DateField()

    @property
    def is_past_due(self) -> bool:
        """Прошло ли бронирование"""
        return datetime.date.today() > self.ts_start

    @property
    def canceled(self) -> bool:
        """Отменено ли бронирование"""
        return self.state == BookingState.CANCELED

    @property
    def price(self) -> int:
        """Итоговая стоимость (по датам и стоимости команаты посуточно)"""
        days = (self.ts_end - self.ts_start).days
        return int(self.room.price * days)

    def __str__(self) -> str:
        return (
            f"{self.room.hotel.name}: {self.room.room_type} ({self.user.username}, С {self.ts_start} ПО {self.ts_end})"
        )

# Модель отзыва
class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    ts_created = models.DateField()

    def __str__(self) -> str:
        return f"{self.booking} | {self.rating}"
```
