from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Форма для создания пользователя
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "first_name", "last_name")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user
