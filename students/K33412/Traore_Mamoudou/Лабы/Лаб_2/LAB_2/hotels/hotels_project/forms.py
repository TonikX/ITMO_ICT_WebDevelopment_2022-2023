from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking, Review
from datetime import date


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'passport', 'phone_number')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'},
                                          format='d-%m-%Y')
        }

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email is already in use. Please enter a different one.')
        return email

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class CreateBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('user', 'room', 'date_in', 'date_out')
        widgets = {
            'date_in': forms.DateInput(attrs={'type': 'date'},
                                       format='d-%m-%Y'),
            'date_out': forms.DateInput(attrs={'type': 'date'},
                                        format='d-%m-%Y'),
        }

    def __init__(self, *args, **kwargs):
        super(CreateBookingForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        date_in = cleaned_data.get("date_in")
        date_out = cleaned_data.get("date_out")
        today = date.today()

        if date_out < date_in:
            raise forms.ValidationError("'Date in' shouldn't be greater than 'Date out'")

        if date_in < today:
            raise forms.ValidationError("Can't book a room in the past")


class CreateReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('user', 'hotel', 'room', 'rating', 'date_in', 'date_out', 'body')
        widgets = {
            'date_in': forms.DateInput(attrs={'type': 'date'},
                                       format='d-%m-%Y'),
            'date_out': forms.DateInput(attrs={'type': 'date'},
                                        format='d-%m-%Y'),
            'body': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['room'].disabled = True
        self.fields['hotel'].disabled = True