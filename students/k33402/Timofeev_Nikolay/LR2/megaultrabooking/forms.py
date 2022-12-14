from django.forms import ModelForm, BooleanField, DateField, Form
from django.forms.widgets import DateInput, SelectDateWidget

from .models import User, Hotel, Room, Review, Booking


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'owner', 'address', 'description']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'price', 'facilities']


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['ts_start', 'ts_end']
        widgets = {
            'ts_start': DateInput(attrs={'type': 'date'}),
            'ts_end': DateInput(attrs={'type': 'date'}),
        }


class EditBookingForm(Form):
    cancel = BooleanField(required=False)
    ts_start = DateField(required=False, widget=DateInput(attrs={'type': 'date'}))
    ts_end = DateField(required=False, widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        fields = ['cancel', 'ts_start', 'ts_end']
