# Generated by Django 4.1.5 on 2023-02-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_book_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookuser',
            name='returned_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]