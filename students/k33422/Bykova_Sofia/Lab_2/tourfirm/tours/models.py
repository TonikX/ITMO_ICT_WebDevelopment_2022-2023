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
