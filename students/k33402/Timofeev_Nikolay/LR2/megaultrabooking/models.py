from __future__ import annotations

from dateutil.relativedelta import relativedelta
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.TextChoices):
    LANDLORD = ('LL', 'Landlord')
    RENTER = ('RR', 'Renter')


class RoomType(models.TextChoices):
    SINGLE = ('S', "Single Person")
    TWOBEDS = ('TB', "Two Bedrooms")
    LUX = ('LUX', "President Residence")


class User(AbstractUser):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=3, choices=UserType.choices, default=UserType.RENTER)

    @property
    def landlord(self):
        return self.type == UserType.LANDLORD

    def __str__(self) -> str:
        return f"{self.username}"


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def get_last_month_booking_statistics(self):
        last_month_start = datetime.datetime.now() - relativedelta(months=1)
        last_month_end = datetime.datetime.now()

        bookings = Booking.objects.filter(
            room__hotel_id=self.id,
            ts_start__gte=last_month_start,
            ts_end__lt=last_month_end
        )

        revenue = 0
        for b in bookings:
            revenue += b.price

        return {
            'booking_count': bookings.count(),
            'total_revenue': revenue
        }

    def get_last_month_visitors(self):
        last_month_start = datetime.datetime.now() - relativedelta(months=1)
        last_month_end = datetime.datetime.now()

        bookings = Booking.objects.filter(
            room__hotel_id=self.id,
            ts_start__gte=last_month_start,
            ts_end__lt=last_month_end
        )

        visitor_ids = bookings.values_list('user_id', flat=True)
        visitors = User.objects.filter(id__in=visitor_ids)

        return bookings

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=3, choices=RoomType.choices, default=RoomType.SINGLE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    facilities = models.TextField()

    @property
    def capacity(self):
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


class BookingState(models.TextChoices):
    PENDING = ('PD', 'Ожидает')
    CANCELED = ('CL', 'Отменено')
    FINISHED = ('FN', 'Прошедшее')


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2, choices=BookingState.choices, default=BookingState.PENDING)
    ts_start = models.DateField()
    ts_end = models.DateField()

    @property
    def is_past_due(self) -> bool:
        return datetime.date.today() > self.ts_start

    @property
    def canceled(self) -> bool:
        return self.state == BookingState.CANCELED

    @property
    def price(self) -> int:
        days = (self.ts_end - self.ts_start).days
        return int(self.room.price * days)


    def __str__(self) -> str:
        return f"{self.room.hotel.name}: {self.room.room_type} ({self.user.username}, С {self.ts_start} ПО {self.ts_end})"


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    ts_created = models.DateField()

    def __str__(self) -> str:
        return f"{self.booking} | {self.rating}"
