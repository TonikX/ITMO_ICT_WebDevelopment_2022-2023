# Generated by Django 4.1.4 on 2022-12-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='library_card_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
