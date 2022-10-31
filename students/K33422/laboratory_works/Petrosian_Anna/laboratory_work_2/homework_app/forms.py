from django import forms
from homework_app.models import Assignment


class AssignmentForm(forms.ModelForm):
    submission = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Assignment
        fields = ['submission']