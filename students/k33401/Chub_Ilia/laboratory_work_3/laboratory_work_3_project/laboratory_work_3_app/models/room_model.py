from django.db import models
from .book_instance_model import BookInstanceModel


class RoomModel(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    books = models.ManyToManyField(BookInstanceModel)
