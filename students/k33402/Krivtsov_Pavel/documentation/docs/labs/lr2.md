# Веб-приложение для бронирования отелей
---
## Модель

![Model](../../img/hotelsModel.png)

_models.py_
```python
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class Owner(models.Model):
    organization_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.organization_name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Facilities(models.Model):
    pets_allowed = models.BooleanField(verbose_name="Разрешены домашние животные")
    parking = models.BooleanField(verbose_name="Есть парковка при отеле")
    restaurant = models.BooleanField(verbose_name="Есть ресторан при отеле")
    free_wifi = models.BooleanField(verbose_name="В номере есть бесплатный WiFi")
    spa = models.BooleanField(verbose_name="Есть спа-центр при отеле")
    fitness_centre = models.BooleanField(verbose_name="Есть фитнесс-центр при отеле")
    facilities_for_disabled = models.BooleanField(verbose_name="Номер подходит для людей с ограниченными возможностями")

    def get_fields(self):
        fields = []
        for field in Facilities._meta.fields:
            if field.name != "id":
                fields.append((field.verbose_name, getattr(self, field.name)))

        return fields


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    price = models.FloatField()
    facilities = models.ForeignKey(Facilities, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.hotel.name + " " + self.name


class Reservation(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " " + self.room.name


def validate_range(value):
    if value < 0 or value > 10:
        raise ValidationError(f"{value} is outside the range 0...10")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    rating = models.IntegerField(validators=[validate_range], null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

```

---

## Формы
### Регистрации

_forms.py_
```python
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'from-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'from-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'from-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
```

### Бронирования

_forms.py_
```python
class ReserveForm(forms.ModelForm):
    date_start = forms.DateTimeField(label='Дата заезда', widget=forms.DateInput(attrs={'type': 'date'}))
    date_end = forms.DateTimeField(label='Дата выезда', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Reservation
        fields = ('date_start', 'date_end')
```

### Ввода комментария
_forms.py_
```python
class InputCommentForm(forms.ModelForm):
    reservation = forms.ModelChoiceField(label='Период проживания', empty_label='Не выбрано', queryset=None, required=False)
    rating = forms.IntegerField(label='Оценка', min_value=0, max_value=10)
    body = forms.TextInput(attrs={'size': 10, 'title': None})

    def __init__(self, user: tp.Optional[User], room: tp.Optional[Room], *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user and room:
            self.fields['reservation'].queryset = Reservation.objects.filter(user=user).filter(room=room)

    class Meta:
        model = Comment
        fields = ('reservation', 'rating', 'body')
```
---
## View's
_views.py_

### Страница регистрации
```python
from django.urls import reverse_lazy
from .forms import RegisterUserForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"

        return context
```

### Страница авторизации
```python
from django.contrib.auth.forms import AuthenticationForm

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"

        return context

    def get_success_url(self):
        next_page = self.request.GET.get("next", default="/")
        return next_page
```

### Выход из профиля
```python
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('hotels')
```

### Профиль
```python
from .models import Reservation

def profile(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "profile.html", {"title": "Профиль", "reservations": reservations})
```

### Список отелей
```python
from .models import Hotel

class HotelList(ListView):
    model = Hotel
    template_name = "hotel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Hotels"

        return context
```

### Информация об отеле
```python
from .models import Hotel, Room

class HotelInfo(DetailView):
    model = Hotel
    template_name = "hotel_info.html"
    context_object_name = "hotel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['hotel'].name
        context['rooms'] = Room.objects.filter(hotel=context['hotel'])

        return context
```

### Информация о номере
```python
from django.shortcuts import get_object_or_404, render
from .models import Comment, Room
from .forms import InputCommentForm

def room_info(request, pk):
    room = get_object_or_404(Room, id=pk)
    comments = Comment.objects.filter(room=room)

    if request.method == "POST":
        form = InputCommentForm(request.user, room, request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.room = room
            form.save()

            return redirect("room_info", pk=pk)
    else:
        if request.user.is_authenticated:
            form = InputCommentForm(request.user, room)
        else:
            form = InputCommentForm(None, None)

    return render(request, "room_info.html", {"title": room.name, "room": room, "comments": comments, "form": form})
```

### Класс, объединяющий методы для бронирования (создание, обновление, удаление)
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reservation
from .forms import ReserveForm
from datetime import datetime

class ReservationView:
    @staticmethod
    def _is_dates_valid(date_start, date_end) -> bool:
        return (date_start < date_end) and (date_start > datetime.now(tz=pytz.UTC))

    @staticmethod
    def _is_dates_free(date_start, date_end, room_id, user_id) -> bool:
        reservations = Reservation.objects.filter(room=room_id).exclude(user=user_id)
        for old_reservation in reservations:
            if (old_reservation.date_start < date_start < old_reservation.date_end) or \
                    (old_reservation.date_start < date_end < old_reservation.date_end):
                return False

        return True

    @staticmethod
    def _check_dates(request, room_id, user_id) -> tp.Tuple[bool, str]:
        date_start = datetime.strptime(request.POST['date_start'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)
        date_end = datetime.strptime(request.POST['date_end'], '%Y-%m-%d').replace(tzinfo=pytz.UTC)

        if not ReservationView._is_dates_valid(date_start, date_end):
            return False, 'Дата заезда должна быть позже сегодняшней и раньше даты выезда. Попробуйте заново'

        if not ReservationView._is_dates_free(date_start, date_end, room_id, user_id):
            return False, 'Выбранные даты заняты. Попробуйте другие'

        return True, ''

    @staticmethod
    def reserve_room(request, pk):
        room = get_object_or_404(Room, id=pk)
        form = ReserveForm(request.POST or None)
        if form.is_valid():
            dates_check = ReservationView._check_dates(request, pk, request.user.id)

            if not dates_check[0]:
                messages.error(request, dates_check[1])
                return redirect('reserve', pk=pk)

            form = form.save(commit=False)
            form.user = request.user
            form.room = room
            form.save()
            return redirect('profile')

        return render(request, "reserve.html", {"title": room.name, "form": form})

    @staticmethod
    def update_reservation(request, pk):
        reservation = get_object_or_404(Reservation, id=pk)
        form = ReserveForm(request.POST or None, instance=reservation)

        if not reservation.user == request.user:
            return redirect(f'profile')

        if form.is_valid():
            dates_check = ReservationView._check_dates(request, reservation.room.id, request.user.id)
            if not dates_check[0]:
                messages.error(request, dates_check[1])
                return redirect('update_reservation', pk=pk)

            form.save()
            return redirect('profile')

        return render(request, "update_reservation.html", {"title": "Изменить бронирование", "form": form})

    @staticmethod
    def delete_reservation(request, pk):
        reservation = Reservation.objects.get(id=pk)

        if request.user.id != reservation.user.id:
            return redirect('profile')

        if request.method == 'POST':
            reservation.delete()
            return redirect('profile')

        return render(request, 'delete_reservation.html', {'title': 'Отмена бронирования', 'reservation': reservation})
```

### Таблица постояльцев
```python
from django.shortcuts import render
from .models import Reservation

def guests_info(request):
    reservations = Reservation.objects.filter(date_start__month__lte=datetime.now().month, date_end__month__gte=datetime.now().month)

    hotels_guests: tp.Dict[Hotel, tp.Set[str]] = {}
    for reservation in reservations:
        if reservation.room.hotel in hotels_guests:
            hotels_guests[reservation.room.hotel].add(reservation.user.username)
        else:
            hotels_guests[reservation.room.hotel] = {reservation.user.username}

    return render(request, "guests.html", {"title": "Постояльцы", "hotels_guests": hotels_guests, "month": datetime.now().strftime("%B")})

```

---

## Все URL паттерны
_hotels_app/urls.py_
```python
urlpatterns = [
    path("", views.HotelList.as_view(), name="hotels"),
    path("hotel/<int:pk>", views.HotelInfo.as_view(), name="hotel_info"),
    path("room/<int:pk>", views.room_info, name="room_info"),
    path("room/<int:pk>/reserve", login_required(views.ReservationView.reserve_room, login_url="login"), name="reserve"),
    path("reservation/<int:pk>/update",
         login_required(views.ReservationView.update_reservation, login_url="login"),
         name="update_reservation"),
    path("reservation/<int:pk>/delete",
         login_required(views.ReservationView.delete_reservation, login_url="login"),
         name="delete_reservation"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", login_required(views.profile, login_url="login"), name="profile"),
    path("guests/", views.guests_info, name="guests")
]
```
