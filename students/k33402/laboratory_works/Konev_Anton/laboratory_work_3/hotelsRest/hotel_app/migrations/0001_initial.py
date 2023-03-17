# Generated by Django 4.1.3 on 2022-12-04 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CleaningStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('middle_name', models.TextField()),
                ('last_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('middle_name', models.TextField()),
                ('last_name', models.TextField()),
                ('city', models.TextField()),
                ('passport', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(default='')),
                ('price', models.FloatField()),
                ('floor', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('room_type', models.TextField(choices=[('SINGLE', 'Single'), ('DOUBLE', 'Double'), ('TRIPLE', 'Triple')])),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('week_day', models.TextField(choices=[('SUNDAY', 'Sunday'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday')])),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel_app.cleaningstaff')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel_app.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotel_app.room')),
            ],
        ),
    ]
