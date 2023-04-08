from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Country(models.Model):
    """Модель страны"""
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    code = models.SlugField("Код страны", primary_key=True, max_length=2, validators=[MinLengthValidator(2)])
    name = models.CharField("Название страны", max_length=50)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    """Модель города"""
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    name = models.CharField("Название города", max_length=50)
    description = models.TextField("Описание", blank=True, default="")
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    country = models.ForeignKey(Country, models.CASCADE, verbose_name="Страна", related_name="cities")

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class UserChoice(models.Model):
    """Модель выбранного пользоватем города"""
    class Meta:
        verbose_name = "Город пользователя"
        verbose_name_plural = "Города пользователей"
        unique_together = ["user", "city"]

    user = models.ForeignKey(User, models.CASCADE, verbose_name="Пользователь", related_name="choices")
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город", related_name="choice")

    def __str__(self):
        return f"{self.user.username} - {self.city.name}"
