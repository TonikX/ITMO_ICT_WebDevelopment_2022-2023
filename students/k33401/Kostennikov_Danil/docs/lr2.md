# Lab 2

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

* models.py

```python
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Сonference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=300)
    place_description = models.TextField()
    descriptions = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    conditions = models.TextField()

    def get_absolute_url(self):
        return reverse('get_conference_by_id', kwargs={'id': self.id})

    def get_absolute_apply_url(self):
        return reverse('conference_apply', kwargs={'id': self.id})

    def get_absolute_comment_url(self):
        return reverse('create_comment', kwargs={'id': self.id})

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True,max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    rank = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)


class User_confirence(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Сonference, on_delete=models.CASCADE)

```


* view.py

```python
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import *

from .forms import RegistrUser, LoginUser, ConferenceApply, CreateComment
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


class Reg_user(CreateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'password'
    ]
    template_name = "reg_user.html"
    success_url = reverse_lazy('get_all_conferences')

def conference_apply(request, id):
    form = ConferenceApply(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email,password=password).first()
        if not user:
            message = "Wrong email or password, or user is not registered"
            return render(request, 'conference_apply.html', context={"form": form, "message": message})

        conference = Сonference.objects.get(id=id)
        user_conf = User_confirence.objects.filter(user_id=user,conference_id=conference).exists()
        if user_conf:
            message = "You have alreade applied"
            return render(request, 'conference_apply.html', context={"form": form, "message": message})
        User_confirence.objects.create(user_id=user, conference_id=conference)
        message = "Success"
        return render(request, 'conference_apply.html', context={"form": form, "message": message})
    return render(request, 'conference_apply.html', context={"form": form})

def get_conferences(request):
    conferences = Сonference.objects.all()
    return render(request, 'conferences.html', context={'conferences': conferences})


def get_conference_by_id(request, id):
    conference = Сonference.objects.get(id=id)
    users_conf = User_confirence.objects.filter(conference_id=id)
    coments = Comment.objects.filter(conference_id=id)
    return render(request, 'conference.html', context={'conference': conference, 'users_conf': users_conf,
                                                       'coments': coments})

def applies(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email, password=password)
        if not user:
            return False
        return redirect(f"/applies/{email}")
    except:
        return render(request, "applies.html")

def user_applies(request, email):
    user = User.objects.get(email=email)
    user_conf = User_confirence.objects.filter(user_id=user)
    return render(request, 'user_applies.html', context={"user_conf": user_conf})

def delete_apply(request, email,id):
    try:
        User_confirence.objects.get(id=id).delete()
        return redirect(f"/applies/{email}")
    except:
        return redirect(f"/applies/{email}")

def create_comment(request,id):
    form = CreateComment(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email,password=password).first()
        if not user:
            message = "Wrong email or password, or user is not registered"
            return render(request, 'create_comment.html', context={"form": form, "message": message})

        conference = Сonference.objects.get(id=id)
        comment = form.cleaned_data['comment']
        rank = form.cleaned_data['rank']

        Comment.objects.create(user_id=user,conference_id=conference, comment=comment,rank=rank)
        return redirect(f"/conference/{id}")

    return render(request, 'create_comment.html', context={"form": form})
```

* forms.py

```python
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from Conferences.models import User, Сonference, Comment


class RegistrUser(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]



class ConferenceApply(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = Сonference
        fields = ["email", "password"]

class CreateComment(forms.ModelForm):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=60)

    class Meta:
        model = Comment
        fields = ["email", "password", "comment", "rank"]
```

* ursl.py

```python
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('conferences/', get_conferences, name='get_all_conferences'),
    path('conference/<int:id>/', get_conference_by_id, name='get_conference_by_id'),
    path("registration/", views.Reg_user.as_view(), name="register"),
    path("conference_apply/<int:id>/", views.conference_apply, name="conference_apply"),
    path("applies", views.applies, name='applies'),
    path("applies/<str:email>/", views.user_applies, name='user_applies'),
    path("delete_apply/<str:email>/<int:id>", views.delete_apply, name='delete_apply'),
    path("create_comment/<int:id>", views.create_comment, name='create_comment')



]
```