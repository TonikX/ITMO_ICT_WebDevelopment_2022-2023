from django.contrib.auth.forms import UserCreationForm
from django import forms

from timetable.models import Teacher, Student, User, Homework, StudentGroup, HomeworkAnswer

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


class TeacherAnswerOnHomework(forms.Form):
    def __init__(self, *args, **kwargs):
        points = kwargs.pop('points', None)
        homework_answer = kwargs.pop('homework_answer', None)
        message = kwargs.pop('message', None)
        super(TeacherAnswerOnHomework, self).__init__(*args, **kwargs)
        if points:
            self.fields['points'].widget = forms.NumberInput(attrs={'value': points})
        if homework_answer:
            self.fields["homework_answer_id"].widget = forms.HiddenInput(attrs={'value': homework_answer.pk})
        if message:
            self.fields["message"].widget = forms.TextInput(attrs={'value': message})

    homework_answer_id = forms.IntegerField()
    points = forms.IntegerField(label='points', min_value=0, max_value=15)
    message = forms.CharField(label='message', max_length=180)


class MakeHomeworkForm(forms.Form):
    def __init__(self, *args, **kwargs):
        answer = kwargs.pop('answer', None)
        homework = kwargs.pop('homework', None)
        super(MakeHomeworkForm, self).__init__(*args, **kwargs)
        if homework:
            self.fields["homework_id"].widget = forms.HiddenInput(attrs={'value': homework.pk})
        if answer:
            self.fields["answer"].widget = forms.TextInput(attrs={'value': answer})

    homework_id = forms.IntegerField()
    answer = forms.CharField(label='message', max_length=180)


class CreateHomeworkForm(forms.ModelForm):
    groups = [(group.pk, f"{group.character}{group.number}") for group in StudentGroup.objects.all()]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateHomeworkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Homework
        fields = ["task_description", "start_date", "end_date", "max_points"]
        widgets = {
            "start_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            "end_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    student_group = forms.ChoiceField(required=True, choices=groups)

    def save(self, commit=True):
        homework = super(CreateHomeworkForm, self).save(commit=False)
        print("DATA", self.cleaned_data)
        homework.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
        homework.teacher = Teacher.objects.get(user=self.user)
        if commit:
            homework.save()
        return homework


class StudentForm(forms.ModelForm):
    groups = [(group.pk, f"{group.character}{group.number}") for group in StudentGroup.objects.all()]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(StudentForm, self).__init__(*args, **kwargs)

    student_group = forms.ChoiceField(required=True, choices=groups)

    class Meta:
        model = Student
        fields = ["birthdate"]
        widgets = {
            "birthdate": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        student.user = self.user
        student.user.with_additional_info = True
        student.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
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
        if self.cleaned_data["role"] == "teacher":
            user.is_teacher = True
        if self.cleaned_data["role"] == "student":
            user.is_student = True
        if commit:
            user.save()
        return user
