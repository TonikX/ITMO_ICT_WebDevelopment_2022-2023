# Generated by Django 4.1.7 on 2023-03-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practical_work_3_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carowner',
            options={},
        ),
        migrations.AlterModelManagers(
            name='carowner',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='password',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='username',
        ),
        migrations.AlterField(
            model_name='driverslicense',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practical_work_3_app.carowner'),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practical_work_3_app.carowner'),
        ),
    ]
