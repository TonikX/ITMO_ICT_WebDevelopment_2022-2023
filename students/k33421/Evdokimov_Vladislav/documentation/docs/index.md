# Лабораторная работа №2. Евдокимов Владислав К33421



## Описание
		  ВАРИАНТ 4:
	Список туров туристической фирмы

Хранится информация о названии тура, турагенстве, описании тура, периоде проведения тура, условиях оплаты.
Необходимо реализовать следующий функционал:
1) Регистрация новых пользователей.
2) Просмотр и резервирование туров. Пользователь должен иметь возможность редактирования и удаления своих резервирований. 
3) Написание отзывов к турам. При добавлении комментариев, должны сохраняться даты тура, текст комментария, рейтинг (1-10), информация о комментаторе.
4) Администратор должен иметь возможность подтвердить резервирование тура средствами Django-admin. 
5) В клиентской части должна формироваться таблица, отображающая все проданные туры по странам.



## Файлы проекта:

	models.py
```
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField("username", max_length=150, unique=True)
    password = models.CharField(max_length=30, null=False)
    passport_data = models.CharField(max_length=30, null=False)
    email = models.EmailField("email address", unique=True)
    tour = models.ManyToManyField("self", through="Reservation")
    phone_number = models.IntegerField(null=True)


class Tour(models.Model):
    payment_by = [('Наличные', 'Наличные'), ('Онлайн оплата', 'Онлайн оплата')]
    naming = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=2000, null=False)
    paid_with = models.CharField(max_length=13, choices=payment_by)
    start_date = models.DateField()
    end_date = models.DateField()


class Feedback(models.Model):
    User = get_user_model()
    rating = [(1, '1'), (2, '2'), (3, '3'), (3, '3'), (4, '4'),
              (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=5000)
    tour = models.ForeignKey("Tour", on_delete=models.CASCADE)
    user_rating = models.IntegerField(choices=rating)
    date_of_publication = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()


class Reservation(models.Model):
    User = get_user_model()
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.BooleanField(null=True)
```
	forms.py

```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'passport_data', 'phone_number']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('username', 'start_date', 'tour', 'end_date', 'user_rating', 'comment', 'date_of_publication')

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True


class CreateReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('username', 'tour', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(CreateReservationForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['tour'].disabled = True
```

	views.py
```
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')
    else:
        form = RegistrationForm()
    visual = {'form': form}
    return render(request, 'registration/signin.html', visual)


def user_login(request):
    global form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/main')
        else:
            return HttpResponse('Неправильный логин или пароль!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/main')


class CreateReservation(CreateView):
    form_class = CreateReservationForm
    model = Reservation
    template_name = 'reservation.html'
    context_object_name = 'reservation'
    success_url = '/profile'

    def get_initial(self):
        initial = super(CreateReservation, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        initial['tour'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


class UpdateReserveView(UpdateView):
    model = Reservation
    fields = ['start_date', 'end_date']
    template_name = 'upreservation.html'
    context_object_name = 'reservation'
    success_url = '/profile'


class DeleteReserveView(DeleteView):
    model = Reservation
    template_name = 'delreservation.html'
    context_object_name = 'reservation'
    success_url = '/profile'


def reservedtourlist(request):
    visual = {"reservations": Reservation.objects.all()}
    return render(request, 'reservedtour.html', visual)


class listreservations(ListView):
    template_name = 'profilereservations.html'
    context_object_name = 'reservation_list'

    def get_queryset(self):
        self.user = self.request.user.pk
        return Reservation.objects.filter(username=self.user)


def commentlist(request):
    visual = {"comments": Feedback.objects.all()}
    return render(request, 'comments.html', visual)


def tourlist(request):
    visual = {"tours": Tour.objects.all()}
    return render(request, 'tours.html', visual)


class CreateComment(CreateView):
    form_class = CreateCommentForm
    model = Feedback
    template_name = 'comment.html'
    context_object_name = 'comment'
    success_url = '/comments'

    def get_initial(self):
        initial = super(CreateComment, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        return initial
```
	
	urls.py
```
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('main/', views.homepage),
    path('profile/', views.profile),
    path('login/', views.user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', views.log_out),
    path('reservedtour/', views.reservedtourlist),
    path('comments/', views.commentlist),
    path('createcomment/', CreateComment.as_view()),
    path('tours/', views.tourlist),
    path('tours/<int:pk>/reservation', CreateReservation.as_view(), name='reservation'),
    path('profilereservations/', listreservations.as_view(), name='reservations'),
    path('profilereservations/deletereservation/<int:pk>/', views.DeleteReserveView.as_view()),
    path('profilereservations/updatereservation/<int:pk>/', views.UpdateReserveView.as_view())
]
```



