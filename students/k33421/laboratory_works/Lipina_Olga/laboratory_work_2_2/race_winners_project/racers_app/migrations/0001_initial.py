# Generated by Django 4.1.4 on 2022-12-12 13:48

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Racer",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=30, verbose_name="Фамилия")),
                (
                    "fathername",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Отчество"
                    ),
                ),
                (
                    "team_name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Название команды",
                    ),
                ),
                (
                    "user_descr",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание участника"
                    ),
                ),
                (
                    "car_descr",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание машины"
                    ),
                ),
                (
                    "experience",
                    models.IntegerField(blank=True, null=True, verbose_name="Опыт"),
                ),
                (
                    "type_user",
                    models.CharField(
                        choices=[("A", "Высший"), ("B", "Высокий"), ("C", "Иное")],
                        default="C",
                        max_length=30,
                        verbose_name="Класс участника",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Логин",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                (
                    "num_race",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Номер гонки"
                    ),
                ),
                (
                    "name_race",
                    models.CharField(max_length=50, verbose_name="Название гонки"),
                ),
                (
                    "date_race",
                    models.DateTimeField(
                        unique=True, verbose_name="Дата и время гонки"
                    ),
                ),
                (
                    "place_race",
                    models.CharField(max_length=50, verbose_name="Место гонки"),
                ),
                (
                    "first_place",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "second_place",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sec_place",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "third_place",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="th_pace",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegistrationRace",
            fields=[
                (
                    "num_reg",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Номер регистрации",
                    ),
                ),
                (
                    "num_race_reg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="racers_app.race",
                    ),
                ),
                (
                    "num_user_reg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id_review", models.AutoField(primary_key=True, serialize=False)),
                ("time_race", models.DateTimeField(verbose_name="Дата и время заезда")),
                (
                    "comment_time",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2022, 12, 12, 16, 48, 46, 543510),
                    ),
                ),
                (
                    "rate",
                    models.IntegerField(
                        blank=True,
                        default=10,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="Поставьте рейтинг",
                    ),
                ),
                (
                    "type_comment",
                    models.CharField(
                        choices=[
                            ("RACE_Q", "Вопрос о гонке"),
                            ("COLLAB_Q", "Вопрос о сотрудничестве"),
                            ("OTHER", "Иное"),
                        ],
                        max_length=30,
                        verbose_name="Тип комментария",
                    ),
                ),
                ("text", models.TextField(verbose_name="Комментарий к гонке")),
                (
                    "num_race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="racers_app.race",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]