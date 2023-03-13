from django.db import models
from .reader_model import ReaderModel
from .book_instance_model import BookInstanceModel


class ReaderBookModel(models.Model):
    reader = models.ForeignKey(ReaderModel, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInstanceModel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
