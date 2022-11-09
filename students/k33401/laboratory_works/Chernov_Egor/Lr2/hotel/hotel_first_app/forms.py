from django import forms
from .models import Comment
from .models import Registration


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('id_reg', 'id_employee', 'id_guest', 'id_room', 'status_reg',
                  'status_pay', 'check_in', 'check_out', 'booking')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id_guest', 'id_room', 'username', 'rating_c', 'review_c', 'check_in', 'check_out')
