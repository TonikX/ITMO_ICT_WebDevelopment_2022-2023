from . import *
from .submit_homework_task_model import SubmitHomeworkTaskModel


class EducationalJournalModel(Model):
    submit_homework_task_uuid = ForeignKey(SubmitHomeworkTaskModel, on_delete=CASCADE)
    mark = IntegerField("Mark")
