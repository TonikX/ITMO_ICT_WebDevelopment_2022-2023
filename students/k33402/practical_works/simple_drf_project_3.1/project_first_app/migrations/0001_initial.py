# Generated by Django 4.1.2 on 2022-11-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id_car', models.IntegerField(primary_key=True, serialize=False)),
                ('car_number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarOwnerUser',
            fields=[
                ('id_owner', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id_ownership', models.IntegerField(primary_key=True, serialize=False)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowneruser')),
            ],
        ),
        migrations.CreateModel(
            name='DriversLicense',
            fields=[
                ('id_lic', models.IntegerField(primary_key=True, serialize=False)),
                ('type_lic', models.CharField(max_length=10)),
                ('exp_date', models.DateField()),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.carowneruser')),
            ],
        ),
    ]
