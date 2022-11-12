from django import forms
from hotels.models import Feedback


class CreateFeedback(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['booking', 'author', 'text', 'rate']