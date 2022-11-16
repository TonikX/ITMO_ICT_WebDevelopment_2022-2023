from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Reservation, Comment


User = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ReserveForm(forms.ModelForm):
    date_start = forms.DateTimeField(label='Дата заезда', widget=forms.DateInput(attrs={'type': 'date'}))
    date_end = forms.DateTimeField(label='Дата выезда', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = ('date_start', 'date_end')


class InputCommentForm(forms.ModelForm):
    reservation = forms.ModelChoiceField(label='Период проживания', empty_label='Нет бронирований', queryset=None, required=False)
    rating = forms.IntegerField(label='Оценка', min_value=0, max_value=10)
    body = forms.TextInput(attrs={'size': 10, 'title': None})

    def __init__(self, user, room, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reservation'].queryset = Reservation.objects.filter(user=user).filter(room=room)

    class Meta:
        model = Comment
        fields = ('reservation', 'rating', 'body')
