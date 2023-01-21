#  Web-программирование 2 Лабараторная работа 2 Вариант
## Галиновский Роман К33402 2022-2023
Должна храниться следующая информация:
1. Предмет
2. Преподаватель
3. Дата выдачи
4. Период выполнения
5. Текст задания
6. Информация о штрафах

Необходимо реализовать следующий функционал:
- Регистрация новых пользователей
- Просмотре домашних заданий по всем дисциплинам, их сроки выполнения, а также описания задания
- Сдача домашних заданий в текстовом виде
- Учитель-администратор должен иметь возможность поставить оценку за задания средствами Django-admin
- В клиентской части должна формироваться таблица, отображающая оценки всех учеников класса

`models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TYPE_EX = (
        ('teacher', 'я учитель'),
        ('student', 'я студент'))
    status = models.CharField(max_length=10, null=True, blank=True, choices=TYPE_EX)
    group = models.CharField(max_length=10, null=True, blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=20)


class Homework(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    period = models.IntegerField(null=True, blank=True) 
    task = models.TextField(null=True, blank=True)
    fine_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title + '(' + self.teacher.first_name + ')' + ' @' + self.course.course_name


class StudentHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    mark = models.IntegerField(null=True, blank=True)
    done_task = models.TextField(null=True, blank=True)
    
```
`views.py`
```python
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import User, Course, Homework, StudentHomework
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.status == 'student':
                        return HttpResponseRedirect('/')
                    else:
                        return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class UserCreate(CreateView):
    model = User
    template_name = 'registration.html'

    fields = ['username', 'password', 'first_name', 'last_name', 'status', 'group']
    success_url = '/login/'

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(form.cleaned_data['password'])

        if self.object.status == 'teacher':
            self.object.is_staff = True
            self.object.is_superuser = True

        self.object.save()

        return HttpResponseRedirect('/login/')


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


class HomeworkList(ListView):
    model = Homework
    template_name = 'homeworks.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/login/')

        return super(HomeworkList, self).dispatch(request, *args, **kwargs)


class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_create.html'

    fields = ['title', 'course', 'teacher', 'start_date', 'period', 'task', 'fine_info']


class HomeworkUpload(CreateView):
    model = StudentHomework
    template_name = 'homework_upload.html'

    fields = ['homework', 'done_task']
    success_url = '/'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class HomeworkMark(DetailView, UpdateView):
    model = StudentHomework
    fields = ['mark']
    template_name = 'homework_mark.html'
    success_url = '/'


class StudentMarkList(ListView):
    model = Course
    template_name = 'student_mark.html'
```
`forms.py`
``` python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
```
`urls.py`
```python
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('user/list/', views.UserList.as_view()),
    path('', views.HomeworkList.as_view()),
    path('homework/create/', views.HomeworkCreate.as_view()),
    path('homework/upload/', views.HomeworkUpload.as_view()),
    path('homework/mark/<int:pk>', views.HomeworkMark.as_view()),
    path('student/mark/', views.StudentMarkList.as_view()),
    path('registration/', views.UserCreate.as_view()),
    path('login/', views.user_login),
    path('logout/', LogoutView.as_view()),
]
```


