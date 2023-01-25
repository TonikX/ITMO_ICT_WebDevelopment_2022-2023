##  Structure of project

* **hotel** - settings folder
* **account** - authentication and registration app
* **hotel_first_app** - main app
* **templates** - folder with html files

## hotel
* `settings.py`

Add configurations:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hotel_first_app.apps.HotelFirstAppConfig',
    'account.apps.AccountConfig'
]
```
Set path to templates folder:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Change configurations for database:
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_hotel",
        "USER": "postgres",
        "PASSWORD": "Rabotadb123",
        "HOST": "localhost",
        "PORT": "5433",
    }
}
```
Set auth user:
```python
AUTH_USER_MODEL = 'Account.User'
```

* `urls.py`
```python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
]
```

## account
* `models.py`
```python
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
```

* `urls.py`
```python
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', RegView.as_view(), name='index'),
    path('error/', error, name='error'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('hotels/', include('hotel_first_app.urls')),
    path('account/<int:pk>/', AccountUserView.as_view(), name='account'),
    path('account/<int:id_user>/update/<int:pk>', UpdateReserveView.as_view(), name='update_reserve'),
    path('account/<int:id_user>/delete/<int:pk>', ReserveDeleteView.as_view(), name='delete_reserve'),
]
```

* `views.py`
```python
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from datetime import date
from .forms import *
from hotel_first_app.models import Registration
class ReserveDeleteView(DeleteView):
    model = Registration
    template_name = 'delete_reserve.html'
    success_url = '/hotels/hotels/'
class UpdateReserveView(UpdateView):
    form_class = UpdateReserveForm
    template_name = 'update_reserve.html'
    context_object_name = 'reg'
    def get_queryset(self):
        self.success_url = f"/account/{self.kwargs['id_user']}"
        return Registration.objects.filter(pk=self.kwargs['pk'])
class AccountUserView(UpdateView):
    form_class = AccountForm
    template_name = 'account.html'
    def get_context_data(self, **kwargs):
        context = super(AccountUserView, self).get_context_data(**kwargs)
        cur_date = date.today()
        month_ago_date = cur_date.replace(month=(cur_date.month - 1))
        context['month_registrations'] = Registration.objects.filter(check_out__gte=month_ago_date)
        context['taken_registrations'] = Registration.objects.filter(status_reg="T")
        context['booked_registrations'] = Registration.objects.filter(status_reg="B")
        context['guest_registrations'] = Registration.objects.filter(id_guest=self.kwargs['pk'])
        context['guests'] = User.objects.filter(is_superuser=False)
        return context
    def get_queryset(self):
        self.success_url = f"/account/{self.kwargs['pk']}"
        return User.objects.filter(pk=self.kwargs['pk'])
def error(request):
    return render(request, 'error.html')
class RegView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'index.html'
    success_url = 'hotels'
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        context = {'username': ""}
        if form.is_valid():
            form.save()
            context['username'] = form.cleaned_data.get('username')
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('hotels')
        return render(request, 'error.html')
class LogInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('hotels')
class LogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
```

* `forms.py`
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from hotel_first_app.models import Registration
class UpdateReserveForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('id_reg', 'id_employee', 'id_guest', 'id_room', 'status_reg',
                  'status_pay', 'check_in', 'check_out', 'booking')
class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',)
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
```

## hotel_first_app
* `models.py`
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
class Hotel(models.Model):
    id_hotel = models.IntegerField(primary_key=True, verbose_name='ID Hotel')
    name_hotel = models.CharField(max_length=100, verbose_name='Name')
    city_hotel = models.CharField(max_length=30, verbose_name='City')
    address_hotel = models.CharField(max_length=255, verbose_name='Address')
    rating_hotel = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                    null=True,
                                                    blank=True,
                                                    verbose_name='Rating')
    des_hotel = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')
class Employee(models.Model):
    id_employee = models.IntegerField(primary_key=True, verbose_name='ID Employee')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    first_name_employee = models.CharField(max_length=30, verbose_name='First name')
    last_name_employee = models.CharField(max_length=30, verbose_name='Last name')
    phone_employee = models.CharField(max_length=12, verbose_name='Phone')
    class Meta:
        ordering = ["first_name_employee", "last_name_employee"]
class RoomType(models.Model):
    ECONOM = 'E'
    STANDARD = 'S'
    LUX = 'L'
    TYPE_CHOICES = [
        (ECONOM, 'Econom'),
        (STANDARD, 'Standard'),
        (LUX, 'Lux'),
    ]
    id_rt = models.IntegerField(primary_key=True, verbose_name='ID Room type')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    type_rt = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name='Type')
    rating_rt = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                 null=True,
                                                 blank=True,
                                                 verbose_name='Rating')
    price_rt = models.PositiveIntegerField(verbose_name='Price')
    des_rt = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description')
    class Meta:
        ordering = ["id_rt"]
class Room(models.Model):
    FREE = 'F'
    TAKEN = 'T'
    BOOKED = 'B'
    STATUS_CHOICES = [
        (FREE, 'Free'),
        (TAKEN, 'Taken'),
        (BOOKED, 'Booked'),
    ]
    id_room = models.IntegerField(primary_key=True, verbose_name='ID Room')
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='ID Hotel')
    id_rt = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, verbose_name='ID Room type')
    number_room = models.IntegerField(verbose_name='Number')
    status_room = models.CharField(max_length=1, choices=STATUS_CHOICES, default='F', verbose_name='Status')
    review_room = models.CharField(max_length=255, null=True, blank=True, verbose_name='Review')
    class Meta:
        ordering = ["number_room"]
class Registration(models.Model):
    TAKEN = 'T'
    BOOKED = 'B'
    PAID = 'YP'
    NO_PAID = 'NP'
    STATUS_REG_CHOICES = [
        (TAKEN, 'Taken'),
        (BOOKED, 'Booked'),
    ]
    STATUS_PAY_CHOICES = [
        (PAID, 'Paid for'),
        (NO_PAID, 'Not paid for'),
    ]
    id_reg = models.IntegerField(primary_key=True, verbose_name='ID Reg')
    id_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name='ID Employee')
    id_guest = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='ID Guest')
    id_room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name='ID Room')
    status_reg = models.CharField(max_length=1, choices=STATUS_REG_CHOICES, verbose_name='Registration status')
    status_pay = models.CharField(max_length=2, choices=STATUS_PAY_CHOICES, verbose_name='Payment status')
    check_in = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out = models.DateField(null=False, blank=False, verbose_name='Check out')
    booking = models.DateField(null=False, blank=False, verbose_name='Booking date')
    class Meta:
        ordering = ["-check_in", "-check_out"]
class Comment(models.Model):
    id_guest = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='ID Guest')
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, verbose_name='ID Room')
    username = models.CharField(max_length=30)
    rating_c = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                verbose_name='Rating')
    review_c = models.TextField(max_length=255, null=True, blank=True, verbose_name='Review')
    check_in = models.DateField(null=False, blank=False, verbose_name='Check in')
    check_out = models.DateField(null=False, blank=False, verbose_name='Check out')
```

* `urls.py`
```python
from django.urls import path
from .views import *
urlpatterns = [
    path('hotels/', HotelListView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', HotelView.as_view(), name='hotel'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/', RoomListView.as_view(), name='hotel-rooms'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:pk>/', RoomView.as_view(), name='room'),
    path('hotels/<int:id_hotel>/<int:id_rt>/rooms/<int:id_room>/comment/', CommentView.as_view(), name='comment'),
    path('reserve/', ReserveView.as_view(), name='reserve'),
]
```

* `views.py`
```python
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from .forms import *
from .models import *
class ReserveView(CreateView):
    form_class = ReserveForm
    template_name = 'reserve.html'
    def post(self, request, *args, **kwargs):
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            print(request)
            return redirect('hotels')
        return render(request, 'error.html')
class CommentView(CreateView):
    form_class = CommentForm
    template_name = 'comment.html'
    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        context['room'] = Room.objects.get(pk=self.kwargs['id_room'])
        return context
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        context = {'form': form,
                   'hotel': Hotel.objects.get(pk=self.kwargs['id_hotel']),
                   'room_type': RoomType.objects.get(pk=self.kwargs['id_rt']),
                   'room': Room.objects.get(pk=self.kwargs['id_room'])}
        return render(request, 'comment.html', context)
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print(request)
            return redirect('room', id_hotel=self.kwargs['id_hotel'], id_rt=self.kwargs['id_rt'], pk=self.kwargs['id_room'])
        return render(request, 'error.html')
class RoomView(DetailView):
    model = Room
    template_name = 'room.html'
    context_object_name = 'room'
    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        context['comments'] = Comment.objects.filter(id_room=self.kwargs['pk'])
        return context
class RoomListView(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'
    def get_context_data(self, **kwargs):
        context = super(RoomListView, self).get_context_data(**kwargs)
        context['hotel'] = Hotel.objects.get(pk=self.kwargs['id_hotel'])
        context['room_type'] = RoomType.objects.get(pk=self.kwargs['id_rt'])
        return context
    def get_queryset(self):
        return Room.objects.filter(id_rt=self.kwargs['id_rt'])
class HotelView(DetailView):
    model = Hotel
    template_name = 'hotel.html'
    context_object_name = 'hotel'
    def get_context_data(self, **kwargs):
        context = super(HotelView, self).get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.filter(id_hotel=self.kwargs['pk'])
        return context
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'hotels'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        return context
```

* `forms.py`
```python
from django import forms
from .models import Comment
from .models import Registration
class ReserveForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('id_reg', 'id_employee', 'id_guest', 'id_room', 'status_reg',
                  'status_pay', 'check_in', 'check_out', 'booking')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id_guest', 'id_room', 'username', 'rating_c', 'review_c', 'check_in', 'check_out')
```