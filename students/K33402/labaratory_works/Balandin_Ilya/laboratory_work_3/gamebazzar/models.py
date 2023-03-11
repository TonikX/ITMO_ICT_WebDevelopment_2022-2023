from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=512)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.game} for {self.platform}"


class Sell(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username} - {self.product}"
