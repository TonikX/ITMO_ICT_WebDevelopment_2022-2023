# Generated by Django 4.1.1 on 2022-11-07 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transport",
            fields=[
                ("id_car", models.IntegerField(primary_key=True, serialize=False)),
                ("gov_number", models.CharField(max_length=15)),
                ("marka", models.CharField(max_length=20)),
                ("model_car", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Transport_owner",
            fields=[
                ("id_owner", models.IntegerField(primary_key=True, serialize=False)),
                ("last_name", models.CharField(max_length=30)),
                ("first_name", models.CharField(max_length=30)),
                ("date_birthday", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Ownership",
            fields=[
                (
                    "id_owner_car",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("date_start", models.DateField()),
                ("sate_end", models.DateField(null=True)),
                (
                    "id_car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.transport"
                    ),
                ),
                (
                    "id_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.transport_owner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver_doc",
            fields=[
                ("id_doc", models.IntegerField(primary_key=True, serialize=False)),
                ("number_doc", models.CharField(max_length=10)),
                ("type_doc", models.CharField(max_length=10)),
                ("date_start_doc", models.DateField()),
                (
                    "id_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.transport_owner",
                    ),
                ),
            ],
        ),
    ]
