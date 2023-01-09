# Generated by Django 4.1.4 on 2022-12-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Читатель'), (2, 'Автор'), (3, 'Работник библиотеки')], default=1),
        ),
    ]