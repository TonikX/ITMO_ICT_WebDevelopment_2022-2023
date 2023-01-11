from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_auto_20211222_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.IntegerField(null=True, verbose_name='Floor'),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.CharField(choices=[('$100', '$100'), ('$200', '$200'), ('$300', '$300')], default='-', max_length=20, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('single', 'single'), ('double', 'double'), ('triple', 'triple')], default='-', max_length=20, null=True, verbose_name='Type'),
        ),
    ]