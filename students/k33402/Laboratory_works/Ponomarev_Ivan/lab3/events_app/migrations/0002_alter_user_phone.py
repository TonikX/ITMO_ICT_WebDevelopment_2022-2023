# Generated by Django 4.1.5 on 2023-03-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(default=79999999999),
        ),
    ]
