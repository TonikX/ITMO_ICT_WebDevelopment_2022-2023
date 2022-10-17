from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Hotel(models.Model):
    name = models.CharField("Название отеля", primary_key = True, max_length=255)
    address = models.CharField("Адрес", max_length=255)
    stars = models.PositiveSmallIntegerField("Рейтинг", validators=[MinValueValidator(1), MaxValueValidator(5)])
    owner = models.CharField("Владелец отеля", max_length=255)

    def __str__(self):
        return f"{self.stars}-star hotel {self.name}"

class Room(models.Model):
    number_room = models.IntegerField("Номер комнаты", primary_key = True)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, verbose_name = "Отель")
    type_room = models.CharField("Описание комнаты", max_length=100)
    beds = models.PositiveSmallIntegerField("Количество спальных мест", validators=[MinValueValidator(1)])  
    room_price = models.PositiveIntegerField("Стоимость номера")

    class Meta:
        # One hotel can't have two rooms with the same number
        unique_together = ('hotel', 'number_room')

    def __str__(self):
        return f"Room {self.number_room} of hotel {self.hotel.name}"

class Guest(models.Model):
    first_name = models.CharField("Имя", max_length=30, null=False)
    last_name = models.CharField("Фамилия", max_length=30, null=False)
    passport = models.CharField("Номер паспорта", primary_key=True, max_length=30)

    def __str__(self):
        return f"Гость {self.last_name} {self.first_name}"


class Reservation(models.Model):
    order_number = models.AutoField("Номер заказа", primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default = "Ромашка")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE,verbose_name = "Гость") 
    arrival_date = models.DateField("Дата заезда")
    departure_date = models.DateField("Дата выезда")
    price = models.PositiveIntegerField("Стоимость проживания")
    booking_date = models.DateTimeField("Дата бронирования", auto_now_add=True)

    @property
    def duration(self):
        return (self.departure_date - self.arrival_date).days

    def clean(self):
        # Check that start < end
        if self.arrival_date >= self.departure_date:
            raise ValidationError("Duration date must be greater than start date")

    def save(self, *args, **kwargs):
        # Calculate the price based on number of nights at the hotel
        self.price = self.room.room_price * self.duration
        super(Reservation, self).save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.pk} in hotel {self.room.hotel.name} from {self.arrival_date} to {self.departure_date}"

class Comment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, verbose_name = "Код бронирования")
    date_start = models.DateField("Дата заезда")
    date_end = models.DateField("Дата выезда")
    text = models.TextField("Комментарий", null=False)
    rate = models.IntegerField("Оценка", default=10,validators=[MaxValueValidator(10), MinValueValidator(1)])
    sing_author = models.CharField("Укажите ваш ник", max_length=30)

    def save(self, *args, **kwargs):
        self.date_start  = self.reservation.arrival_date
        self.date_end = self.reservation.departure_date
        super(Comment, self).save(*args, **kwargs)
