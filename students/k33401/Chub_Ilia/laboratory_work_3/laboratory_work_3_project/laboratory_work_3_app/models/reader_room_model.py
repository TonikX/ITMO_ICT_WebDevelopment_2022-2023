from django.db import models
from .reader_model import ReaderModel
from .room_model import RoomModel


class ReaderRoomModel(models.Model):
    reader = models.ForeignKey(ReaderModel, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
