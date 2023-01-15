from django.forms import ModelForm
from .models import Comment

class MakeComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['num_race', 'comment_type', 'rate', 'username', 'text']