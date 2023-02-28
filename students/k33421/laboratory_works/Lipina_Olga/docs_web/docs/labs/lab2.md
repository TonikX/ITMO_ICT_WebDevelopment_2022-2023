# Лабораторная работа №2

## Текст задания
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
> 
---

##  `models.py`
```python
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# from race_winners_project.race_winners_project.settings import AUTH_USER_MODEL

# Create your models here.
class Racer(AbstractUser):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    fathername = models.CharField("Отчество", null=True, blank=True, max_length=30)
    team_name = models.CharField("Название команды", null=True, blank=True, max_length=30)
    user_descr = models.TextField("Описание участника", null=True, blank=True)
    car_descr = models.TextField("Описание машины", null=True, blank=True)
    experience = models.IntegerField("Опыт", null=True, blank=True)
    USER_TYPE = [    ('A', 'Высший'),
                     ('B', 'Высокий'),
                     ('C', 'Иное')]
    type_user = models.CharField("Класс участника", max_length=30, choices=USER_TYPE, default='C')
    username = models.CharField("Логин", primary_key=True, max_length=50)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f"{self.last_name} {self.first_name}"



class Race(models.Model):
    num_race = models.AutoField("Номер гонки", primary_key=True)
    name_race = models.CharField("Название гонки", max_length=50)

    date_race = models.DateTimeField("Дата и время гонки", unique=True)
    place_race = models.CharField("Место гонки", max_length=50)

    first_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True)
    second_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='sec_place')
    third_place = models.ForeignKey('Racer', on_delete=models.CASCADE, null=True, blank=True, related_name='th_pace')

    def __str__(self):
        return f"Гонка № {self.num_race}, {self.name_race}"


class RegistrationRace(models.Model):
    num_reg = models.AutoField("Номер регистрации", primary_key=True)
    num_race_reg = models.ForeignKey(Race, on_delete=models.CASCADE)
    num_user_reg = models.ForeignKey('Racer', on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.num_race_reg}, user: {self.num_user_reg}")

class Comment(models.Model):
    id_review = models.AutoField(primary_key=True)
    num_race =  models.ForeignKey(Race, on_delete=models.CASCADE)
    time_race = models.DateTimeField("Дата и время заезда")
    comment_time = models.DateTimeField(default=datetime.now(), blank=True)

    COMMENT_TYPES = [('RACE_Q', 'Вопрос о гонке'),
                     ('COLLAB_Q', 'Вопрос о сотрудничестве'),
                     ('OTHER', 'Иное')]
    rate = models.IntegerField("Поставьте рейтинг", default=10, validators=[MaxValueValidator(10), MinValueValidator(1)],
                               null=True, blank=True)
    username = models.ForeignKey('Racer', on_delete=models.CASCADE)
    type_comment = models.CharField("Тип комментария", max_length=30, choices=COMMENT_TYPES)
    text = models.TextField("Комментарий к гонке")

    def save(self, *args, **kwargs):
        self.time_race = self.num_race.date_race
        super(Comment, self).save(*args, **kwargs)

```



## `views.py`
```python
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.db import IntegrityError


from .forms import MakeComment
from .models import *

# Create your views here.

def main_page(request):
    return render(request, 'main.html')




def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST.get("first_name", 'NaN')
        team_name = request.POST.get("team_name", 'NaN')
        fathername = request.POST.get("fathername", 'NaN')
        experience = request.POST.get("experience", 'NaN')
        last_name = request.POST.get("last_name", 'NaN')

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register_django.html", {
                "message": "passwords do not match"
            })

        try:
            if experience=='':
                experience=0
            student = Racer.objects.create_user(username, email, password, fathername=fathername,
                                                team_name=team_name,
                                                experience=experience)
            student.first_name = first_name
            student.last_name = last_name
            student.save()
            # homeworks = Homework.objects.all()
            # for homework in homeworks:
            #     assignment = Assignment(student=student, homework=homework)
            #     assignment.save()
        except IntegrityError:
            return render(request, "register_django.html", {
                "message": "username already taken"
            })
        login(request, student)
        return redirect(reverse("races"))
    else:
        return render(request, "register_django.html")



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
    return render(request, 'login_django.html', locals())

# @login_required
# def log_out(request):
#     logout(request)
#     return redirect(reverse('logout'))
#



class RegisterUser(CreateView):
    model = Racer
    fields = ['username',
              'first_name', 'last_name', 'fathername',
              'team_name',
              'user_descr',
              'car_descr',
              'experience',
              'type_user']
    success_url = '/user_list/'
    template_name = "user_register.html"

class UserList(ListView):
    # list view
    model = Racer
    template_name = 'user_list.html'

class RaceList(ListView):
    # list view
    model = Race
    template_name = 'race_list.html'

def get_race(request, id_race: int):
    # https:..race/1/
    try:
        race = Race.objects.get(pk=id_race)
    except Race.DoesNotExist:
        raise Http404("Race does not exist.")
    return render(request, 'race.html', {'race': race})


class RegRaceList(ListView):
    # list view
    model = RegistrationRace

    template_name = 'reg_race_list.html'

def reg_race_list_vies(request):
    context = {
        'reg_races': RegistrationRace.objects.filter(num_user_reg=request.user)
    }
    print(request.user)
    print('--', context)
    return render(request, 'reg_race_list.html', context)


class RegRaceCreate(CreateView):
  model = RegistrationRace
  template_name = 'reg_race_form.html'
  fields = ['num_race_reg']
  success_url = '/reg_race/list/'
  def form_valid(self, form):
    form.instance.num_user_reg = self.request.user
    return super().form_valid(form)

class RegRaceDelete(DeleteView):
    model = RegistrationRace
    template_name = 'reg_race_delete.html'
    success_url = '/reg_race/list/'

class RegRaceUpdate(UpdateView):
    model = RegistrationRace
    fields = ['num_race_reg']
    template_name = 'reg_race_update.html'
    success_url = '/reg_race/list/'

@login_required
def make_comment(request):
    data = {}
    form = MakeComment(request.POST or None)
    user_racer = None
    if request.user.is_authenticated:
        user_racer = request.user
        # request.POST['username'] = username
    else:
        return None
    if form.is_valid():
        bet = form.save(commit=False)  # the bet isn't saved just yet
        bet.username = user_racer  # you add the user here
        bet.save()
    data['form'] = form
    return render(request, 'comment_create.html', data)

def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'comments_list.html', list_comments)

```

## `racers_app/urls.py`
```python
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
   # path('registration/', RegisterUser.as_view(), name='reg'),
    path('registration/', register, name='reg'),
    path('user_list/', UserList.as_view()),
    path('race/list/', RaceList.as_view(), name='races'),
    path('race/<int:id_race>', get_race),
    path('main/', main_page, name='main'),

    path('reg_race/list/', reg_race_list_vies),
    path('reg_race/', login_required(RegRaceCreate.as_view()), name='reg-race'),
    path('reg_race/<int:pk>/update/', RegRaceUpdate.as_view()),
    path('reg_race/<int:pk>/delete/', RegRaceDelete.as_view()),

    path('comments/create/', make_comment, name='comment-create'),
    path('comments/list/', all_comments),

    path('login/', log_in, name='login'),
    path('logout/',  auth_views.LogoutView.as_view(template_name='logout_django.html'), name='logout')
]


```