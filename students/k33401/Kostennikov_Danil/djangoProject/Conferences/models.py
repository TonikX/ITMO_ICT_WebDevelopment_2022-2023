from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Сonference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=300)
    place_description = models.TextField()
    descriptions = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    conditions = models.TextField()

    def get_absolute_url(self):
        return reverse('get_conference_by_id', kwargs={'id': self.id})

    def get_absolute_apply_url(self):
        return reverse('conference_apply', kwargs={'id': self.id})

    def get_absolute_comment_url(self):
        return reverse('create_comment', kwargs={'id': self.id})

class User(AbstractUser):
    pass

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    rank = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)


class User_confirence(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)
