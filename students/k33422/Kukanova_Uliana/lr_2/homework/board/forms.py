from django import forms
from django.contrib.auth.forms import UserCreationForm
from board.models import Student, Assignment


class NewStudent(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'first_name', 'last_name']


class NewSubmission(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['homework', 'submission']
