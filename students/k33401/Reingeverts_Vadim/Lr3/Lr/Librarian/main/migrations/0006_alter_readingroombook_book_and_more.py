# Generated by Django 4.1.5 on 2023-02-04 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_readingroombook_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingroombook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
        migrations.AlterUniqueTogether(
            name='readingroombook',
            unique_together={('book', 'reading_room')},
        ),
    ]
