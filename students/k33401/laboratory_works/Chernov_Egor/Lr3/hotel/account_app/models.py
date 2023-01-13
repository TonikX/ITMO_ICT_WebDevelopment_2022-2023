from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from hotel_app.models import Hotel


class Guest(models.Model):
    user_g = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_guest", verbose_name='ID User')
    phone_guest = models.CharField(max_length=10, verbose_name="Phone")
    passport_guest = models.CharField(max_length=10, null=True, blank=True, verbose_name="Passport")


class Employee(models.Model):
    user_empl = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_employee",
                                     verbose_name='ID User')
    hotel_empl = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="hotel_employee", verbose_name='ID Hotel')
    phone_employee = models.CharField(max_length=10, verbose_name="Phone")
    position_employee = models.CharField(max_length=100, verbose_name="Position")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Guest.objects.create(user_g=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_staff:
        if Guest.objects.get(user_g=instance):
            Guest.objects.filter(user_g=instance).delete()
        Employee.objects.create(user_empl=instance)
    else:
        if Employee.objects.all():
            if Employee.objects.get(user_empl=instance):
                Employee.objects.filter(user_empl=instance).delete()
