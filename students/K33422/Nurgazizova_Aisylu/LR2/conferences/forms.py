from django import forms
from .models import *


class RegisterToConferenceForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['theme']
        exclude = ['user', 'conference', 'create_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': 15, 'cols': 70, 'class': 'form-control', 'placeholder': 'Type your comment...'}),
        }
        fields = ['text', 'rate']
        exclude = ['user', 'create_time']