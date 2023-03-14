from django.db import models
from .reader_model import ReaderModel
from .user_model import UserModel


class UserReaderModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)
    reader = models.ForeignKey(ReaderModel, on_delete=models.CASCADE)
