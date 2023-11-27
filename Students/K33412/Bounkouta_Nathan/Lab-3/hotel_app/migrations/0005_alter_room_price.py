from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_auto_20211222_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Price'),
        ),
    ]