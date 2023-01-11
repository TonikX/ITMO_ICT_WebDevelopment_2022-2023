from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    # фамилия
    surname = models.CharField(max_length=30)
    # отчество
    lastname = models.CharField(max_length=30)
    passport = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username


class Conference(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 10)])
    text = models.CharField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text