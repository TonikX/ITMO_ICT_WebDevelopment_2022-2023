from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Owner(AbstractUser):
	last_name = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30)
	date_of_birth = models.DateTimeField(null=True, blank=True)
	address = models.CharField(max_length=50, null=True)
	nationality = models.CharField(max_length=30, null=True)
	passport = models.CharField(max_length=30, null=True)

	def __str__(self):
		return "{} {}".format(self.last_name, self.first_name)


class Vehicle(models.Model):
	registration_number = models.CharField(max_length=15)
	manufacturer = models.CharField(max_length=20)
	model = models.CharField(max_length=20)
	color = models.CharField(max_length=30, null=True, blank=True)
	ownership = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Property')

	def __str__(self):
		property = Property.objects.filter(vehicle_id=self).order_by('start_date').last()
		return "{}'s {} {}".format(
			property.owner_id.first_name,
			self.manufacturer,
			self.model
		) if property else \
			"{} {}".format(self.manufacturer, self.model)


class Property(models.Model):
	owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return "{}'s {} ({} - {})".format(
			"{} {}".format(self.owner_id.last_name, self.owner_id.first_name),
			"{} {}".format(self.vehicle_id.manufacturer, self.vehicle_id.model),
			self.start_date.date(),
			self.end_date.date() if self.end_date else 'Present time'
		)


class License(models.Model):
	owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	license_number = models.CharField(max_length=10)
	issue_date = models.DateTimeField()

	def __str__(self):
		return "{}'s license no. {} (issued {})".format(
			self.owner_id.first_name,
			self.license_number,
			self.issue_date.date()
		)
