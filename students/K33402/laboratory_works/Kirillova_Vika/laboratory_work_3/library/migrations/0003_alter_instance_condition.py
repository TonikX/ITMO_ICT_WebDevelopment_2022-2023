# Generated by Django 4.1.3 on 2023-01-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_readerbook_book_bookinst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='condition',
            field=models.CharField(choices=[('х', 'хорошее'), ('у', 'удовлетворительное'), ('п', 'плохое')], max_length=1, verbose_name='Состояние экземпляра'),
        ),
    ]
