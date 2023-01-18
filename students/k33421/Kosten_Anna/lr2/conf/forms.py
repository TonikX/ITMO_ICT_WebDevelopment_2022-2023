from .models import Comment, RegisteredSpeech
from django.forms import ModelForm, HiddenInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ("date",)
        required_css_class = 'form-required'
        widgets = {'conference': HiddenInput, 'user': HiddenInput}


class SpeechRegisterForm(ModelForm):
    class Meta:
        model = RegisteredSpeech
        exclude = ("results",)
        widgets = {'conference': HiddenInput, 'user': HiddenInput}
