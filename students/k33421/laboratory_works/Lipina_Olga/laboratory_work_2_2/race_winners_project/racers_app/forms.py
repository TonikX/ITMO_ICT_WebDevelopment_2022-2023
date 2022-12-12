from django.forms import ModelForm, EmailField
from .models import Comment, Racer


class MakeComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['num_race', 'type_comment', 'rate', 'text']


