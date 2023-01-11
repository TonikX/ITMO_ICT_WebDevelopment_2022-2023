# Пет проект "Тайный санта" (лр 3-4)

## Модели

Описание моделей:

- Лобби
- Гость
- Пользователь
- Custom Account Manager

`models.py`

```python
from django.db import models
from django.conf import settings
from string import ascii_lowercase
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(ascii_lowercase, k=length))
        if Lobby.objects.filter(code=code).count() == 0:
            break

    return code


class Lobby(models.Model):
    code = models.CharField(max_length=10, unique=True,
                            default=generate_unique_code, primary_key=True)
    name = models.CharField(max_length=50)
    event_date = models.DateField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    started = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Lobby'
        verbose_name_plural = 'Lobbies'


class Guest(models.Model):
    lobby = models.ForeignKey(Lobby, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_host = models.BooleanField(default=False)
    giving_to = models.ForeignKey(
        'Guest', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lobby.code + ' | ' + self.user.username

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, name, password, **other_fields)

    def create_user(self, username, name, password, **other_fields):

        if not username:
            raise ValueError(_('You must provide a username'))

        user = self.model(username=username, name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    preferences = models.TextField(_(
        'preferences'), max_length=500, blank=True)

    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.username
```

## Конструкторы

`views.py`

```python
from functools import partial
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Lobby, Guest
from .serializers import LobbySerializer, GuestSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings

# Create your views here.


class LobbyList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer


class LobbyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer


class LobbyGuests(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        guests = Guest.objects.filter(lobby=pk).order_by('id')
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, pk):
    #     data = request.data
    #     guest = Guest.objects.create(
    #         lobby=Lobby.objects.get(pk=pk),
    #         user=settings.AUTH_USER_MODEL.objects.get(pk=data['user_id']),
    #         is_host=data['is_host']
    #     )
    #     # Create an article from the above data
    #     serializer = GuestSerializer(guest)
    #     if serializer.is_valid(raise_exception=True):
    #         guest_saved = serializer.save()
    #     return Response(guest_saved)


class GuestList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class Shuffle_lobby(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        guests = Guest.objects.filter(lobby=pk).order_by('?')
        lobby = Lobby.objects.get(code=pk)
        lobby.started = True
        lobby.save()
        for i, guest in enumerate(guests):
            guest.giving_to = guests[(i + 1) % len(guests)]
            guest.save()
        # serializer = GuestSerializer(guests, many=True)

        return Response('guests are successfully shuffled!')
```

## URLs

Описание путей:

- api/lobby/ - Список лобби
- api/guest/ - Список гостей
- api/lobby/<str:pk>/ - Описание лобби
- api/guest/<int:pk>/ - Описание гостя
- api/lobby/<str:pk>/guest/ - Список гостей в лобби
- api/lobby/<str:pk>/shuffle/ - Перемешивание гостей в лобби
- api/token/ - Авторизация / Получение токенов
- api/token/refresh/ - Обновление access токена
- api/user/<int:pk>/ - Получение информации о пользователе
- api/user/create/ - Создание нового пользователя
- api/user/logout/blacklist/ - Логаут

# Фронтенд

## Описание страниц

- Auth - Аутентификация
- CreateLobby - Создание лобби
- Home - Начальная страница
- JoinLobby - Присоединиться к лобби
- Lobby - Страница лобби
- NotFound - Страница для отображения ошибки 404

## Компоненты

- BackButton - Кнопка назад
- Button - Кнопка
- FormWrapper - Обертка для форм
- Header - Заголовок
- Help - Помощник
- InputField - Поле ввода
- Loader - Крутилка загрузка
- PrivateRoute - Приватный маршрут
- Textarea - Поле ввода большого текста

## Кастомные хуки

- useMultistepForm - хук для создания многостраничных форм

`useMultistepForm.ts`

```javascript
import { ReactElement, useState } from 'react';

export function useMultistepForm(steps: ReactElement[]) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);

  function next() {
    setCurrentStepIndex((i) => {
      if (i >= steps.length - 1) return i;
      return i + 1;
    });
  }

  function back() {
    setCurrentStepIndex((i) => {
      if (i <= 0) return i;
      return i - 1;
    });
  }

  function goTo(index: number) {
    setCurrentStepIndex(index);
  }

  return {
    currentStepIndex,
    step: steps[currentStepIndex],
    steps,
    isFirstStep: currentStepIndex === 0,
    isLastStep: currentStepIndex === steps.length - 1,
    goTo,
    next,
    back,
  };
}
```

# Docker

`docker-compose.yml`

```docker

#docker-compose.yml
version: "3.8"
services:
  db:
    image: postgres:latest  # image: pgdb-v2
    environment:
      - POSTGRES_DB=sntwnf
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin


  backend:
    restart: always
    build:
      context: ./backend_django
    command: gunicorn santa.wsgi --bind 0.0.0.0:8000
    # command: python3 manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - db


  frontend:
    build:
      context: ./frontend
    volumes:
      - react_build:/frontend/build


  nginx:
    restart: always
    image: nginx:latest
    ports:
      - 80:8080
    volumes:
      - ./nginx/nginx-setup.conf:/etc/nginx/conf.d/default.conf:ro
      - react_build:/var/www/frontend
    depends_on:
      - backend
      - frontend

volumes:
  react_build:

```

## backend

`Dockerfile`

```docker
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /backend_django
COPY . /backend_django
RUN pip3 install -r requirements.txt
COPY . .
```

## frontend

`Dockerfile`

```docker
FROM node:15.13-alpine
WORKDIR /frontend
COPY . .
RUN npm install
RUN npm run build
```

## nginx

`nginx-setup.conf`

```nginx
upstream api {
    server backend:8000;
}

server {
  listen 8080;

  location / {
    root /var/www/frontend;
  }

  location /api/ {
    proxy_pass http://api;
    proxy_set_header Host $http_host;
  }

}
```
