from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class Conference(models.Model):
    name = models.CharField(max_length=300)
    topics = models.ManyToManyField('Tag', blank=True, related_name='confs')
    place = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True)
    participants = models.ManyToManyField('Participant')
    conf_description = models.CharField(max_length=1000)
    place_description = models.CharField(max_length=150)
    terms_of_participation = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('conf_registration_url', kwargs={'name': self.name})

    def __str__(self):
        return self.name


class Participant(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Performance(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_recommended = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} by {self.author.first_name} {self.author.last_name}"


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('tags_detail_url', kwargs={'title': self.title})

    def __str__(self):
        return self.title
