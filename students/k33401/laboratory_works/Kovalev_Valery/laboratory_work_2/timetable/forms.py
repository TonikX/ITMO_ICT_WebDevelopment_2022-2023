from django.contrib.auth.forms import UserCreationForm
from django import forms

from timetable.models import Teacher, Student, User

ROLES = [
    ('teacher', 'Teacher'),
    ('student', 'Student'),
]


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TeacherForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = ["subject"]

    def save(self, commit=True):
        teacher = super(TeacherForm, self).save(commit=False)
        teacher.user = self.user
        teacher.user.with_additional_info = True
        if commit:
            teacher.user.save()
            teacher.save()
        return teacher


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(StudentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ["student_group"]

    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        student.user = self.user
        student.user.with_additional_info = True
        if commit:
            student.user.save()
            student.save()
        return student


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        required=True,
        choices=ROLES
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        print("ROLE", self.cleaned_data["role"])
        if self.cleaned_data["role"][0] == "teacher":
            user.is_teacher = True
        if self.cleaned_data["role"][0] == "student":
            user.is_student = True
        if commit:
            user.save()
        return user
