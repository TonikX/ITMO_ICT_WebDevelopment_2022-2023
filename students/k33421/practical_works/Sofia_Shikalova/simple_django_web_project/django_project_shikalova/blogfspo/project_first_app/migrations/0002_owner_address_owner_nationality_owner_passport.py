# Generated by Django 4.1.3 on 2022-12-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='passport',
            field=models.IntegerField(null=True),
        ),
    ]