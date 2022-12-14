# Generated by Django 4.1.1 on 2022-11-21 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_car_owner_address_car_owner_nationality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver_license',
            name='id_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ownerdhip',
            name='id_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='project_first_app.car'),
        ),
        migrations.AlterField(
            model_name='ownerdhip',
            name='id_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
