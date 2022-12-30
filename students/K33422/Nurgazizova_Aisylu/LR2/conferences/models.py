from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Conference(models.Model):
    title = models.CharField(max_length=1000)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)
    themes = models.CharField(max_length=100000)
    place = models.CharField(max_length=1000)
    place_description = models.CharField(max_length=10000)
    con_description = models.CharField(max_length=10000)
    conditions = models.CharField(max_length=10000)


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    theme = models.CharField(max_length=1000)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.CharField(max_length=100000, blank=True)
    rate = models.IntegerField(default=1,
                               validators=[
                                   MaxValueValidator(10),
                                   MinValueValidator(1)
                               ])


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_recommended = models.FloatField(default=False)