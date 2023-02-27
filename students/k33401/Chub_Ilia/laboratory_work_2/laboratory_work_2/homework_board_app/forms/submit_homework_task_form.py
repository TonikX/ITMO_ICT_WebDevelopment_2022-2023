from django.forms import Form, UUIDField, CharField
from ..models import SubmitHomeworkTaskModel


class SubmitHomeworkTaskForm(Form):
    homework_uuid = UUIDField()
    answer = CharField(label="Your answer", max_length=1000)

    class Meta:
        model = SubmitHomeworkTaskModel
        fields = ("homework_uuid", "answer")
