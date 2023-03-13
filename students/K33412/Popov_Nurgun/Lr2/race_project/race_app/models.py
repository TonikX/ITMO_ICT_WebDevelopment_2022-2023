from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Racer(models.Model):
    DRIVER_CLASSES = (
        ('Circuit', 'Circuit racer'),
        ('Rally', 'Rally racer'),
        ('Endurance', 'Rally racer'),
        ('Drag', 'Drag racer')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)
    team = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    driver_class = models.CharField(max_length=100, choices=DRIVER_CLASSES, null=True)
    experience = models.IntegerField(null=True)
    decription = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Car(models.Model):
    CAR_TYPES = (
        ('Circuit', 'Circuit car'),
        ('Rally', 'Rally car'),
        ('Endurance', 'Rally car'),
        ('Drag', 'Drag car')
    )
    car_model = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True, unique=True)
    car_type = models.CharField(max_length=100, choices=CAR_TYPES, null=True)
    speed = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    racer = models.ForeignKey(Racer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{}'.format(self.car_model)


class Race(models.Model):
    RACE_TYPES = (
        ('Circuit', 'Circuit race'),
        ('Rally', 'Rally race'),
        ('Endurance', 'Endurance race'),
        ('Drag', 'Drag race')
    )
    name = models.CharField(max_length=100, null=True)
    race_date = models.DateField(null=True)
    race_type = models.CharField(max_length=100, choices=RACE_TYPES, null=True)
    length = models.IntegerField(null=True)
    registrations = models.ManyToManyField(Racer, through='Registration', blank=True)

    def __str__(self):
        return '{}'.format(self.name)



class Registration(models.Model):
    race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
    racer = models.ForeignKey(Racer, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    place = models.IntegerField(null=True, blank=True)

class Comment(models.Model):
    RATE = (
               ('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'),
               ('6', '6'),
               ('7', '7'),
               ('8', '8'),
               ('9', '9'),
               ('10', '10'),

    )
    COMMENT_TYPE = (
        ('Вопрос о сотрудничестве', 'Cooperation'),
        ('Вопрос о гонках', 'About race'),
        ('Иное', 'Other')
    )

    race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
    racer = models.ForeignKey(Racer, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    comment_type = models.CharField(max_length=100, choices=COMMENT_TYPE, null=True)
    rate = models.CharField(max_length=100, choices=RATE, null=True)
