# Create your models here.
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	REQUIRED_FIELDS = ["first_name", "last_name", "position", "working_days", "working_hours"]
	position = models.TextField()
	working_days = models.TextField()
	working_hours = models.TextField()


class Product(models.Model):
	image_name = models.TextField()
	name = models.TextField()
	price = models.IntegerField()
	quantity = models.IntegerField()


class SaleRecord(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
	datetime = models.DateTimeField(default=datetime.now, blank=True)
	quantity = models.IntegerField(default=1)
