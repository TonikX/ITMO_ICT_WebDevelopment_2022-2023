from django import forms
from .models import Tourist, Reservation, Comment
  
  
class SignupForm(forms.ModelForm):
    class Meta:
        model = Tourist
        help_texts = {
            'username': None,
        }
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'rating'
        ]
