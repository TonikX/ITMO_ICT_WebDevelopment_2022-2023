from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participation_cond = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class PlannedConference(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    place = models.ForeignKey(
        Place, on_delete=models.SET_NULL, null=True, blank=True)
    themes = models.ManyToManyField(Theme)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.conference.name + ' | ' + self.place.name[:50] + ('...' if len(self.place.name) > 50 else '')

    class Meta:
        ordering = ['start_date']


class RegisteredConference(models.Model):
    conference = models.ForeignKey(PlannedConference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    results = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(PlannedConference, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(0, 11)], null=True, blank=True, default=None)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.first_name + ' | ' + self.text[:50] + ('...' if len(self.text) > 50 else '')

    class Meta:
        ordering = ['-date']
