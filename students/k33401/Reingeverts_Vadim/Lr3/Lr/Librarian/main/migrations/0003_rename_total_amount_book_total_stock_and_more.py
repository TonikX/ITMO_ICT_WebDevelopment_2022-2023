# Generated by Django 4.1.5 on 2023-02-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_readingroom_capacity_alter_readingroombook_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='total_amount',
            new_name='total_stock',
        ),
        migrations.RenameField(
            model_name='readingroombook',
            old_name='amount',
            new_name='stock',
        ),
    ]
