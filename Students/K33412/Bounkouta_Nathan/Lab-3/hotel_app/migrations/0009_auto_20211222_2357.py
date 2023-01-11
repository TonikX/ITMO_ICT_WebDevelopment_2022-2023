from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0008_alter_room_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(null=True, verbose_name='Floor'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.CharField(max_length=20, null=True, verbose_name='Price'),
        ),
    ]