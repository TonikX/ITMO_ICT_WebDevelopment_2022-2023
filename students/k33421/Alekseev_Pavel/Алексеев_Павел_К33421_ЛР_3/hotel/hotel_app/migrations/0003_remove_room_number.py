# Generated by Django 4.1.4 on 2022-12-13 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0002_rename_passport_employee_id_emp"),
    ]

    operations = [
        migrations.RemoveField(model_name="room", name="number",),
    ]
