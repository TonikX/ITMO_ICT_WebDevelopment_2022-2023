# Generated by Django 4.1.5 on 2023-01-23 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flightuser',
            options={'verbose_name': 'Flight Ticket', 'verbose_name_plural': 'Flight Tickets'},
        ),
    ]