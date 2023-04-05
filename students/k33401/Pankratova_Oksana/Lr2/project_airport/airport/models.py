from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Flight(models.Model):
    TYPES = models.TextChoices('TYPES', 'arrival departure')
    number = models.CharField(max_length=10)
    company = models.CharField(max_length=30)
    type = models.CharField(choices=TYPES.choices, max_length=10)
    arr_time = models.DateTimeField()
    dep_time = models.DateTimeField()
    gate = models.IntegerField()
    passengers = models.ManyToManyField(User, through='Ticket', related_name='flights')
    comments = models.ManyToManyField(User, through='Comment', related_name='com_flight')


class Ticket(models.Model):
    FOOD = (('in', 'included'), ('not', 'not included'))
    CLASS = (('eco', 'econom'), ('bus', 'business'))
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, unique=True, blank=True)
    food = models.CharField(max_length=15, choices=FOOD, blank=True)
    clas = models.CharField(max_length=10, choices=CLASS, blank=True)


class Comment(models.Model):
    GRADE = (('0', 'disgusting'), ('1', 'awful'), ('2', 'really bad'), ('3', 'bad'), ('4', 'worse than expected'),
             ('5', 'okey'), ('6', 'better than expected'), ('7', 'good'), ('8', 'really good'), ('9', 'great'),
             ('10', 'incredible'))
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    grade = models.CharField(choices=GRADE, max_length=30)
