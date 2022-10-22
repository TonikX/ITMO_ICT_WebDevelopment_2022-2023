from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Hotel(models.Model):
    id_hotel = models.IntegerField(primary_key=True, verbose_name='ID Hotel')
    name_hotel = models.CharField(max_length=100, verbose_name='Name')
    city_hotel = models.CharField(max_length=30, verbose_name='City')
    address_hotel = models.CharField(max_length=255, verbose_name='Address')
    rating_hotel = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                    null=True,
                                                    blank=True,
                                                    verbose_name='Rating')
    des_hotel = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')


class Guest(models.Model):
    id_guest = models.IntegerField(primary_key=True, verbose_name='ID Guest')
    first_name_guest = models.CharField(max_length=30, verbose_name='First name')
    last_name_guest = models.CharField(max_length=30, verbose_name='Last name')
    phone_guest = models.CharField(max_length=12, verbose_name='Phone')
    passport_guest = models.CharField(max_length=10, verbose_name='Passport')

    class Meta:
        ordering = ["first_name_guest", "last_name_guest"]


class Employee(models.Model):
    id_employee = models.IntegerField(primary_key=True, verbose_name='ID Employee')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    first_name_employee = models.CharField(max_length=30, verbose_name='First name')
    last_name_employee = models.CharField(max_length=30, verbose_name='Last name')
    phone_employee = models.CharField(max_length=12, verbose_name='Phone')

    class Meta:
        ordering = ["first_name_employee", "last_name_employee"]


class RoomType(models.Model):
    ECONOM = 'E'
    STANDARD = 'S'
    LUX = 'L'
    TYPE_CHOICES = [
        (ECONOM, 'Econom'),
        (STANDARD, 'Standard'),
        (LUX, 'Lux'),
    ]
    id_rt = models.IntegerField(primary_key=True, verbose_name='ID Room type')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    type_rt = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name='Type')
    rating_rt = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                 null=True,
                                                 blank=True,
                                                 verbose_name='Rating')
    price_rt = models.PositiveIntegerField(verbose_name='Price')
    des_rt = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')

    class Meta:
        ordering = ["id_rt"]


class Room(models.Model):
    FREE = 'F'
    TAKEN = 'T'
    BOOKED = 'B'
    STATUS_CHOICES = [
        (FREE, 'Free'),
        (TAKEN, 'Taken'),
        (BOOKED, 'Booked'),
    ]
    id_room = models.IntegerField(primary_key=True, verbose_name='ID Room')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    id_rt = models.ForeignKey(RoomType, on_delete=models.SET_NULL, verbose_name='ID Room type')
    number_room = models.IntegerField(verbose_name='Number')
    status_room = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F', verbose_name='Status')
    review_room = models.CharField(max_length=255, null=True, blank=True, verbose_name='Review')

    class Meta:
        ordering = ["number_room"]


class Registration(models.Model):
    TAKEN = 'T'
    BOOKED = 'B'
    PAID = 'YP'
    NO_PAID = 'NP'
    STATUS_REG_CHOICES = [
        (TAKEN, 'Taken'),
        (BOOKED, 'Booked'),
    ]
    STATUS_PAY_CHOICES = [
        (PAID, 'Paid for'),
        (NO_PAID, 'Not paid for'),
    ]
    id_reg = models.IntegerField(primary_key=True, verbose_name='ID Reg')
    id_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, verbose_name='ID Employee')
    id_guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, verbose_name='ID Guest')
    id_room = models.ForeignKey(Room, on_delete=models.SET_NULL, verbose_name='ID Room')
    status_reg = models.CharField(max_length=1, choices=STATUS_REG_CHOICES, verbose_name='Registration status')
    status_pay = models.CharField(max_length=2, choices=STATUS_PAY_CHOICES, verbose_name='Payment status')
    check_in = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out = models.DateField(null=False, blank=False, verbose_name='Check out')
    booking = models.DateField(null=False, blank=False, verbose_name='Booking date')

    class Meta:
        ordering = ["-check_in", "-check_out"]
