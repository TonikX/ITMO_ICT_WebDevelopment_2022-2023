from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse


class OwnerUser(AbstractUser):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class License(models.Model):
    user = get_user_model()
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateField(null=False)

    def __str__(self):
        return self.number

class Car(models.Model):
    gos_number = models.CharField(max_length=15, null=False)
    mark = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)
    user = get_user_model()
    owner = models.ManyToManyField(user, through='Ownership')

    def __str__(self):
        return self.gos_number

class Ownership(models.Model):
    user = get_user_model()
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True)
