
from django.db import models

class Сonference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=300)
    place_description = models.TextField()
    descriptions = models.TextField()
    period = models.DurationField()
    conditions = models.TextField()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)


class User_confirence(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)
