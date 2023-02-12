from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.model


class Ownership(models.Model):
    # car_owner_id = models.ForeignKey(
    #     'CarOwner', on_delete=models.CASCADE, null=True, blank=True)
    car_id = models.ForeignKey(
        'Car', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                end_date__gt=models.F('start_date')), name='start_end_date_check', violation_error_message='Start date must be earlier than end date.'),
        ]

    def __str__(self):
        # return f"{self.car_id.__str__()} ({self.car_owner_id.__str__()})"
        try:
            date_range = f"{self.start_date.year}-{self.end_date.year}"
        except AttributeError:
            date_range = f"{self.start_date.year}-present"

        return f"{self.car_id.__str__()} ({date_range})"


class CarOwner(AbstractUser):

    ownership_id = models.ManyToManyField('Ownership', blank=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(max_length=30, null=True, blank=True)

    passport = models.CharField(max_length=10)
    address = models.CharField(max_length=200, blank=True)
    nationality = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        verbose_name = "Car owner"
        verbose_name_plural = "Car owners"

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)


class DriverLicense(models.Model):
    LICENSE_TYPES = (
        ('A', 'Motorcycles'),
        ('B', 'Cars'),
        ('C', 'Trucks'),
        ('D', 'Buses'),
        ('M', 'Motorbikes'),
    )
    car_owner_id = models.ForeignKey('CarOwner', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10, choices=LICENSE_TYPES,
                                    default='B')
    issue_date = models.DateTimeField()

    def __str__(self):
        return f"{self.license_type} - {self.car_owner_id.__str__()} ({self.serial_number})"
