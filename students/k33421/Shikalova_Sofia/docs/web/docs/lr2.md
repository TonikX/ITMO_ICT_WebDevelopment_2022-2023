# Лабораторная работа №2 (6 вариант)

## Описание работы 

> **Табло победителей автогонок**
> 
> Табло должно отображать информацию об участниках автогонок: ФИО участника,
название команды, описание автомобиля, описание участника, опыт и класс участника.
Необходимо реализовать следующий функционал:
> - Регистрация новых пользователей.
> - Просмотр автогонок и регистрацию гонщиков. Пользователь должен иметь
возможность редактирования и удаления своих регистраций.
> - Написание отзывов и комментариев к автогонкам. Предварительно
комментатор должен зарегистрироваться. При добавлении комментариев
должны сохраняться даты заезда, текст комментария, тип комментария
(вопрос о сотрудничестве, вопрос о гонках, иное), рейтинг (1-10),
информация о комментаторе.
> - Администратор должен иметь возможность указания времени заезда и
результата средствами Django-admin.
> - В клиентской части должна формироваться таблица всех заездов и
результатов конкретной гонки.

##  `models.py`
```python
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserRacer(AbstractUser):
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    patronymic = models.CharField("Patronymic", null=True, max_length=30)
    team = models.CharField("Team", null=True, max_length=30)
    member_descr = models.TextField("Team member description", null=True)
    car_descr = models.TextField("Car description", null=True)
    experience_years = models.IntegerField("Experience in years", null=True)
    CLASSES = [ ('C', 'Non-pro'),
                ('B', 'Experienced'),
                ('A', 'Professional'),
                ('L', 'Another')]
    user_class = models.CharField("User's class", max_length=30, choices=CLASSES, default='L')
    username = models.CharField("Username", primary_key=True, max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Race(models.Model):
    num_race = models.AutoField("Race number", primary_key=True)
    name_race = models.CharField("Race name", max_length=50)
    date_race = models.DateTimeField("Race date", unique=True)
    place_race = models.CharField("Race place", max_length=50)

    first_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True)
    second_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True, related_name='sec_place')
    third_place = models.ForeignKey("UserRacer", on_delete=models.CASCADE, null=True, blank=True, related_name='th_pace')

    def __str__(self):
        return f"Race: {self.num_race}, {self.name_race}"


class Registration(models.Model):
    num_reg = models.AutoField("Registration number", primary_key=True)
    num_race_reg = models.ForeignKey(Race, on_delete=models.CASCADE)
    num_user_reg = models.ForeignKey(UserRacer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.num_reg}, user: {self.num_user_reg}")


class Comment(models.Model):
    id_review = models.AutoField(primary_key=True)
    num_race =  models.ForeignKey(Race, on_delete=models.CASCADE)
    time_race = models.DateTimeField("Race date and time")
    comment_time = models.DateTimeField(default=datetime.now(), blank=True)

    COMMENT_TYPES = [('RACE_Q', 'Question about race'),
                     ('COLLAB_Q', 'Question about collaboration'),
                     ('OTHER', 'Other')]
    rate = models.IntegerField("Rating", default=10, validators=[MaxValueValidator(10), MinValueValidator(1)],
                               null=True, blank=True)
    username = models.ForeignKey(UserRacer, on_delete=models.CASCADE)
    comment_type = models.CharField("Comment type", max_length=30, choices=COMMENT_TYPES)
    text = models.TextField("Comment")

    def save(self, *args, **kwargs):
        self.time_race = self.num_race.date_race
        super(Comment, self).save(*args, **kwargs)
```

## `views.py`
```python
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from .forms import MakeComment
from .models import *


def home_page(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST.get("first_name", 'NaN')
        team = request.POST.get("team", 'NaN')
        patronymic = request.POST.get("patronymic", 'NaN')
        experience_years = request.POST.get("experience_years", 'NaN')
        last_name = request.POST.get("last_name", 'NaN')

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "reg_django.html", {
                "message": "passwords do not match"
            })

        try:
            if experience_years=='':
                experience_years=0
            racer = UserRacer.objects.create_user(username, email, password, patronymic=patronymic,
                                                team=team,
                                                experience_years=experience_years)
            racer.first_name = first_name
            racer.last_name = last_name
            racer.save()
        except IntegrityError:
            return render(request, "reg_django.html", {
                "message": "username is taken"
            })
        login(request, racer)
        return redirect(reverse("races"))
    else:
        return render(request, "reg_django.html")


def reg_list_view(request):
    context = {
        'reg_races': Registration.objects.filter(num_user_reg=request.user)
    }
    print(request.user)
    print(context)
    return render(request, 'reg_list.html', context)


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('races'))
        else:
            error_text = 'invalid credentials'
    return render(request, 'login.html', locals())


class RegisterUser(CreateView):
    model = UserRacer
    fields = ['username',
              'first_name', 'last_name', 'fathername',
              'team_name',
              'user_descr',
              'car_descr',
              'experience',
              'type_user']
    success_url = '/user_list/'
    template_name = "user_reg.html"


class RegList(ListView):
    model = Registration
    template_name = 'reg_list.html'


class UserList(ListView):
    model = UserRacer
    template_name = 'user_list.html'


class RaceList(ListView):
    model = Race
    template_name = 'race_list.html'


def get_race(request, id_race: int):
    try:
        race = Race.objects.get(pk=id_race)
    except Race.DoesNotExist:
        raise Http404("Race does not exist.")
    return render(request, 'race.html', {'race': race})


class RegRaceList(ListView):
    model = Registration
    template_name = 'reg_list.html'


class RegRaceCreate(CreateView):
  model = Registration
  template_name = 'reg_form.html'
  fields = ['num_race_reg', 'num_user_reg']
  success_url = '/reg_list/'


class RegRaceDelete(DeleteView):
    model = Registration
    template_name = 'reg_delete.html'
    success_url = '/reg_list/'


class RegRaceUpdate(UpdateView):
    model = Registration
    fields = ['num_race_reg', 'num_user_reg']
    template_name = 'reg_update.html'
    success_url = '/reg_list/'


def comment(request):
    data = {}
    form = MakeComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'comment.html', data)


def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'comments_list.html', list_comments)
```

## `race_winners_app/urls.py`
```python
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home_page, name='home'),
    path('registration/', register, name='reg'),
    path('user_list/', UserList.as_view()),
    path('race/list/', RaceList.as_view(), name='races'),
    path('race/<int:id_race>', get_race),

    path('reg_list/', RegList.as_view()),
    path('reg_race/', login_required(RegRaceCreate.as_view()), name='reg-race'),
    path('reg_race/<int:pk>/update/', RegRaceUpdate.as_view()),
    path('reg_race/<int:pk>/delete/', RegRaceDelete.as_view()),

    path('comments/create/', comment, name='comment-create'),
    path('comments/list/', all_comments),

    path('login/', log_in, name='login'),
    path('logout/',  auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]
```