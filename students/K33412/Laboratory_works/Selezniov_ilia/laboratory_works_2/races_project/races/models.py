from django.db import models
from datetime import datetime
import django
from django.contrib.auth.models import User

class Driver(models.Model):
	COUNTRIES = (
		('ES', 'Spain'),
		('IT', 'Italy'),
		('FR', 'France'),
		('DE', 'Deutschland'))

	RACER_TYPES = (
		('Drag', 'Drag racer'),
		('Sport', 'Sports car racer'),
		('Off', 'Off-road racer'))
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	surname = models.CharField(max_length=200, null=True)
	team = models.CharField(max_length=200, null=True)
	country = models.CharField(max_length=2, choices=COUNTRIES, null=True)
	driver_class = models.CharField(max_length=5, choices=RACER_TYPES, null=True)
	age = models.IntegerField(null=True)
	experience = models.IntegerField(null=True)

	def __str__(self):
		return '{} {}'.format(self.name, self.surname)

class Car(models.Model):
	CAR_TYPES = (
		('Drag', 'Drag'),
		('Sport', 'Sportscar'),
		('Off', 'Off-road'))
	car_model = models.CharField(max_length=200, null=True)
	number = models.IntegerField(null=True, unique=True)
	car_class = models.CharField(max_length=200, choices=CAR_TYPES, null=True)
	speed = models.IntegerField(null=True)
	weight = models.FloatField(null=True)
	length = models.FloatField(null=True)
	mileage = models.IntegerField(null=True)
	driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.car_model, self.number)

class Race(models.Model):
	RACE_TYPES = (
		('Drag', 'Drag racing'),
		('Sport', 'Sports car racing'),
		('Off', 'Off-road racing'))
	race_date = models.DateField(null=True)
	race_type = models.CharField(max_length=200, choices=RACE_TYPES, null=True)
	length = models.IntegerField(null=True)
	name = models.CharField(max_length=200, null=True)
	registrations = models.ManyToManyField(Driver, through='Registration', blank=True)
	time = models.TimeField(null=True, blank=True)

	def __str__(self):
		return '{} - {}'.format(self.name, self.id)


class Comment(models.Model):
	TYPE = (
		('Cooperation', 'Cooperation'),
		('Race', 'Race'),
		('Other', 'Other'))
	RATE = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'))
	race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
	driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
	text = models.TextField()
	com_type = models.CharField(max_length=11, choices=TYPE, null=True)
	grade = models.CharField(max_length=1, choices=RATE, null=True)
	def __str__(self):
		return '{}: {}'.format(self.driver, self.com_type)


class Registration(models.Model):
	race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
	driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
	reg_date = models.DateField(null=True, blank=True, default = django.utils.timezone.now)
	place = models.IntegerField(null=True, blank=True)
	car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '{} {}'.format(self.race, self.driver)



 



