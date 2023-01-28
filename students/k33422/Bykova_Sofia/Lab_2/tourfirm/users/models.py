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
