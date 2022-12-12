# Лабораторная работа 2

## Структура проекта

- `laboratory_work_2` - основная директория django-проекта
- `tourism` - основное приложение
- `tourism/templates` - директория с html-шаблонами

## Настройки

- `laboratory_work_2/settings.py`  

_настройка путей и модели авторизации_
```python
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'tourism.Tourist'
```
_настройка приложений_
```python
INSTALLED_APPS = [
    'tourism',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- `laboratory_work_2/urls.py`  

_добавление url приложения_
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tourism.urls')),
]
```

## Приложение `tourism`

- `admin.py`
```python
from django.contrib import admin
from tourism.models import Tour, Tourist, Reservation

@admin.register(Tour, Tourist, Reservation)
class Admin(admin.ModelAdmin):
    pass
```
- `forms.py`
```python
from django import forms
from .models import Tourist, Reservation, Comment
  
  
class SignupForm(forms.ModelForm):
    class Meta:
        model = Tourist
        help_texts = {
            'username': None,
        }
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'rating'
        ]
```
- `models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Tourist(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Tour(models.Model):
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True, blank=True)
    end_date = models.DateField(auto_now_add=True, blank=True)
    terms_of_payment = models.CharField(max_length=50)
    tourists = models.ManyToManyField('Tourist', through='Reservation')


class Reservation(models.Model):
    tourist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)


class Comment(models.Model):
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    author = models.ForeignKey('Tourist', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    publish_date = models.DateTimeField(auto_now_add=True)
```
- `urls.py`
```python
from django.urls import path
from django.contrib.auth import views
import tourism.views


urlpatterns = [
    path('', tourism.views.view_table, name='view_table'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign_out/', views.LogoutView.as_view(), name='sign_out'),
    path('sign_up/', tourism.views.sign_up, name='sign_up'),
    path('tours/', tourism.views.view_tours, name='view_tours'),
    path('tours/<int:pk>', tourism.views.view_tour, name='view_tour'),
    path('tours/<int:pk>/reserve', tourism.views.reserve_tour, name='reserve_tour'),
    path('reservations/', tourism.views.view_reservations, name='view_reservations'),
    path('reservations/<int:pk>/cancel', tourism.views.cancel_reservation, name='cancel_reservation'),
]
```
- `views.py`
```python
from django.shortcuts import render, redirect
from django.http import Http404 
from .forms import SignupForm, ReserveForm, CommentForm
from .models import Tourist, Tour, Reservation, Comment


def view_table(request):
    ctx = {}
    ctx['tours_by_country'] = {c: Tour.objects.filter(country=c) for c in list(dict.fromkeys([x.country for x in Tour.objects.all()]))}
    return render(request, 'view_table.html',  ctx)


def sign_up(request):
    ctx = {}

    form = SignupForm(request.POST or None)

    if form.is_valid():
        u = form.save(commit=False)
        password = request.POST.dict().get('password')
        u.set_password(password or 'password')
        form.save()
        return redirect('/login/')
    ctx['form'] = form
    return render(request, 'signup.html', ctx)


def view_tours(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    ctx = {}
    ctx['tours'] = Tour.objects.all().order_by('country')
    return render(request, 'view_tours.html', ctx)


def view_tour(request, pk):
    ctx = {}
    try:
        ctx['tour'] = Tour.objects.get(pk=pk)
        ctx['comments'] = Comment.objects.filter(tour=pk)
        form = CommentForm(request.POST or None)
        ctx['form'] = form

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Tourist.objects.get(pk=request.user.id)
            comment.tour = ctx['tour']
            comment.save()
    except Tour.DoesNotExist:
        raise Http404("Такой тур не найден")
    return render(request, 'view_tour.html', ctx)


def reserve_tour(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login/')
    form = ReserveForm(request.POST or None)
    reservation = form.save(commit=False)
    reservation.tour = Tour.objects.get(pk=pk)
    reservation.tourist = Tourist.objects.get(pk=request.user.id)
    reservation.save()
    return redirect(f'/reservations/')



def view_reservations(request):
    ctx = {}
    if not request.user.is_authenticated:
        return redirect('/login/')
    ctx['reservations'] = Reservation.objects.filter(tourist=request.user.id)
    return render(request, 'view_reservations.html', ctx)


def cancel_reservation(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    reservation = Reservation.objects.get(pk=pk, tourist=request.user.id)
    reservation.delete()
    return redirect('/reservations/')
```