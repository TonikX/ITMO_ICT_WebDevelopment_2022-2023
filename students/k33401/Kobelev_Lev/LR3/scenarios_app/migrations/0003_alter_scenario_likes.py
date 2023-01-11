# Generated by Django 4.1.2 on 2022-12-14 21:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("scenarios_app", "0002_alter_scenario_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scenario",
            name="likes",
            field=models.ManyToManyField(
                null=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
