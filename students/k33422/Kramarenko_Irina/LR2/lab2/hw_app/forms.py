from django import forms
from .models import StudentHomework, Student


class UploadHW(forms.ModelForm):
    class Meta:
        model = StudentHomework
        fields = [
            "student_id",
            "homework_id",
            "text",
        ]


class RegUser(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "birthdate",
        ]