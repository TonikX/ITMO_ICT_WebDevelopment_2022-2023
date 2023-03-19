from . import *


class SubmitHomeworkTaskModel(Model):
    uuid = UUIDField(primary_key=True, default=uuid4, editable=False)
    student_id = ForeignKey(StudentModel, on_delete=CASCADE)
    homework_uuid = ForeignKey(HomeworkModel, on_delete=CASCADE)
    answer = CharField(max_length=1000, blank=True, null=False)
