from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id_guest', 'id_room', 'rating_c', 'review_c', 'check_in', 'check_out')
