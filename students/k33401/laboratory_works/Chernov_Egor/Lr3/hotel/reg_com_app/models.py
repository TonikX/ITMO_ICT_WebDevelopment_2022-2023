from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from hotel_app.models import Hotel, RoomType, Room


class Registration(models.Model):
    STATUS_REG_CHOICES = [
        ('T', 'Taken'),
        ('B', 'Booked'),
    ]
    STATUS_PAY_CHOICES = [
        ('YP', 'Paid for'),
        ('NP', 'Not paid for'),
    ]

    user_reg = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='user_registration', verbose_name='ID User')
    hotel_reg = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='hotel_registration', verbose_name='ID Hotel')
    rt_reg = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='rt_registration', verbose_name='ID Room type')
    room_reg = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='room_registration', verbose_name='ID Room')

    employee_reg = models.PositiveIntegerField(null=True, blank=True, verbose_name='ID Employee')
    status_reg_reg = models.CharField(max_length=1, choices=STATUS_REG_CHOICES, verbose_name='Registration status')
    status_pay_reg = models.CharField(max_length=2, choices=STATUS_PAY_CHOICES, verbose_name='Payment status')
    check_in_reg = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out_reg = models.DateField(null=False, blank=False, verbose_name='Check out')
    booking_reg = models.DateField(null=False, blank=False, verbose_name='Booking date')


class Comment(models.Model):
    user_com = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_comment',
                                 verbose_name='ID Guest')
    room_com = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_comment', verbose_name='ID Room')

    rating_com = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                  verbose_name='Rating')
    review_com = models.TextField(max_length=255, null=True, blank=True, verbose_name='Review')
    check_in_com = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out_com = models.DateField(null=False, blank=False, verbose_name='Check out')
