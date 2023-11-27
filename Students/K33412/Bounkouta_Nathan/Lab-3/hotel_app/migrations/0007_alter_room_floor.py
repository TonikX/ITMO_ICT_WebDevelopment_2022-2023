from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0006_alter_room_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.CharField(default=0, max_length=10, verbose_name='Floor'),
        ),
    ]