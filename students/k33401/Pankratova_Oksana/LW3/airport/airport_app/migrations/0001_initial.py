# Generated by Django 4.2 on 2023-04-10 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('position', models.CharField(choices=[('s', 'stuard'), ('c', 'comander'), ('p', 'second pilot'), ('n', 'navigator')], max_length=20)),
                ('education', models.CharField(max_length=500)),
                ('experience', models.IntegerField()),
                ('passport', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7, unique=True)),
                ('type', models.CharField(max_length=10)),
                ('num_seats', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransitLanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport', models.CharField(max_length=30)),
                ('arr_dt', models.DateTimeField()),
                ('dep_dt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('air_departure', models.CharField()),
                ('air_arrival', models.CharField()),
                ('dep_dt', models.DateTimeField()),
                ('arr_dt', models.DateTimeField()),
                ('employee', models.ManyToManyField(related_name='flight', through='airport_app.Allowance', to='airport_app.employee')),
                ('plane', models.ManyToManyField(related_name='flight', to='airport_app.plane')),
                ('transit_land', models.ManyToManyField(related_name='flight', to='airport_app.transitlanding')),
            ],
        ),
        migrations.AddField(
            model_name='allowance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowance', to='airport_app.employee'),
        ),
        migrations.AddField(
            model_name='allowance',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowance', to='airport_app.flight'),
        ),
    ]
