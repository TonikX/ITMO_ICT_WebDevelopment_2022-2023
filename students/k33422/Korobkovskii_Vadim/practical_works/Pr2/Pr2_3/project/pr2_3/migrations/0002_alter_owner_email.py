# Generated by Django 4.1.2 on 2022-10-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr2_3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
