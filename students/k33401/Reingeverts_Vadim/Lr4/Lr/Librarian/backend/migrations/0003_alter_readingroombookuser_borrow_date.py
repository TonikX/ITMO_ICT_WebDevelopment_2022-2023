# Generated by Django 4.1.5 on 2023-03-09 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_book_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingroombookuser',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]