from django import forms
from .models import TaskCompletion


class SolutionForm(forms.ModelForm):
    class Meta:
        model = TaskCompletion
        fields = ['answer']
        widgets = {
            'answer': forms.Textarea(attrs={'maxlength': 500, 'cols': 44, 'required': 'true'}),
        }

    def __init__(self, task, user, subject, task_text, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)
        self.homework = task
        self.student = user
        self.subject = subject
        self.task_text = task_text

    def save(self, commit=True):
        instance = super(SolutionForm, self).save(commit=False)
        if not instance.homework_id:
            instance.homework = self.homework
            instance.student = self.student
            instance.subject = self.subject
            instance.task_text = self.task_text
        if commit:
            instance.save()
        return instance