from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='room_client',
        ),
        migrations.AddField(
            model_name='client',
            name='room_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel_app.room', verbose_name='Room'),
        ),
        migrations.RemoveField(
            model_name='room',
            name='client_room',
        ),
        migrations.AddField(
            model_name='room',
            name='client_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Client'),
        ),
    ]