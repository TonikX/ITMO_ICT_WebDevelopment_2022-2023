# Generated by Django 4.1.7 on 2023-03-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_remove_ticket_ticket_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='can_buy',
            field=models.BooleanField(default=True),
        ),
    ]
