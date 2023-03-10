from django import forms

from work_space.models import CreateTask, AnswerTask


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = CreateTask
        fields = ['subject', 'task', 'sanctions', 'data_finish']



class AnswerTaskForm(forms.ModelForm):

    class Meta:
        model = AnswerTask
        fields = ['answer', 'task']
