# ЛАБОРАТОРНАЯ РАБОТА №2

## ОПИСАНИЕ ЗАДАНИЯ
# ВАРИАНТ 2

Доска домашних заданий.

О домашнем задании должна храниться следующая информация: предмет,
преподаватель, дата выдачи, период выполнения, текст задания, информация о штрафах.
Необходимо реализовать следующий функционал:

* Регистрация новых пользователей.
* Просмотр домашних заданий по всем дисциплинам (сроки выполнения,
описание задания).
* Сдача домашних заданий в текстовом виде.
* Администратор (учитель) должен иметь возможность поставить оценку за
задание средствами Django-admin.
* В клиентской части должна формироваться таблица, отображающая оценки
всех учеников класса.

## файлы с кодом
* model.py     
``` py
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver


class Homework(models.Model):
    homework_id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    task = models.CharField(max_length=300)
    subject = models.CharField(max_length=30, blank=False)
    begin_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)
    penalty = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #REQUIRED_FIELDS = ['self.user.first_name', 'self.user.last_name']
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Assignment(models.Model):
    assignment_id = models.IntegerField(blank=False, primary_key=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    grade = models.CharField(default='-', max_length=5, blank=True)
    submission = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.student.user.first_name} {self.student.user.last_name}:\
        {self.homework.name}\
        | {"graded" if self.grade != "-" else "submitted" if len(self.submission) else "in process"}'


@receiver(models.signals.post_save, sender=Homework)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        students = Student.objects.all()
        for student in students:
            duplicates = Assignment.objects.filter(student=student, homework=instance).all()
            if not len(duplicates):
                assignment = Assignment(student=student, homework=instance)
                assignment.save()

# Create your models here.
```
* views.py
``` py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from homework_app.models import Student, Homework, Assignment,User,Teacher
from homework_app.forms import AssignmentForm,StudentSignUpForm,TeacherSignUpForm,HomeworkForm
from homework_app.decorators import student_required,teacher_required
from django.http import HttpResponseRedirect
class StudentSignUpView(CreateView):
        
    model = User
    form_class = StudentSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
   
        user = form.save()
        login(self.request, user)
        return redirect('login')

class TearchSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
   
        user = form.save()
        login(self.request, user)
        return redirect('login')
@method_decorator(teacher_required, name='dispatch')

class HomeworkCreate(CreateView):
    model = Homework 
    form_class: HomeworkForm
    template_name = 'createhomework.html'
    fields = "__all__"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HomeworkForm()
        return context
    def form_valid(self, form):

        form.save()
        
        return redirect('homework_list')
    



def log_in(request):
    # if request.user.is_authenticated:
    #     return redirect('homework_list')
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('homework_list'))
        else:
            error_text = 'invalid credentials'

    return render(request, 'login.html', locals())


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
@teacher_required
def class_grades_list(request):
    context = {}
    students = Student.objects.all()
    context["students"] = students
    context["homeworks"] = Homework.objects.all()
    context["grades"] = {}
    assignments = Assignment.objects.all()
    for homework in context["homeworks"]:
        for assignment in assignments:
            if assignment.homework == homework and assignment.student.pk != 3:
                if not assignment.student.pk in context["grades"]:
                    context["grades"][assignment.student.pk] = []
                context["grades"][assignment.student.pk].append(
                    assignment.grade)

    return render(request, 'class_grades.html', context)

@method_decorator(login_required, name='dispatch')

class HomeworkList(ListView):
 
    model = Homework
    template_name = 'homework_list.html'

@method_decorator(login_required, name='dispatch')
class HomeworkDetail(DetailView):
    model = Homework
    template_name = 'homework_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AssignmentForm()
        return context

@method_decorator(student_required, name='dispatch')   

class AssignmentView(ListView):
    model = Assignment
    template_name = 'studentgrade.html'

    def get_queryset(self):
        studentt=Student.objects.get(user=self.request.user)
        return Assignment.objects.filter(student=studentt)


@login_required
def hand_in(request, pk):
    homework = Homework.objects.get(pk=pk)
    studentt = Student.objects.get(user=request.user)
    assignment = Assignment.objects.get(student=studentt,homework=homework)
    form = AssignmentForm(request.POST,instance=assignment)
    if form.is_valid():
        form.save()

        return redirect(reverse('homework_list'))

```

* formes.py
``` py
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
```
* urls.py
``` py
from django.urls import path

from homework_app import views

urlpatterns = [
    path('student/register/', views.StudentSignUpView.as_view(), name='register'),
    path('teacher/register/', views.TearchSignUpView.as_view(), name='Tregister'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('class_grades/', views.class_grades_list, name='class_grades'),
    path('homework/create/', views.HomeworkCreate.as_view(),name='homework_create'),
    path('homeworks/', views.HomeworkList.as_view(),name='homework_list'),
    path('homework/<int:pk>', views.HomeworkDetail.as_view(),
         name='homework_detail'),
    path('handin/<int:pk>', views.hand_in, name='handin'),
    path('mygrade/', views.AssignmentView.as_view(),name='mygrade'),
]
```

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
