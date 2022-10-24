from django.forms import ModelForm
from .models import Comment

class MakeComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['num_race', 'type_comment', 'rate', 'username', 'text']