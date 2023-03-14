from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Conference(models.Model):
    name = models.CharField(max_length=300)
    topics = models.ManyToManyField('Tag', blank=True, related_name='confs')
    place = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True)
    participants = models.ManyToManyField('Participant', through='Performance')
    conf_description = models.CharField(max_length=1000)
    place_description = models.CharField(max_length=150)
    terms_of_participation = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('conf_registration_url', kwargs={'name': self.name})

    def get_absolute_reg_url(self):
        return reverse('registration_url', kwargs={'name': self.name})

    def __str__(self):
        return self.name


class Participant(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Performance(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    is_recommended = models.BooleanField(default=False)
    author = models.ForeignKey(Participant, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} by {self.author.first_name} {self.author.last_name} at {self.conference.name}"


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('tags_detail_url', kwargs={'title': self.title})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Participant, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.author.username}"
