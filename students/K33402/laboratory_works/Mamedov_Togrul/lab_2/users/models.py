from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class ClientManager(UserManager):

    def create_user(self, username, first_name,
                    last_name, password=None, **extra_fields):
        if not username:
            raise ValueError('Clients must have the username')
        if not first_name:
            raise ValueError('Clients must have the first_name')
        if not last_name:
            raise ValueError('Clients must have the second_name')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length=50)
    grade = models.IntegerField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = ClientManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
