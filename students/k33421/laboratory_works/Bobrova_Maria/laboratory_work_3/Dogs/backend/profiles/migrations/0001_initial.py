# Generated by Django 4.1.3 on 2022-11-14 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nike",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="НикНейм"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile/",
                        verbose_name="Аватар",
                    ),
                ),
                ("name", models.CharField(default="default", max_length=100)),
                ("surname", models.CharField(default="default", max_length=100)),
                (
                    "follow",
                    models.ManyToManyField(
                        related_name="follow_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Подписчики",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Профиль",
                "verbose_name_plural": "Профили",
            },
        ),
    ]