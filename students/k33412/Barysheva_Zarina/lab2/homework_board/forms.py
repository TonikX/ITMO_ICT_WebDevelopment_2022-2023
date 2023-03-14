from django.forms import ModelForm
from .models import DoneTask, User, Assignment

class DoneTaskForm(ModelForm):
    class Meta:
        model = DoneTask
        fields = ['text']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'surname', 'name', 'password']

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject_id', 'start_date', 'end_date', 'text', 'fine']
