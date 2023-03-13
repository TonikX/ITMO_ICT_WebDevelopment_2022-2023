from django.db import models


class BookModel(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    year_of_publishing = models.IntegerField()
