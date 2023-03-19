import datetime

from django.db import models
from .reader_model import ReaderModel
from .book_instance_model import BookInstanceModel


def get_end_date():
    return datetime.date.today() + datetime.timedelta(days=14)


class ReaderBookModel(models.Model):
    reader = models.ForeignKey(ReaderModel, on_delete=models.CASCADE)
    book_instance = models.ForeignKey(BookInstanceModel, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=get_end_date)
