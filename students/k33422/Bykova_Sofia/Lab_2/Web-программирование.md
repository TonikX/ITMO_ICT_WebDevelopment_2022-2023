# Web-программирование
## Лабораторная работа 2
### Описание варианта:
Список туров туристической фирмы
Хранится информация о названии тура, турагенстве, описании тура, периоде
проведения тура, условиях оплаты.
Необходимо реализовать следующий функционал:
 Регистрация новых пользователей.
 Просмотр и резервирование туров. Пользователь должен иметь возможность
редактирования и удаления своих резервирований.
 Написание отзывов к турам. При добавлении комментариев, должны
сохраняться даты тура, текст комментария, рейтинг (1-10), информация о
комментаторе.
 Администратор должен иметь возможность подтвердить резервирование
тура средствами Django-admin.
 В клиентской части должна формироваться таблица, отображающая все
проданные туры по странам.
Код прокомментирован.
# models для пользователей
```py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Собственная модель пользователя
class CustomUser(AbstractUser):
    # Имя и фамилия переопределены как обязательные поля
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)

    # Превращает "Иван Иванов" в "Иван И"
    @property
    def anonimous_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name[0]}"
        else:
            return "Безымянный пользователь"
```
# models для туров
```py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from users.models import CustomUser


# Модель тура
class Tour(models.Model):
    destination = models.CharField("Направление", max_length=200)
    date_from = models.DateField("Начало")
    date_to = models.DateField("Конец")
    hotel = models.CharField("Название отеля", max_length=100)
    price = models.PositiveIntegerField("Цена")
    count = models.PositiveIntegerField("Количество мест", default=0)

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    # Функция получения количества свободных мест
    @property
    def empty_count(self):
        occupied = 0
        for reservation in self.reservations.all():
            occupied += reservation.count
        return self.count - occupied

    # Функция получения количества свободных мест, исключающая конкретное резевривование (нужно для редактирования)
    def adjusted_empty_count(self, exclude_id):
        occupied = 0
        for reservation in self.reservations.exclude(pk=exclude_id):
            occupied += reservation.count
        return self.count - occupied

    def __str__(self):
        return f"Тур \"{self.destination}\" ({self.date_from} - {self.date_to})"


# Модель резервирования
class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="reservations")
    tour = models.ForeignKey(Tour, verbose_name="Тур", on_delete=models.CASCADE, related_name="reservations")
    count = models.PositiveIntegerField("Количество людей", validators=[MinValueValidator(1)])
    approved = models.BooleanField("Подтверждение", default=False)

    class Meta:
        verbose_name = "Резервирование"
        verbose_name_plural = "Резервирования"

    # Считает суммарную цену на всех людей
    @property
    def total_price(self):
        return self.count * self.tour.price

    # Есть ли отзыв
    @property
    def has_review(self):
        return hasattr(self, "review")

    # Проверяет что в туре достаточно мест
    def clean(self):
        if self.tour.adjusted_empty_count(self.pk) < self.count:
            raise ValidationError("В туре недостаточно мест")

    def __str__(self):
        return f"Бронирование тура \"{self.tour.destination}\" пользователем {self.user.username}"


# Модель отзыва
class Review(models.Model):
    reservation = models.OneToOneField(Reservation, verbose_name="Резервация", on_delete=models.CASCADE, related_name="review")
    text = models.TextField("Текст")
    stars = models.PositiveIntegerField("Оценка из 10", validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв на тур \"{self.reservation.tour.destination}\" пользователя {self.reservation.user.username}"

```

# views для пользователей
``` py
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Представление с формой для регистрации пользователя
class UserCreateFormView(FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(UserCreateFormView, self).form_valid(form)
```
# views для туров
``` py
from .models import Tour, Reservation, Review


# Список доступных туров
class TourListView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = "tours/tours.html"
    queryset = Tour.objects.order_by("destination")  # Туры сортируются по пункту назначения
    login_url = reverse_lazy("login")

    # Показывает только те туры где есть место
    def get_queryset(self):
        queryset = self.queryset
        ids = [tour.id for tour in queryset if tour.empty_count > 0]
        return queryset.filter(pk__in=ids)


# Список резервирований пользователя
class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "tours/reservations.html"
    queryset = Reservation.objects.none()  # Задаем queryset чтобы django не выдавал ошибку
    login_url = reverse_lazy("login")

    # Выбирает только резервирования текущего пользователя
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


# Информация о туре + отзывы
class TourAndReviewsView(LoginRequiredMixin, DetailView):
    model = Tour
    template_name = "tours/reviews.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        # Fetch comments for room
        context = super(TourAndReviewsView, self).get_context_data(**kwargs)
        review_ids = []
        for reservation in self.get_object().reservations.all():
            if reservation.has_review:
                review_ids.append(reservation.review.pk)
        context['reviews'] = Review.objects.filter(pk__in=review_ids)
        return context


# Создание резервирования
class CreateReservationView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "tours/reserve.html"
    fields = ("tour", "count")
    success_url = reverse_lazy("reservations")
    login_url = reverse_lazy("login")

    # Добавляет текущего пользователя в модель
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReservationView, self).form_valid(form)

    # Выбирает нужный тур в поле если он уже указан в ссылке
    def get_initial(self):
        initial = super(CreateReservationView, self).get_initial()
        if 'select' in self.request.GET:
            initial['tour'] = self.request.GET.get('select')
        return initial


# Создание отзыва
class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "tours/write.html"
    fields = ("text", "stars")
    success_url = reverse_lazy("reservations")
    login_url = reverse_lazy("login")

    # Привязывает комментарий к резервированию по url
    def form_valid(self, form):
        form.instance.reservation = get_object_or_404(Reservation, pk=int(self.request.GET['reservation']))
        return super(CreateReviewView, self).form_valid(form)

```
Были задокументированы наиболее значимые файлы. 