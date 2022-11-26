from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(label="Имя")
    surname = forms.CharField(label="Фамилия")

    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'surname']

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})