# Generated by Django 4.1.3 on 2022-11-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0003_alter_plannedconference_options_comment_date"),
    ]

    operations = [
        migrations.AlterModelOptions(name="comment", options={"ordering": ["date"]},),
        migrations.AlterField(
            model_name="comment",
            name="date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
