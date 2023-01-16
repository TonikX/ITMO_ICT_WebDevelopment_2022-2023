from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):

    CATEGORY = [
        ("Спорт и фитнес", "Спорт и фитнес"),
        ("Искусство и культура", "Искусство и культура"),
        ("Природа", "Природа"),
        ("Карьера и образование", "Карьера и образование"),
        ("Театры", "Театры"),
        ("Концерты", "Концерты"),
    ]

    TYPES_EVENTS = [
        ("offline", "Очно"),
        ("online", "Онлайн"),
    ]

    DISTRICT = [
        ('any', 'Любой'),
        ("admiral", "Адмиралтейский"),
        ("vasileostrov", "Василеостровской"),
        ("vyborg", "Выборгский"),
        ("kalininsk", "Калининский"),
        ("kirov", "Кировский"),
        ("krasnogvard", "Красногвардейский"),
        ("krasnosel", "Красносельский"),
        ("kronshtad", "Кронштадский"),
        ("moskovsk", "Московский"),
        ("nevsk", "Невский"),
        ("petrograd", "Петроградский"),
        ("center", "Центральный"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY)
    place = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.CharField(max_length=50)
    photo = models.CharField(max_length=100)
    type_event = models.CharField(max_length=10, choices=TYPES_EVENTS)
    district = models.CharField(max_length=20, choices=DISTRICT)
    description = models.TextField(blank=True)
    contact_number = models.CharField(max_length=12, blank=True)
    contact_name = models.CharField(max_length=50, blank=True)
    map = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['last_name', 'first_name', 'email']

class UsersEvents(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reg_user')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reg_event')
