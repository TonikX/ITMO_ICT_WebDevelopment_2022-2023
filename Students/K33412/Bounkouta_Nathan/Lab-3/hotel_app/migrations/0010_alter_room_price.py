from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0009_auto_20211222_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
    ]