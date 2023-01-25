# Laboratory work 2
> Рейнгеверц В.А. - K33401
## Practical part

### Practical work 2.1.1-2.1.5

Model
![](https://i.imgur.com/60P88U7.png)

View
![](https://i.imgur.com/G0y3Vvm.png)

### Practical work 2.2.1-2.2.2

![](https://i.imgur.com/cRPpsFy.gif)

### Practical work 2.2.3

![](https://i.imgur.com/vwzqnWc.gif)

### Practical work 2.3

![](https://i.imgur.com/FlRST5k.png)


___


## Lab work part - TrackerFly

> 17 mod 7 = Вариант 3

3. Табло отображения информации об авиаперелетах.
   Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе (прилет, отлет), номере гейта.
   Необходимо реализовать следующий функционал:

- [x] Регистрация новых пользователей.
- [x] Просмотр и резервирование мест на рейсах. Пользователь должен иметь возможность редактирования и удаления своих резервирований.
- [x] Администратор должен иметь возможность зарегистрировать на рейс пассажира и вписать в систему номер его билета средствами Django-admin.
- [x] В клиентской части должна формироваться таблица, отображающая всех пассажиров рейса.
- [x] Написание отзывов к рейсам. При добавлении комментариев, должны сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о комментаторе.

### Screenshots

#### Homepage
![](https://i.imgur.com/1lDqUFj.png)
![](https://i.imgur.com/EX6IHFm.png)
#### Log In & Sign Up
![](https://i.imgur.com/nAkSOVo.png)
![](https://i.imgur.com/x5Yt6Iy.jpeg)

#### Flights
![](https://i.imgur.com/wKyAkww.png)

#### Flight Details
![](https://i.imgur.com/QKed9uS.png)
#### Flight Reviews
![](https://i.imgur.com/rZbDlap.png)
![](https://i.imgur.com/vaU5HLz.png)

#### Flight Passengers
![](https://i.imgur.com/suzaSYW.png)
#### Profile
![](https://i.imgur.com/1yJuVUn.png)


### [main/models.py](Lr/TrackerFly/main/models.py)
```python

from django.db.models import Avg
from datetime import datetime
from django.db.models import Count
from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from django.core.validators import MinValueValidator, MaxValueValidator

# Модель кастомного пользвателя
# - Имеет поля для ссылки и ключа для личного API
class User(AbstractUser):

    api_url = models.CharField(
        max_length=100, default="https://airlabs.co/api/v9/airports?", blank=True)
    api_key = models.CharField(
        max_length=100, default="4a84701d-216b-4db5-a5f6-5b69f85fe6d7", blank=True)


# through table модель для m2m связи между рейсом (Flight) и пользователем (User)
# - Имеет поле ticket_number – номер рейса
class FlightUser(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=15)

    def get_random_ticket_number(self):
        return User.objects.make_random_password(length=12, allowed_chars='1234567890')

    def __str__(self):
        return f"{self.ticket_number} ({self.user})"

    class Meta:
        verbose_name = "Flight Ticket"
        verbose_name_plural = "Flight Tickets"

# Модель рейса
# - Имеет поля для номера рейса, авиакомпании, даты отлета, даты прилета, типа (прилет, отлет), номере гейта, iata кода для аэропортов прибития и отправления, о m2m резерваторах, максимального количества резерваторов, цены билета
# - Имеет вспомогательные методы для возвращения отзывов на рейс, средний рейтинг, список iata кодов и группировку по дате (дню)
# - Имеет валидацию даты отправления и прибытия (второе не раньше первого)
# - Имеет валидацию максимального количества резерваторов через `forms.py`
class Flight(models.Model):
    FLIGHT_TYPES = (
        ('Departure', 'Departure'),
        ('Arrival', 'Arrival'),
    )

    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    flight_type = models.CharField(
        max_length=20, choices=FLIGHT_TYPES, default='Departure')

    gate = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10)

    # iata_codes
    source_airport_code = models.CharField(max_length=10)
    destination_airport_code = models.CharField(max_length=10)

    max_reservations = models.IntegerField(default=120)
    reservators = models.ManyToManyField(
        'User', through="FlightUser", blank=True)

    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )

    def get_reviews(self):
        return self.review_set.all()

    def get_user_review(self, user):
        return self.review_set.filter(user=user).first()

    def get_avg_rating(self):
        reviews = self.get_reviews()
        return reviews.aggregate(Avg("rating"))["rating__avg"] or 0

    def get_iata_code(self):
        """ Returns the list of two iata codes used in source_airport_code and destination_airport_code fields """
        return [self.source_airport_code, self.destination_airport_code]

    @classmethod
    def get_iata_codes(cls):
        """ Returns the list of all iata codes used in model """
        flights = cls.objects.all()
        iata_codes = []

        for flight in flights:
            iata_codes = [*iata_codes, *flight.get_iata_code()]

        return iata_codes

    @classmethod
    def group_by_day(cls, **kwargs):
        flights = cls.objects.filter(**kwargs)

        dates = flights.extra(
            select={'day': 'date( departure )'}
        ).values('day').annotate(available=Count('departure'))
        dates_dict = {}
        for date in dates:
            grouped_date = datetime.strptime(date['day'], '%Y-%m-%d').date()
            dates_dict[date['day']] = flights.filter(
                departure__contains=grouped_date)

        return dates_dict

    def __str__(self):
        return self.airline + " " + self.flight_number

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                arrival__gt=models.F('departure')), name='departure_arrival_check', violation_error_message='Departure must be earlier than arrival.'),
        ]


# Модель отзыва
# - Иммет поля для заглавия, текста, рейтинга, рейса и пользователя
# - Имеет валидацию о рейтенге между 1 и 10
class Review(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.title

```



### [main/views.py](Lr/TrackerFly/main/views.py)
```python
from django.urls import resolve
from urllib.parse import urlparse
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.views.generic import RedirectView
from operator import itemgetter

from . import models, forms, utils


# Домашняя страница
class Home(TemplateView):
    template_name = 'home.html'

# Страница со всеми перелетами
# - Требует быть залогиненным
# - Иммет ссылки на резервацию и подробности рейса
# - Отображает возможные ошибки
# - Отображает групированный список моделелей рейса (Flight)
# - Группировка происходит на основе даты рейса
# - Так как модель рейса не содержит города отправления/назначения, об этом берется из iata кода аэропортов, следющие API:
#   - airlabs.co (Дает координаты аэропорта по iata коду)
#   - OpenStreetMap.org (Дает город/регион по координатам)
class Flights(LoginRequiredMixin, ListView):
    model = models.Flight
    template_name = 'flights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_key = self.request.user.api_key
        api_url = self.request.user.api_url
        iata_codes = self.model.get_iata_codes()

        # Getting city names based on iata airport codes
        cities_result = utils.get_city_by_iata_code(
            api_key, api_url, iata_codes)
        iata_codes_dict, error = itemgetter(
            'iata_codes_dict', 'error')(cities_result)

        # Setting city names from dict
        date_dict = self.model.group_by_day()
        for date, flights in date_dict.items():
            for flight in flights:
                flight.source = iata_codes_dict[flight.source_airport_code]
                flight.destination = iata_codes_dict[flight.destination_airport_code]

        context['dates'] = date_dict
        context['error'] = error
        return context


# Подробности о рейсе
# - Требует быть залогиненным
# - Иммет ссылки на резервацию, отзывы и пассажиров рейса
# - Отображает все поля модели рейса (Flight)
# - Отображает возможные ошибки
class FlightDetails(LoginRequiredMixin, DetailView):
    model = models.Flight
    template_name = 'flight_details.html'

    def get_context_data(self, **kwargs):
        context = super(FlightDetails, self).get_context_data(**kwargs)
        try:
            flight = self.model.objects.get(pk=self.kwargs.get('pk'))
        except self.model.DoesNotExist:
            return go_back(
                self.request,
                error_message="This flight does not exist"
            )

        api_key = self.request.user.api_key
        api_url = self.request.user.api_url
        iata_codes = flight.get_iata_code()

        # Getting city names based on iata airport codes
        cities_result = utils.get_city_by_iata_code(
            api_key, api_url, iata_codes)
        iata_codes_dict, error = itemgetter(
            'iata_codes_dict', 'error')(cities_result)
        try:
            flight.source = iata_codes_dict[flight.source_airport_code]
            flight.destination = iata_codes_dict[flight.destination_airport_code]
        except KeyError:
            error = "Cached request is incorrect"

        context['flight'] = flight
        context['error'] = error

        return context

# Список пассажиров рейса
# - Требует быть залогиненным
# - Отображает m2m связь резерватора с рейсом (through table)
class FlightPassengers(LoginRequiredMixin, DetailView):
    model = models.FlightUser
    template_name = 'flight_passengers.html'

    def get_context_data(self, **kwargs):
        context = super(FlightPassengers, self).get_context_data(**kwargs)
        try:
            flight_tickets = self.model.objects.filter(
                flight__pk=self.kwargs.get('pk'))
        except self.model.DoesNotExist:
            return go_back(
                self.request,
                error_message="This flight does not exist"
            )

        context['flight_tickets'] = flight_tickets
        return context

# Список пассажиров рейса
# - Требует быть залогиненным
# - Отображает отзывы к рейсу (Review model)
class FlightReviews(LoginRequiredMixin, DetailView):
    model = models.Flight
    template_name = 'flight_reviews.html'

    def get_context_data(self, **kwargs):
        context = super(FlightReviews, self).get_context_data(**kwargs)
        flight = self.object
        flight.avg_rating = flight.get_avg_rating()

        reviews = flight.get_reviews()

        context['flight'] = flight
        context['reviews'] = reviews
        return context

# Форма создания отзыва к рейсу
# - Требует быть залогиненным
# - Позволяет написать отзыв и поставить оценку рейсу
# - Создание повторного отзыва на тот же рейс заменяет предыдущий
# - Отображает возможные ошибки
class FlightReviewCreate(LoginRequiredMixin, CreateView):
    model = models.Review
    form_class = forms.FlightReviewForm
    template_name = 'flight_review_create.html'

    def get_success_url(self):
        return go_back(self.request, url="flight_reviews", to_redirect=False, ignore_provided_kwargs=True)

    def form_valid(self, form):
        try:
            flight = models.Flight.objects.get(pk=self.kwargs['pk'])
        except models.Flight.DoesNotExist:
            return go_back(
                self.request,
                error_message="This flight does not exist"
            )

        user = self.request.user
        review = flight.get_user_review(user)
        if review:
            review.delete()

        form.instance.flight = flight
        form.instance.user = user

        return super().form_valid(form)

# Форма регистрации
# - Хеширование и валидация паролей
# - Отображает возможные ошибки
# - Автологин после регистрации
# - Иммет ссылку на авторизацию
class SignUp(CreateView):
    model = models.User
    form_class = forms.UserSignUpForm
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse("home")

    # Auto login after signing up
    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


# Форма входа
# - Отображает возможные ошибки
# - Иммет ссылку на регистрацию
class LogIn(LoginView):
    template_name = 'log_in.html'

# Выход из аккаунта
# - Нужен для кнопки выхода
class LogOut(RedirectView):
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogOut, self).get_redirect_url(*args, **kwargs)

# Профиль пользователя
# - Отображает данные пользователя (имя, логин, email)
# - Отображает зарезервированные рейсы
# - Иммет ссылку на подробности рейса
class Profile(LoginRequiredMixin, TemplateView):
    model = models.User
    template_name = 'profile.html'

    login_url = 'log_in'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)

        api_key = self.request.user.api_key
        api_url = self.request.user.api_url
        iata_codes = models.Flight.get_iata_codes()

        # Getting city names based on iata airport codes
        cities_result = utils.get_city_by_iata_code(
            api_key, api_url, iata_codes)
        iata_codes_dict, error = itemgetter(
            'iata_codes_dict', 'error')(cities_result)

        # Setting city names from dict
        date_dict = models.Flight.group_by_day(
            reservators__in=[self.request.user])
        for date, flights in date_dict.items():
            for flight in flights:
                flight_ticket = models.FlightUser.objects.filter(
                    user=self.request.user, flight=flight).first()

                flight.ticket_number = flight_ticket.ticket_number
                flight.source = iata_codes_dict[flight.source_airport_code]
                flight.destination = iata_codes_dict[flight.destination_airport_code]

        context['dates'] = date_dict
        context['error'] = error
        context.update({'user': self.request.user})
        return context


# Резервация toggle
# - Нужен для кнопки резервации
# - Требует быть залогиненным
# - Если пользователь не резервировал данный рейс, происходит резервация (при условии что есть места)
# - Если пользователь резервировал данный рейс, то резервация отменяется
# - Генерирует рандомный, 12-значный номер билета при создании связи между резерватором и рейсом
@login_required
def toggle_reserve(request, pk):
    model = models.Flight

    try:
        flight = model.objects.get(pk=pk)
    except model.DoesNotExist:
        return go_back(
            request,
            error_message="This flight does not exist"
        )

    is_reserved = request.user in flight.reservators.filter(pk=request.user.pk)

    if not is_reserved:
        reservators_count = flight.reservators.count()
        max_reservations = flight.max_reservations

        if reservators_count >= max_reservations:
            return go_back(
                request=request,
                error_message="All seats have already been reserved."
            )

        flight.reservators.add(request.user)

        # Generation random ticket number
        flight_ticket = models.FlightUser.objects.filter(
            user=request.user, flight=flight).first()
        flight_ticket.ticket_number = flight_ticket.get_random_ticket_number()
        flight_ticket.save()

    else:
        flight.reservators.remove(request.user)

    return go_back(request)

# - Редиректит на предыдущую страницу
def go_back(request, to_redirect=True, ignore_provided_kwargs=True, url="", kwargs={}, error_message=""):
    curr_url = request.path
    prev_url = urlparse(request.META.get('HTTP_REFERER')).path
    prev_url_name = resolve(prev_url).url_name
    prev_url_kwargs = resolve(prev_url).kwargs

    if not url:
        url = prev_url_name
    if ignore_provided_kwargs:
        kwargs = prev_url_kwargs

    # Prevent getting stuck in redirecting
    if curr_url == url:
        url = "home"
        kwargs = {}

    if error_message:
        messages.error(request, error_message)
    if to_redirect:
        return redirect(reverse_lazy(url, kwargs=kwargs))
    else:
        return reverse_lazy(url, kwargs=kwargs)
```

###[main/urls.py](Lr/TrackerFly/main/urls.py)
```python
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('signup/', views.SignUp.as_view(), name="sign_up"),
    path('login/', views.LogIn.as_view(), name="log_in"),
    path('logout/', views.LogOut.as_view(), name="log_out"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('flights/', views.Flights.as_view(), name="flights"),
    path('flight/<int:pk>', views.FlightDetails.as_view(), name="flight_details"),
    path('flight/reserve/<int:pk>', views.toggle_reserve, name="toggle_reserve"),
    path('flight/passengers/<int:pk>',
         views.FlightPassengers.as_view(), name="flight_passengers"),
    path('flight/reviews/<int:pk>',
         views.FlightReviews.as_view(), name="flight_reviews"),
    path('flight/review/create/<int:pk>',
         views.FlightReviewCreate.as_view(), name="flight_review_create"),
]
```



___



## My Notes

### Activating python venv

```bash
source ../.web-dev-env/Scripts/activate
```

### VSCode setup

`Python: Select Interpreter` – to fix IntelliSense

```bash
python -m pip install --upgrade djlint
```

Install djlint extension and add its config - `.djlintrc`:

```json
{
    "ignore": "H030,H031"
}
```

### Admin

User: `admin`

Email: `admin@example.com`

Password: `admin`

### Requirements
- django-tailwind
- geocoder
- requests_cache
- django-money


### Running

Script for running dev server with tailwinds,

```bash
bash run.sh
```

which combines this:

```bash
source ../../../.web-dev-env/Scripts/activate && python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

and that command:

```bash
source ../../../.web-dev-env/Scripts/activate && python manage.py tailwind start
```
