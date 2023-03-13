# Generated by Django 4.1.7 on 2023-03-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory_work_3_app', '0003_bookinstancemodel_readermodel_roommodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='readermodel',
            name='books_instances',
            field=models.ManyToManyField(related_name='reader_book_instance', through='laboratory_work_3_app.ReaderBookModel', to='laboratory_work_3_app.bookinstancemodel'),
        ),
    ]
