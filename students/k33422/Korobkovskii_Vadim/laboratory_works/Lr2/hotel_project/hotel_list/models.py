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


