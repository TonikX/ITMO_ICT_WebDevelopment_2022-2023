# Generated by Django 4.1.4 on 2022-12-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library_app", "0004_remove_reader_passport_reader_reader_hall"),
    ]

    operations = [
        migrations.AddField(
            model_name="instancebook",
            name="instance_hall",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="library_app.hall",
                verbose_name="Зал",
            ),
        ),
    ]
