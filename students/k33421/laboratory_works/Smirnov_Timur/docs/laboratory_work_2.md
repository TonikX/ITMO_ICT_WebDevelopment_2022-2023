# Лабораторная работа №2

## Список научных коференций

Интерфейс описывает названия конференций, список тематик, место проведения,
период проведения, описание конференций, описание место проведения, условия участия.
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

## Модели

Описание моделей:

- Тема конференции
- Конференция
- Места проведения
- Запланированная конференция
- Зарегистрированные выступления
- Комментарии

`models.py`

```python
from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participation_cond = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class PlannedConference(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    place = models.ForeignKey(
        Place, on_delete=models.SET_NULL, null=True, blank=True)
    themes = models.ManyToManyField(Theme)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.conference.name + ' | ' + self.place.name[:50] + ('...' if len(self.place.name) > 50 else '')

    class Meta:
        ordering = ['start_date']


class RegisteredConference(models.Model):
    conference = models.ForeignKey(PlannedConference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    results = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(PlannedConference, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[(i, i) for i in range(0, 11)], null=True, blank=True, default=None)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.first_name + ' | ' + self.text[:50] + ('...' if len(self.text) > 50 else '')

    class Meta:
        ordering = ['-date']

```

## Конструкторы

`views.py`

```python
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Theme, PlannedConference, RegisteredConference, Comment
from .forms import CommentForm, ConferenceRegisterForm


class CustomLoginView(LoginView):
    template_name = 'conferences/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('conferences')


class RegisterPage(FormView):
    template_name = 'conferences/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('conferences')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('conferences')
        return super(RegisterPage, self).get(*args, **kwargs)


class ConferencesList(ListView):
    model = PlannedConference
    template_name = 'conferences/conferences_list.html'
    context_object_name = 'conferences'


def conference_detail(request, pk):
    conference = PlannedConference.objects.get(pk=pk)
    registers = RegisteredConference.objects.filter(
        conference__pk=pk, results=True)
    comments = Comment.objects.filter(conference__pk=pk)
    initial = {'conference': conference, 'user': request.user}
    comment_form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form. save()
        else:
            comment_form = c_form
    context = {'conference': conference,
               'comments': comments, 'comment_form': comment_form, 'registers': registers}
    return render(request, 'conferences/conference_detail.html', context)


class ThemesList(ListView):
    model = Theme
    template_name = 'conferences/themes_list.html'
    context_object_name = 'themes'


class ThemeDetail(DetailView):
    model = Theme
    context_object_name = 'theme'
    template_name = 'conferences/theme_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conferences"] = PlannedConference.objects.filter(
            themes__id=context['theme'].id)
        return context


@login_required
def conference_register_view(request, pk):
    conference = PlannedConference.objects.get(pk=pk)
    initial = {'conference': conference, 'user': request.user}
    form = ConferenceRegisterForm(initial=initial)
    if request.method == 'POST':
        c_form = ConferenceRegisterForm(request.POST)
        if c_form.is_valid():
            c_form. save()
            return redirect(f'/conference/{pk}')
        else:
            form = c_form
    context = {'conference': conference, 'form': form}
    return render(request, 'conferences/conference_register.html', context)


class RegisterList(LoginRequiredMixin, ListView):
    model = RegisteredConference
    template_name = 'conferences/registers.html'
    context_object_name = 'registers'


class DeleteRegisterView(LoginRequiredMixin, DeleteView):
    model = RegisteredConference
    context_object_name = 'register'
    success_url = reverse_lazy('my_registers')

```

## URLs

Описание путей:

- /conferences/ - Список конференций
- /conference/<int:pk>/ - Описание конкретной конференции
- /conference/<int:pk>/register/ - Регистрация на выступление
- /myregisters/ - Список моих регистраций
- /myregisters/delete/<int:pk>/ - Удаление регистрации на выступление
- /themes/ - Список тем конференций
- /themes/<int:pk>/ - Конференции по конкретной теме
- /login/ - Войти в аккаунт
- /logout/ - Выйти из аккаунта
- /register/ - Зарегистрироваться

`urls.py`

```python
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import ConferencesList, CustomLoginView, RegisterPage, ThemesList, ThemeDetail, conference_detail, conference_register_view, RegisterList, DeleteRegisterView

urlpatterns = [
    path('', ConferencesList.as_view(), name='conferences'),
    path('conference/<int:pk>', conference_detail,
         name='conference'),
    path('conference/<int:pk>/register',
         conference_register_view, name='conference_register'),
    path('myregisters',
         RegisterList.as_view(), name='my_registers'),
    path('myregisters/delete/<int:pk>',
         DeleteRegisterView.as_view(), name='register_delete'),
    path('themes', ThemesList.as_view(), name='themes'),
    path('themes/<int:pk>', ThemeDetail.as_view(), name='theme'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='conferences'), name='logout'),
    path('register', RegisterPage.as_view(), name='register'),
]
```
