from django.forms import ModelForm
from .models import *


class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['race', 'car']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['race', 'text', 'comment_type', 'rate']

class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = '__all__'