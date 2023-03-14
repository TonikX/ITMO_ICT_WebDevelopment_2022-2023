from django.db import models
from .book_model import BookModel
from uuid import uuid4


class BookInstanceModel(models.Model):
    statuses = (
        ('g', 'good'),
        ('b', 'bad'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    section = models.IntegerField()
    status = models.CharField(max_length=1, choices=statuses)
