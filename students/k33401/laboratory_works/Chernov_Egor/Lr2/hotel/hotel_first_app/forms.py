from django import forms
from .models import Comment
from .models import Registration


class ReserveForm(forms.ModelForm):
    name_hotel = forms.CharField(max_length=100)
    room_number = forms.IntegerField()

    class Meta:
        model = Registration
        fields = ('name_hotel', 'room_number', 'id_employee', 'id_guest', 'id_room', 'status_reg',
                  'status_pay', 'check_in', 'check_out', 'booking')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id_guest', 'id_room', 'username', 'rating_c', 'review_c', 'check_in', 'check_out')
