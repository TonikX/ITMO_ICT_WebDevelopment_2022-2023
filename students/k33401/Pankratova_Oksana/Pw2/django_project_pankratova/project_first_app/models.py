from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


# Create your models here.
class User(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)


class CustomUser(AbstractUser):
    birth_date = models.DateField()
    passport = models.CharField(max_length=11, blank=True)
    home_add = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=30, blank=True)


class License(models.Model):
    TYPES = models.TextChoices('TYPES', 'A B A1 C D E F M BE CE DE')
    motorist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(choices=TYPES.choices, max_length=3)
    given = models.DateField()


class Automobile(models.Model):
    gos_number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(blank=True, max_length=30)
    owning = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ownership')

    def __str__(self):
        return "{} {} {} {}".format(self.gos_number, self.mark, self.model, self.color)


class Ownership(models.Model):
    id_auto = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    id_motorist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    begin = models.DateField()
    end = models.DateField(blank=True, null=True)

