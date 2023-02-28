from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField("username", max_length=150, unique=True)
    password = models.CharField(max_length=30, null=False)
    passport_data = models.CharField(max_length=30, null=False)
    email = models.EmailField("email address", unique=True)
    id = models.ManyToManyField("self", through="Reservation")
    phone_number = models.IntegerField(null=True)


class Tour(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    naming = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=2000, null=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.naming


class Feedback(models.Model):
    User = get_user_model()
    rating = [(1, '1'), (2, '2'), (3, '3'), (3, '3'), (4, '4'),
              (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)
    tour_id = models.ForeignKey("Tour", on_delete=models.CASCADE)
    user_rating = models.IntegerField(choices=rating)
    date_of_publication = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()


class Reservation(models.Model):
    User = get_user_model()
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.BooleanField(null=True)
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE)
