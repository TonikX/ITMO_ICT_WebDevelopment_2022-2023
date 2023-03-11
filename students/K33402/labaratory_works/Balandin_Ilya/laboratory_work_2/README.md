#Лабораторная работа 2

## Задание

Табло отображения информации об авиаперелетах. Хранится информация о номере рейса, авиакомпании, отлете, прилете, типе
(прилет, отлет). Необходимо реализовать следующий функционал:
- Регистрация новых пользователей.
- Просмотр и резервирование мест на рейсах. Пользователь должен иметь
возможность редактирования и удаления своих резервирований. 
- Администратор должен иметь возможность зарегистрировать на рейс
пассажира и вписать в систему номер его билета средствами Django-admin. 
- В клиентской части должна формироваться таблица, отображающая всех
пассажиров рейса. 
- Написание отзывов к рейсам. При добавлении комментариев, должны
сохраняться дата рейса, текст комментария, рейтинг (1-10), информация о
комментаторе.

##   Модели

### Город

```python
class City(models.Model):
    name = models.CharField('City name', max_length=64, unique=True)
    slug = models.SlugField('City link', max_length=64, unique=True)

    def get_absolute_url(self):
        return reverse('city_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
```

### Авиалиния

```python
class Airline(models.Model):
    name = models.CharField('Airline name', max_length=64, unique=True)

    def __str__(self):
        return self.name
```

### Рейс

```python
class Flight(models.Model):
    number = models.CharField('Flight number', max_length=10, db_index=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    city_from = models.ForeignKey(City, related_name='flights_from', on_delete=models.CASCADE)
    city_to = models.ForeignKey(City, related_name='flights_to', on_delete=models.CASCADE)
    departure = models.DateTimeField('Departure datetime', null=False)
    arrival = models.DateTimeField('Arrival datetime', null=False)
    slug = models.SlugField(max_length=150, unique=True)
    can_buy = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number}: {self.city_from} - {self.city_to}. Departure at {self.departure}"

    def get_absolute_url(self):
        return reverse('flight_details_url', kwargs={'slug': self.slug})
```

### Билет

```python
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # to be filled in when purchasing the ticket
    passenger_name = models.CharField(max_length=32, null=False)
    passenger_surname = models.CharField(max_length=32, null=False)
    passenger_passport = models.CharField(max_length=10, null=False)
    # to be filled in at check-in
    seat = models.CharField(max_length=3, null=True, blank=True, default=None)

    review_text = models.TextField(null=True, default=None, blank=True)
    rate = models.IntegerField(null=True, default=None, blank=True)

    def __str__(self):
        return f"[{self.flight}] {self.passenger_surname} {self.passenger_name}"
```

## Пути

```python
urlpatterns = [
    path('flights/', flights_list, name='flights_list_url'),
    path('flights/<str:slug>/', flight_details, name='flight_details_url'),

    path('registration/', registration, name='registration_url'),
    path('login/', login_page, name='login_url'),
    path('logout/', logout_user, name='logout_url'),

    path('profile/', profile, name='profile_url'),
    path('profile/ticket/<int:pk>/delete/', ticket_delete, name='ticket_delete_url'),
    path('profile/ticket/<int:pk>/review/update/', ReviewUpdate.as_view()),
    path('profile/ticket/<int:pk>/update/', TicketUpdate.as_view()),
]
```

## Представления

### Табло рейсов

```python
def flights_list(request):
    flights = Flight.objects.all()
    flights = flights.order_by('departure').reverse()
    return render(request, 'flights/flights_list.html', context={'flights': flights})
```

### Информация о рейсе

```python
@login_required(login_url='login_url')
def flight_details(request, slug):
    flight = Flight.objects.get(slug__iexact=slug)
    rates = Ticket.objects.filter(flight__slug=slug).exclude(rate=None)
    passengers = Ticket.objects.filter(flight__slug=slug).order_by('seat')
    form = BuyTicketForm(request.POST or None)

    if request.method == 'POST':
        form = BuyTicketForm(request.POST)
        ticket = form.save(commit=False)
        ticket.user = request.user
        ticket.flight = flight
        if form.is_valid():
            ticket.save()
            return redirect('profile_url')

    isOrdered = Ticket.objects.filter(user__username=request.user.username, flight__slug=slug)

    return render(request, 'flights/flight_page.html',
                  context={'flight': flight, 'form': form, 'ordered': isOrdered, 'rates': rates,
                           'passengers': passengers})
```
Соответствующая форма:
```python
class BuyTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "passenger_name",
            "passenger_surname",
            "passenger_passport",
        ]
```

### Регистрация и аутентификация
```python
def registration(request):
    if request.user.is_authenticated:
        return redirect('tours_list_url')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
                return redirect('login_url')
        return render(request, 'flights/registration.html', context={'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('flights_list_url')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile_url')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'flights/login.html', context={})


def logout_user(request):
    logout(request)
    return redirect('login_url')
```

### Профиль пользователя

```python
@login_required(login_url='login_url')
def profile(request):
    tickets = Ticket.objects.filter(user__username__iexact=request.user)
    tickets = tickets.order_by('flight__departure').reverse()
    return render(request, 'flights/profile.html',
                  context={'tickets': tickets})


def ticket_delete(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    return redirect('profile_url')


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['passenger_name', 'passenger_surname', 'passenger_passport']
    success_url = '/profile'
    template_name = 'flights/ticket_update.html'


class ReviewUpdate(UpdateView):
    model = Ticket
    fields = ['rate', 'review_text']
    success_url = '/profile'
    template_name = 'flights/review_update.html'
```