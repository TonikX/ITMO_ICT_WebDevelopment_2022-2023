from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Teacher, Student, User, Homework, StudentGroup, HomeworkAnswer, TeacherAnswerOnHomework

ROLES = [
    ('teacher', 'Teacher'),
    ('student', 'Student'),
]

groups = [(group.pk, group) for group in StudentGroup.objects.all()]


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


class StudentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(StudentForm, self).__init__(*args, **kwargs)

    student_group = forms.ChoiceField(required=True, choices=groups)

    def save(self, commit=True):
        student = Student()
        student.user = self.user
        student.user.with_additional_info = True
        student.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
        if commit:
            student.user.save()
            student.save()
        return student


class TeacherAnswerOnHomeworkForm(forms.ModelForm):
    class Meta:
        model = TeacherAnswerOnHomework
        fields = ["points", "message"]

    def __init__(self, *args, **kwargs):
        self.homework_answer = kwargs.pop('homework_answer', None)
        self.user = kwargs.pop('user', None)
        super(TeacherAnswerOnHomeworkForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        teacher_homework_answer = super(TeacherAnswerOnHomeworkForm, self).save(commit=False)
        teacher_homework_answer.homework_answer = self.homework_answer
        teacher_homework_answer.teacher = self.user.teacher
        if commit:
            teacher_homework_answer.save()
        return teacher_homework_answer


class HomeworkAnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.homework = kwargs.pop('homework', None)
        self.student = kwargs.pop('student', None)
        super(HomeworkAnswerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HomeworkAnswer
        fields = ["answer"]

    answer = forms.CharField(label='message', max_length=180)

    def save(self, commit=True):
        homework_answer = super(HomeworkAnswerForm, self).save(commit=False)
        homework_answer.homework = self.homework
        homework_answer.student = self.student
        if commit:
            homework_answer.save()
        return homework_answer


class HomeworkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(HomeworkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Homework
        fields = ["task_description", "start_date", "end_date", "max_points", "fine_info"]
        widgets = {
            "start_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            "end_date": forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    student_group = forms.ChoiceField(required=True, choices=groups)

    def save(self, commit=True):
        homework = super(HomeworkForm, self).save(commit=False)
        homework.student_group = StudentGroup.objects.get(pk=self.cleaned_data["student_group"])
        homework.teacher = Teacher.objects.get(user=self.user)
        homework.subject = homework.teacher.subject
        if commit:
            homework.save()
        return homework