from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    tel = models.CharField("Telephone", max_length=20, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']
    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField("title", max_length=30, null=False)
    description = models.CharField("description", max_length=200, null=True)
    price = models.FloatField("price", default=0)


class ProductsOfOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.IntegerField("amount",null= False)
    total_price = models.FloatField("total_price")


class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    status_types = (
        ('c', 'created'),
        ('i', 'Invalid'),

    )
    status = models.CharField('status',max_length=1,choices=status_types,default='c')
    products = models.ManyToManyField('Product',through='ProductsOfOrder')
