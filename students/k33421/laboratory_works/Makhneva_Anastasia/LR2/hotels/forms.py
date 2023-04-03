from .models import Comment, Reservation
from django.forms import ModelForm, HiddenInput, DateInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        required_css_class = 'form-required'
        # widgets = {'reservation': HiddenInput}


class DateInput(DateInput):
    input_type = 'date'


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ("status",)
        widgets = {
            'room': HiddenInput,
            'guest': HiddenInput,
            'date_check_in': DateInput(),
            'date_check_out': DateInput(),
        }
