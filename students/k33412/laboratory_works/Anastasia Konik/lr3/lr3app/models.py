from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    date = models.DateTimeField(null=False)
    short_description = models.CharField(max_length=200, null=False)
    full_description = models.CharField(max_length=1000, null=False)
    website = models.CharField(max_length=100, null=False)
    img_src = models.ImageField(max_length=1000, null=True, upload_to='images')

    def __str__(self):
        return self.title.__str__()


class User(AbstractUser):
    img_url = models.ImageField(max_length=1000, null=True, upload_to='images', default='default_user.png')
    email = models.CharField(max_length=30, null=False, unique=True)
    user_info = models.CharField(max_length=200, null=True)

    REQUIRED_FIELDS = ["img_url", "user_info", "email", "first_name", "last_name"]

    def __str__(self):
        return self.username.__str__()


class UserEnrolledEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")

    def __str__(self):
        return self.id.__str__()


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")
    text = models.CharField(max_length=1000, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, to_field="title")

    def __str__(self):
        return self.id.__str__()
