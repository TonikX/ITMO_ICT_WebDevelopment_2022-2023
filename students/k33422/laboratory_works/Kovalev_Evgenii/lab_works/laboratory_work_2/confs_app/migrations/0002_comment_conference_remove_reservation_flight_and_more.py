from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('text', models.CharField(blank=True, max_length=400, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='passenger',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='flight',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='comment',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='confs_app.conference'),
        ),
    ]