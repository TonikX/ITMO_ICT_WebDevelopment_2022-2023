from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    tel = models.CharField("Telephone", max_length=20, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField("title", max_length=30, null=False)
    description = models.CharField("description", max_length=200, null=True)
    ISBM = models.CharField("ISBM", max_length=30, null=False)
    price = models.FloatField("price", default=0)


class Record(models.Model):
    RecordID = models.ForeignKey('RecordID', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField()
