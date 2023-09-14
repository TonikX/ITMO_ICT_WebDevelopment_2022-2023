import datetime

from django.db import models
from datetime import datetime

from users_app.models import User


class Conference(models.Model):
    name = models.TextField()
    topics = models.TextField(default=None)
    location = models.TextField(default=None)
    start_at = models.DateTimeField(default=datetime.now())
    end_at = models.DateTimeField(default=datetime.now())
    rules = models.TextField(default=None)

    def __str__(self):
        return self.name


class ConfRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"ConfRegistration {self.user} \"{self.conference}\""


class ConfComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return f"Comment {self.user} \"{self.conference}\" text={{ {self.text} }} rate={self.rate} conf_dates={{ {self.conference.start_at} - {self.conference.end_at} }}"
