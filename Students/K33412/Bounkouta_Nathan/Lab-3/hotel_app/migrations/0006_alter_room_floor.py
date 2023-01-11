from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0005_alter_room_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(default=0, verbose_name='Floor'),
        ),
    ]