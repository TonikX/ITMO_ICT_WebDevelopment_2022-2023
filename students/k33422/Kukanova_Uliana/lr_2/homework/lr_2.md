Web-программирование 2023
========================
Куканова Ульяна K33422
-------------------------
Лабораторная работа 2

- models.py 
```python
  from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Student(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Homework(models.Model):
    name = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=30, blank=False)
    teacher = models.CharField(max_length=30, blank=False)
    post_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)
    task = models.CharField(max_length=1000)
    students = models.ManyToManyField('Student', through='Assignment')

    def __str__(self):
        return self.name


class Assignment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    homework = models.ForeignKey('Homework', on_delete=models.CASCADE)
    submission = models.CharField(max_length=1000, blank=True)
    grade = models.CharField(default='none', max_length=5, blank=True)

    def __str__(self):
        return f'{self.homework.name} {self.student.last_name}'
```
- views.py 

```python
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from board.models import Student, Homework, Assignment
from board.forms import NewStudent, NewSubmission
# Create your views here.


def find_home(request):
    if request.user.is_authenticated:
        return redirect('/all_hw')
    else:
        return redirect('/login')


def register(request):
    form = NewStudent()
    if request.method == "POST":
        form = NewStudent(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    data = {'form': form}
    return render(request, 'register.html', data)


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/all_hw')

    data = {}
    return render(request, 'login.html', data)


def log_out(request):
    logout(request)
    return redirect('/login')


class AllHomework(ListView):
    model = Homework
    template_name = 'all_hw.html'


class OneHomework(DetailView):
    model = Homework
    template_name = 'hw.html'


class AddSubmission(CreateView):
    form_class = NewSubmission
    model = Assignment
    template_name = 'submit.html'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class OurGrades(ListView):
    model = Assignment
    template_name = 'our_grades.html'

```
- forms.py 
```python
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

```
- urls.py 
```python
from django.urls import path
from .views import *

urlpatterns = [
    path('', find_home, name='home'),
    path('register', register, name='register'),
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('all_hw', AllHomework.as_view()),
    path('hw/<int:pk>', OneHomework.as_view()),
    path('hw/<int:pk>/submit', AddSubmission.as_view(success_url="/all_hw")),
    path('our_grades', OurGrades.as_view()),
    ]
```
