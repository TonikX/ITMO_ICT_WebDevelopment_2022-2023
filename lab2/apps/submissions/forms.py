from django import forms

from apps.submissions.models import Submission


class SubmissionCreationForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('content',)
