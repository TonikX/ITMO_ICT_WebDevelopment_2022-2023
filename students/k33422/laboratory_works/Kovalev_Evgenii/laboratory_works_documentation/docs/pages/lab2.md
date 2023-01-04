# Лабораторная работа №2

### Вариант 5. 
**Список научных конференций**

Необходимо реализовать следующий функционал:

- Регистрация новых пользователей.
- Просмотр конференций и регистрацию авторов для выступлений.
Пользователь должен иметь возможность редактирования и удаления своих
регистраций.
- Написание отзывов к конференциям. При добавлении комментариев,
должны сохраняться даты конференции, текст комментария, рейтинг (1-10),
информация о комментаторе.
- Администратор должен иметь возможность указания результатов
выступления (рекомендован к публикации или нет) средствами Django-
admin. 
- В клиентской части должна формироваться таблица, отображающая всех
участников по конференциям.

### Реализация 

* `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    # фамилия
    surname = models.CharField(max_length=30)
    # отчество
    lastname = models.CharField(max_length=30)
    passport = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.username


class Conference(models.Model):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 10)])
    text = models.CharField(max_length=400, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
```
* `views.py`
````python
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, CreateView, DeleteView, DetailView

from django.shortcuts import render, redirect

from .models import *
from .forms import *


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):

        print(request.POST)
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            print('valid')
            user = form.get_user()
            login(request, user)
            return redirect('conflist_route')
        else:
            print('not valid')
            messages.error(request, 'Указаны неверные данные')

        return redirect('login_route')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('conflist_route')
        else:
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_route')


class SignupView(FormView):
    form_class = UserRegisterForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, 'Успешная регистрация')
            return redirect('login_route')
        else:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request, 'Пользователь с таким именем уже зарегистрирован')
            else:
                messages.error(request, 'Ошибка регистрации')

        return redirect('signup_route')


class ConferenceView(LoginRequiredMixin, ListView):
    model = Conference
    template_name = 'conference_list.html'
    context_object_name = 'conferences'

@login_required
def join_or_leave_conf_view(request, conf_pk, user_pk):
    conf = Conference.objects.get(pk=conf_pk)
    user = User.objects.get(pk=user_pk)

    if user in conf.members.all():
        conf.members.remove(user)
    else:
        conf.members.add(user)

    return redirect('conflist_route')


@login_required
def user_confs_view(request, username):
    all_confs = Conference.objects.all()
    user_confs = []

    for conf in all_confs:
        if request.user in conf.members.all():
            user_confs.append(conf)

    return render(request, 'user_confs.html', {'user_confs': user_confs})


class DetailConfView(LoginRequiredMixin, DetailView):
    model = Conference
    template_name = 'detail_conference.html'
    context_object_name = 'conf'
    pk_url_kwarg = 'conf_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conf_pk = self.kwargs['conf_pk']
        comments = Comment.objects.filter(conference__pk=conf_pk).order_by('-created')
        context['comments'] = comments
        return context


@login_required
def comment_view(request, conf_pk):
    user_obj = User.objects.get(pk=request.user.pk)
    conference = Conference.objects.get(pk=conf_pk)

    comment_text = request.POST['comment_text']

    if str(comment_text).isspace():
        messages.error(request, 'Комментарий не может быть пустым')
    else:
        comment_obj = Comment.objects.create(
            author=user_obj,
            conference=conference,
            rating=0,
            text=comment_text
        )

    return redirect('detail_conf_route', conf_pk=conf_pk)


@login_required
def remove_comment_view(request, conf_pk, comment_pk):
    comment_obj = Comment.objects.get(pk=comment_pk).delete()
    return redirect('detail_conf_route', conf_pk=conf_pk)


@login_required
def conf_members_view(request, conf_pk):
    conference = Conference.objects.get(pk=conf_pk)
    members = conference.members.all()
    context = {
        'members': members,
        'conf': conference
    }
    return render(request, 'conf_members.html', context)
````

* `forms.py`
```python
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'})),
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя'),
    surname = forms.CharField(label='Фамилия'),
    lastname = forms.CharField(label='Отчество'),
    password1 = forms.CharField(label='Пароль'),
    password2 = forms.CharField(label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ('username', 'surname', 'lastname', 'password1', 'password2')
```

* `urls.py`
```python
from django.urls import path

from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login_route'),
    path('signup', SignupView.as_view(), name='signup_route'),
    path('conflist', ConferenceView.as_view(), name='conflist_route'),

    path('logout', logout_view, name='logout_route'),
    path('join_conf/<int:conf_pk>/<int:user_pk>/', join_or_leave_conf_view, name='join_or_leave_conf_route'),
    path('user_confs/<str:username>/', user_confs_view, name='user_confs_route'),

    path('conf/<int:conf_pk>/', DetailConfView.as_view(), name='detail_conf_route'),

    path('comment/create/<int:conf_pk>/', comment_view, name='add_comment_route'),
    path('comment/delete/<int:conf_pk>/<int:comment_pk>/', remove_comment_view, name='remove_comment_route'),
    path('conf/<int:conf_pk>/members', conf_members_view, name='conf_members_route')
]
```