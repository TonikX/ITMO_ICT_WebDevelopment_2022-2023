from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

class Hotel(models.Model):
    name = models.CharField("Название отеля", max_length=50, primary_key=True)
    owner = models.CharField("Владелец отеля", max_length=50)
    address = models.CharField("Адрес отеля", max_length=100)

class Room(models.Model):
    TYPE_ROOM = [
        ('S', 'Стандарт'),
        ('С', 'Комфорт'),
        ('L', 'Люкс'),
        ('F', 'Семейный'),
        ('P', 'Президентский'),
        ('A', 'Апартаменты')
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    number = models.IntegerField("Номер комнаты")
    description = models.CharField("Описание номера", max_length=1000)
    type_room = models.CharField("Тип номера", max_length=1, choices=TYPE_ROOM)
    beds = models.PositiveSmallIntegerField("Количество спальных мест", validators=[MinValueValidator(1)])
    price = models.PositiveIntegerField("Стоимость номера")

    class Meta:
        # One hotel can't have two rooms with the same number
        unique_together = ('hotel', 'number')


class Guest(models.Model):
    last_name = models.CharField("Фамилия", max_length=30, null=False)
    first_name = models.CharField("Имя", max_length=30, null=False)
    passport = models.CharField("Номер паспорта", primary_key=True, max_length=30)

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    date_start = models.DateField("Дата заезда")
    date_end = models.DateField("Дата выезда")
    total_price = models.PositiveIntegerField("Стоимость проживания", null=False)

    @property
    def days(self):
        return (self.date_end - self.date_start).days

    def check_date(self):
        if self.date_start >= self.date_end:
            raise ValidationError("Конечная дата должна быть больше начальной!")

    def save(self, *args, **kwargs):
        self.total_price = self.room.price * self.days
        super(Booking, self).save(*args, **kwargs)

class Feedback(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, verbose_name="Код бронирования")
    author = models.CharField("Укажите ваш ник", max_length=30)
    rate = models.IntegerField("Оценка", default=0, validators=[MaxValueValidator(10), MinValueValidator(1)])
    date_start = models.DateField("Дата заезда")
    date_end = models.DateField("Дата выезда")
    text = models.TextField("Комментарий", null=False)

    def save(self, *args, **kwargs):
        self.date_start = self.booking.date_start
        self.date_end = self.booking.date_end
        super(Feedback, self).save(*args, **kwargs)