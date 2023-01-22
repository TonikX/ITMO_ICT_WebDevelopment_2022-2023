from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=200, null=True)),
                ('number', models.IntegerField(null=True, unique=True)),
                ('car_class', models.CharField(choices=[('Drag', 'Drag'), ('Sport', 'Sportscar'), ('Off', 'Off-road')], max_length=200, null=True)),
                ('speed', models.IntegerField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('mileage', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('com_type', models.CharField(choices=[('Cooperation', 'Cooperation'), ('Race', 'Race'), ('Other', 'Other')], max_length=11, null=True)),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('team', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(choices=[('ES', 'Spain'), ('IT', 'Italy'), ('FR', 'France'), ('DE', 'Deutschland')], max_length=2, null=True)),
                ('driver_class', models.CharField(choices=[('Drag', 'Drag racer'), ('Sport', 'Sports car racer'), ('Off', 'Off-road racer')], max_length=5, null=True)),
                ('age', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_date', models.DateField(null=True)),
                ('race_type', models.CharField(choices=[('Drag', 'Drag racing'), ('Sport', 'Sports car racing'), ('Off', 'Off-road racing')], max_length=200, null=True)),
                ('length', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('place', models.IntegerField(blank=True, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Car')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Driver')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Race')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='registrations',
            field=models.ManyToManyField(blank=True, through='races.Registration', to='races.Driver'),
        ),
        migrations.AddField(
            model_name='comment',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Driver'),
        ),
        migrations.AddField(
            model_name='comment',
            name='race',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Race'),
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='races.Driver'),
        ),
    ]
