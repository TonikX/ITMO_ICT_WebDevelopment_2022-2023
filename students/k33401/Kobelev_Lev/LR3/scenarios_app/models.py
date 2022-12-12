from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class GameSystem(models.Model):
    name = models.CharField(max_length=31, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)


class Scenario(models.Model):
    name = models.CharField(max_length=31)
    short_description = models.CharField(max_length=127)
    full_description = models.TextField()
    game_system = models.ForeignKey(GameSystem, on_delete=models.SET_NULL, null=True)
    is_completed = models.BooleanField()
    is_age_restricted = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name="likes")


class Review(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
