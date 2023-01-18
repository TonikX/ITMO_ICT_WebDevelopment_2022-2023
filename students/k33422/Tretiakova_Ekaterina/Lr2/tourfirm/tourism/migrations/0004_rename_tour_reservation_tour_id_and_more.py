# Generated by Django 4.1.2 on 2022-10-23 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_rename_tour_id_reservation_tour_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='tour',
            new_name='tour_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='tourist_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
