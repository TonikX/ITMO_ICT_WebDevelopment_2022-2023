# Лабораторная работа №2

## Практическая часть

`models.py` - модели проекта
```python
    from django.db import models
    from datetime import date
    from django.contrib.auth.models import AbstractUser

    class Owner(AbstractUser):
        owner_id = models.IntegerField(primary_key=True)
        date_of_birth = models.DateField(null=True)
        passport = models.CharField(max_length=15, blank=False, null=False, unique=True)
        address = models.CharField(max_length=100, blank=False, null=False)
        nationality = models.CharField(max_length=30, blank=True, null=False)

    class Car(models.Model):
        id_number = models.IntegerField(primary_key=True)
        brand = models.CharField(max_length=30)
        car_model = models.CharField(max_length=30)
        color = models.CharField(max_length=30)
    official_number = models.CharField(max_length=30)

    class Owning(models.Model):
        owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
        car = models.ForeignKey(Car, on_delete=models.CASCADE)
        begin_date = models.DateField(default=date(2010, 1, 1))
        end_date = models.DateField(default=date(2020, 1, 1))

    class DrivingLicense(models.Model):
        LICENCE_TYPES = (
            ('A', 'Motorcycles'),
            ('B', 'Cars'),
            ('D', 'Buses'),
        )
        number = models.IntegerField(primary_key=True)
        owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
        date_of_issue = models.DateField(default=date(2010, 1, 1))
        type = models.CharField(max_length=3, choices=LICENCE_TYPES)
```
Определим модель авторизации пользователя:

```python 
AUTH_USER_MODEL = 'project_first_app.Owner'
```

Пример одного из шаблонов:

`owners.hmtl`
```html 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Owners</title>

        <style>
            table {
                border-spacing: 20px 10px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>

    {% if new %}
        <form method="POST" enctype="multipart/form-data"> {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Submit">
        </form>
    {% else %}
        <table>
            <thead>
            <tr>
                <th>Name</th>
                <th>Surname</th>
                <th>Date of birth</th>
                <th>Passport</th>
                <th>Address</th>
                <th>Nationality</th>
            </tr>
            </thead>
        <tbody>
            {% if all %}
                {% for owner in owners %}
                    <tr>
                        <th>{{ owner.first_name }}</th>
                        <th>{{ owner.last_name }}</th>
                        <th>{{ owner.date_of_birth }}</th>
                        <th>{{ owner.passport }}</th>
                        <th>{{ owner.address }}</th>
                        <th>{{ owner.nationality }}</th>
                    </tr>
                {% endfor %}
            {% endif %}
            {% if one %}
                <tr>
                    <th>{{ owner.first_name }}</th>
                    <th>{{ owner.last_name }}</th>
                    <th>{{ owner.date_of_birth }}</th>
                    <th>{{ owner.passport }}</th>
                    <th>{{ owner.address }}</th>
                    <th>{{ owner.nationality }}</th>
                </tr>
            {% endif %}
            </tbody>
        </table>
    {% endif %}

    <a href="../create_owner">New</a>
    </body>
    </html>
```

`urls.py`
```python 
urlpatterns = [
    path('owners/', views.all_owners_detail),
    path('owner/<int:owner_id>/', views.owner_detail),
    path('create_owner/', views.create_owner),
    path('cars/', AllCars.as_view()),
    path('car/<int:pk>/', OneCar.as_view()),
    path('car/<int:pk>/update/', CarUpdate.as_view()),
    path('car/create/', CarCreate.as_view()),
    path('car/<int:pk>/delete/', CarDelete.as_view()),
]
```
`views.py`
```python 
    from django.shortcuts import render , get_object_or_404, redirect
    from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
    from project_first_app.form import OwnerForm
    from .models import Owner, Car

    def all_owners_detail(request):
        context = {"owners": Owner.objects.all(), "all": True}

        return render(request, 'owners.html', context)


    def owner_detail(request, owner_id):
        context = get_object_or_404(Owner, pk=owner_id)

        return render(request, 'owners.html', {"owner": context, "one": True})

    def create_owner(request):
        form = OwnerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/owners')
        return render(request, "owners.html", {"form": form, "new": True})

    class AllCars(ListView):
        model = Car
        template_name = "cars.html"

    class OneCar(DetailView):
        model = Car
        template_name = "cars.html"

    class CarDelete(DeleteView):
        model = Car
        template_name = 'car_confirm_delete.html'
        success_url = '/cars/'


    class CarCreate(CreateView):
        model = Car
        template_name = 'car_create_update.html'
        fields = ['id_number', 'brand', 'car_model', 'color', 'official_number']
        success_url = '/cars/

    class CarUpdate(UpdateView):
        model = Car
        fields = ['id_number', 'brand', 'car_model', 'color', 'official_number']
        success_url = '/cars/'
        template_name = 'car_create_update.html'
```
## Лабораторная часть 

### Список научных коференций

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

### Модели

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

class Theme(models.Model):
  name = models.CharField(max_length=50)

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
    return self.conference.name

class RegisteredSpeech(models.Model):
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
    return self.user.username
```

### Шаблоны
Так как шаблоны имеют достаточно большой объем, то приведу код только одного из шаблонов для примера, а остальные опустим.

Список шаблонов:
* main.html - основной шаблон
* conference_detail.html - шаблон описания конференций
```python
{% extends 'conf/main.html' %} {% block content %}

<div class="conference">
  <div class="header-bar">
    <h1 class="header">{{conference.conference.name}}</h1>
    {% if request.user.is_authenticated %}
      <a class="inroll" href={% url 'conference_register' conference.id%}>Записаться выступающим</a>
    {% endif %}
  </div>
  <h3>Описание</h3>
  <p class="description">{{conference.conference.description}}</p>
  <h3>Условия участия</h3>
  <p class="part-cond">{{conference.conference.participation_cond}}</p>
  <h3>Информация о конференции</h3>
  <div class="info">
    <p class="place">Адрес: <i>{{conference.place.name}} | {{conference.place.address}}</i></p>
    <p class="date">Дата проведения: {{conference.start_date}} - {{conference.end_date}}</p>
  </div>
</div>

<div class="register-section">
  <div class="header-bar">
    <h3 class="header">Выступления</h3>
  </div>
  {% if registers|length > 0 %}
    {% for register in registers %}
      <h4>{{register.user}} - <i>{{register.name}}</i></h4>
    {% endfor %}
  {% else %}
    <p>Выступлений нет</p>
  {% endif %}
</div>

<div class="comment-section">
  <div class="header-bar">
    <h3 class="header">Комментарии</h3>
  </div>

  {% if request.user.is_authenticated %}
    <form class='comment-form' method="post">
      {% csrf_token %}
      <p class="rating">Рейтинг: {{ comment_form.rating }}</p>
      <p class="text">Текст: <br /> {{comment_form.text}}</p>
      {{comment_form.user}}
      {{comment_form.conference}}
      <input class="button" type="submit" value="Добавить">
    </form>
  {% endif %}

  {% for comment in comments %}
    <div class="comment">
      <div class="header-bar">
        <h4 class="author">{{comment.user|title}}</h4>
        <h3 class="rating">{{comment.rating|title}}</h3>
      </div>
      <p class="text">{{comment.text}}</p>
    </div>
  {% endfor %}

</div>

{% endblock content %}
```

* conference_register.html - форма регистрации на выступление
* coferences_list.html - список конференций
* login.html - страница с формой для авторизации
* logout.html - страница для выхода из аккаунта
* register.html - страница регистрации
* registeredspeech_confirm_delete.html - страница подтверждения удаления выступления
* registers.html - список зарегистрированных выступлений
* theme_detail.html - список конференций по определенной теме
* themes_list.html - список тем

### Представления

`views.py`

```python
class RegisterPage(FormView):
  template_name = 'conf/register.html'
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

class CustomLoginView(LoginView):
  template_name = 'conf/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('conferences')

class ConferencesList(ListView):
  model = PlannedConference
  template_name = 'conf/conferences_list.html'
  context_object_name = 'conferences'


def conference_detail(request, pk):
  conference = PlannedConference.objects.get(pk=pk)
  registers = RegisteredSpeech.objects.filter(
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
  return render(request, 'conf/conference_detail.html', context)


class ThemesList(ListView):
  model = Theme
  template_name = 'conf/themes_list.html'
  context_object_name = 'themes'


class ThemeDetail(DetailView):
  model = Theme
  context_object_name = 'theme'
  template_name = 'conf/theme_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["conferences"] = PlannedConference.objects.filter(
      themes__id=context['theme'].id)
    return context


@login_required
def conference_register_view(request, pk):
  conference = PlannedConference.objects.get(pk=pk)
  initial = {'conference': conference, 'user': request.user}
  form = SpeechRegisterForm(initial=initial)
  if request.method == 'POST':
    c_form = SpeechRegisterForm(request.POST)
    if c_form.is_valid():
      c_form. save()
      return redirect(f'/conference/{pk}')
    else:
      form = c_form
  context = {'conference': conference, 'form': form}
  return render(request, 'conf/conference_register.html', context)


class RegisterList(LoginRequiredMixin, ListView):
  model = RegisteredSpeech
  template_name = 'conf/registers.html'
  context_object_name = 'registers'


class DeleteRegisterView(LoginRequiredMixin, DeleteView):
  model = RegisteredSpeech
  context_object_name = 'register'
  success_url = reverse_lazy('my_registers')
```

### Маршрутизация

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