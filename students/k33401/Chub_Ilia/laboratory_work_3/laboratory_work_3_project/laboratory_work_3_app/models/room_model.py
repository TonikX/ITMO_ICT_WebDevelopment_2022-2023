from django.db import models
from .book_instance_model import BookInstanceModel
from uuid import uuid4


class RoomModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    books = models.ManyToManyField(BookInstanceModel)
