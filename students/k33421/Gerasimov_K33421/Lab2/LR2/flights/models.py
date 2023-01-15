from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Модель авиакомпании
class AviaCompany(models.Model):
    class Meta:
        verbose_name = "Авиакомпания"
        verbose_name_plural = "Авиакомпании"

    name = models.CharField("Название", max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


# Модель рейса
class Flight(models.Model):
    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    class TypeChoices(models.IntegerChoices):
        DEPARTING = 0, "Отлет"
        ARRIVING = 1, "Прилет"

    number = models.CharField("Номер рейса", max_length=255, unique=True)
    from_city = models.CharField("Город отлета", max_length=255)
    to_city = models.CharField("Город прилета", max_length=255)
    departure_time = models.DateTimeField("Время отлета")
    arrival_time = models.DateTimeField("Время прилета")
    type = models.IntegerField("Отлет/прилет", choices=TypeChoices.choices)
    gate = models.CharField("Номер гейта", max_length=255)
    company = models.ForeignKey(AviaCompany, verbose_name="Авиакомпания", on_delete=models.CASCADE,
                                related_name="flights")

    def __str__(self):
        return str(self.number)


# Модель бронирования
class Booking(models.Model):
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    flight = models.ForeignKey(Flight, verbose_name="Рейс", on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="bookings")
    seats = models.IntegerField("Количество", validators=[MinValueValidator(1)])
    review_text = models.TextField("Отзыв", default="")
    review_number = models.IntegerField("Оценка", null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return str(self.id)
