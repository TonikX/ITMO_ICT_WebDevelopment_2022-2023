from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Tourist(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Tour(models.Model):
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(auto_now_add=True, blank=True)
    terms_of_payment = models.CharField(max_length=50)
    tourists = models.ManyToManyField('Tourist', through='Reservation')


class Reservation(models.Model):
    tourist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class Comment(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    author = models.ForeignKey('Tourist', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    publish_date = models.DateTimeField(auto_now_add=True)
    
