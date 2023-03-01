from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0002_remove_dog_dog_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(choices=[('Achihuahua', 'Achihuahua'), ('Apchihuahua', 'Apchihuahua'), ('Pudel', 'Pudel'), ('Sobaka', 'Sobaka'), ('Dobel', 'Dobel'), ('Ovcharka', 'Ovcharka'), ('Doberman', 'Doberman')], max_length=100),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='breedof_show',
            field=models.CharField(choices=[('Achihuahua', 'Achihuahua'), ('Apchihuahua', 'Apchihuahua'), ('Pudel', 'Pudel'), ('Sobaka', 'Sobaka'), ('Dobel', 'Dobel'), ('Ovcharka', 'Ovcharka'), ('Doberman', 'Doberman')], max_length=50),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='show_class',
            field=models.CharField(choices=[('Puppy', '1-9 m.o'), ('Junior', '9-24 m.o'), ('Open', '15+ m.o'), ('Work', '15+ m.o with certificate'), ('Champions', '15+ m.o with champion certificate'), ('Veteran', '8+ y.o')], max_length=200),
        ),
    ]
