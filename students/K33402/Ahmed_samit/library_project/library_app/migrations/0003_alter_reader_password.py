# Generated by Django 4.1.2 on 2022-12-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_reader_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
