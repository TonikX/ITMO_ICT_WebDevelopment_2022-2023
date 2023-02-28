from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError


from homework_app.models import (User,Student,Assignment,Teacher,Homework)

class AssignmentForm(forms.ModelForm):
    submission = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Assignment
        fields = ['submission']


class HomeworkForm(forms.ModelForm):
    
    class Meta:
        model = Homework
        fields = ['homework_id','name','task','subject','begin_date','deadline','penalty','teacher','students']

    
    def save(self):
        homework = super().save(commit=False) 
        homework.save()
        return homework   


class StudentSignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

class TeacherSignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        tearch = Teacher.objects.create(user=user)
        return user
