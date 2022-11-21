# Generated by Django 4.1.3 on 2022-11-02 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('birthday', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=15)),
                ('vehicle_brand', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('vehicle_color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField(null=True)),
                ('id_owner', models.ManyToManyField(to='First_app.carowner')),
                ('id_vehicle', models.ManyToManyField(to='First_app.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10)),
                ('license_type', models.CharField(max_length=10)),
                ('issue_date', models.DateTimeField()),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First_app.carowner')),
            ],
        ),
    ]
