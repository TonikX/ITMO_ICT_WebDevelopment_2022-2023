from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        User = get_user_model()
        model = User
        # fields name and surname I take from my AbstractUser class - Guest
        fields = ("username", "email", 'name', 'surname', "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
