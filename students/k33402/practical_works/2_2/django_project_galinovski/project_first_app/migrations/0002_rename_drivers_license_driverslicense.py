from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drivers_license',
            new_name='DriversLicense',
        ),
    ]