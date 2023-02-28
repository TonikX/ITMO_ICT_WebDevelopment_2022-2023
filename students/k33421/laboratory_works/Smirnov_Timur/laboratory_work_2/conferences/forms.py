from .models import Comment, RegisteredConference
from django.forms import ModelForm, HiddenInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ("date",)
        required_css_class = 'form-required'
        widgets = {'conference': HiddenInput, 'user': HiddenInput}


class ConferenceRegisterForm(ModelForm):
    class Meta:
        model = RegisteredConference
        exclude = ("results",)
        widgets = {'conference': HiddenInput, 'user': HiddenInput}
