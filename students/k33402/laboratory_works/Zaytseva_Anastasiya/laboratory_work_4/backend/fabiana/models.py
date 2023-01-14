from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FabianaUser(AbstractUser):
    email = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['email']


class Order(models.Model):
    user = models.ForeignKey(FabianaUser, on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(FabianaUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    purchased = models.BooleanField(blank=True,default=False)
