from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Owner(AbstractUser):
    username = models.CharField(_("username"), max_length=150, unique=True)
    password = models.CharField(max_length=30, null=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField(null=True, blank=True)

    passport = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    national = models.CharField(max_length=30, null=True, blank=True)


class Auto(models.Model):
    number = models.CharField(max_length=15)
    mark = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.mark} , {self.number}"



class License(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type_license = models.CharField(max_length=10)
    date_get = models.DateField()


class Owning(models.Model):
    owner_auto = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    auto_id = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True, blank=True)

    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
