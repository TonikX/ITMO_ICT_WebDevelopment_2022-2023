from django.db import models
from django.core.exceptions import ValidationError

class Guest(models.Model):
    passport = models.TextField("Номер паспорта", max_length=10, primary_key=True)
    last_name = models.TextField("Фамилия", max_length=20, null=False)
    first_name = models.TextField("Имя", max_length=20, null=False)
    patronymic = models.TextField("Отчество", max_length=20, null=True)
    city = models.TextField("Город", max_length=30, null=False)


class TypesRoom(models.Model):
    ROOM_TYPES = (
        ("Одноместный", "Одноместный"),
        ("Двуместный", "Двуместный"),
        ("Трехместный", "Трехместный"),
    )
    name_type = models.TextField("Тип номера", choices=ROOM_TYPES)
    count_beds = models.IntegerField("Кол-во спальных мест")
    price = models.FloatField("Цена")


class Room(models.Model):
    room_number = models.IntegerField("Номер комнаты", primary_key=True)
    room_type = models.ForeignKey(TypesRoom, on_delete=models.CASCADE, verbose_name="Тип номера")
    floor = models.PositiveIntegerField("Этаж")
    phone_number = models.PositiveIntegerField("Номер телефона", max_length=11)


class Booking(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="booking_room")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="booking_guest")
    date_start = models.DateTimeField("Дата заезда")
    date_end = models.DateTimeField("Дата выезда")
    total_price = models.PositiveIntegerField("Стоимость проживания", null=True)

    @property
    def days(self):
        return (self.date_end - self.date_start).days

    def check_date(self):
        if self.date_start >= self.date_end:
            raise ValidationError("Конечная дата должна быть больше начальной!")

    def save(self, *args, **kwargs):
        self.total_price = self.room_number.room_type.price * self.days
        super(Booking, self).save(*args, **kwargs)


class Workers(models.Model):
    last_name = models.TextField("Фамилия", max_length=20, null=False)
    first_name = models.TextField("Имя", max_length=20, null=False)
    patronymic = models.TextField("Отчество", max_length=20, null=True)


class Cleaning(models.Model):
    WEEK_DAYS = (
        ("ПН", "Понедельник"),
        ("ВТ", "Вторник"),
        ("СР", "Среда"),
        ("ЧТ", "Четверг"),
        ("ПТ", "Пятница"),
        ("СБ", "Суббота"),
        ("ВС", "Воскресенье"),
    )

    id_worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField("Этаж")
    day_of_week = models.TextField("День недели", choices=WEEK_DAYS)
