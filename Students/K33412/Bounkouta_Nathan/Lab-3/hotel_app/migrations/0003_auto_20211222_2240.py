from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_auto_20211222_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='room_client',
        ),
        migrations.RemoveField(
            model_name='room',
            name='client_room',
        ),
        migrations.AddField(
            model_name='client',
            name='room_booked',
            field=models.ManyToManyField(null=True, through='hotel_app.Booking', to='hotel_app.Room', verbose_name='Room'),
        ),
        migrations.AddField(
            model_name='room',
            name='client_in',
            field=models.ManyToManyField(null=True, through='hotel_app.Booking', to=settings.AUTH_USER_MODEL, verbose_name='Client'),
        ),
    ]