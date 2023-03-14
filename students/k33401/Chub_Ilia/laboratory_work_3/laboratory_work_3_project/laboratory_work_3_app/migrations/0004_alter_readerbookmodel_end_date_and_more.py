# Generated by Django 4.1.7 on 2023-03-19 19:57

import datetime
from django.db import migrations, models
import laboratory_work_3_app.models.reader_book_model


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory_work_3_app', '0003_rename_book_readerbookmodel_book_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readerbookmodel',
            name='end_date',
            field=models.DateField(default=laboratory_work_3_app.models.reader_book_model.get_end_date),
        ),
        migrations.AlterField(
            model_name='readerbookmodel',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
