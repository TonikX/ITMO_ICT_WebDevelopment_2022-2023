from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=100, verbose_name='Name')
    city_hotel = models.CharField(max_length=100, verbose_name='City')
    address_hotel = models.CharField(max_length=255, verbose_name='Address')
    rating_hotel = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                                    null=True,
                                                    blank=True,
                                                    verbose_name='Rating')
    des_hotel = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')


class RoomType(models.Model):
    TYPE_CHOICES = [
        ("E", 'Econom'),
        ("S", 'Standard'),
        ("L", 'Lux'),
    ]

    hotel_rt = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_room_type",
                                 verbose_name='ID Hotel')
    type_rt = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name='Type')
    rating_rt = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],
                                                 null=True,
                                                 blank=True,
                                                 verbose_name='Rating')
    price_rt = models.PositiveIntegerField(verbose_name='Price')
    des_rt = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')


class Room(models.Model):
    STATUS_CHOICES = [
        ("F", 'Free'),
        ("T", 'Taken'),
        ("B", 'Booked'),
    ]

    hotel_r = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_room", verbose_name='ID Hotel')
    rt_r = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rt_room", verbose_name='ID Room type')
    number_room = models.PositiveIntegerField(verbose_name='Number')
    status_room = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F', verbose_name='Status')
    review_room = models.CharField(max_length=255, null=True, blank=True, verbose_name='Review')
