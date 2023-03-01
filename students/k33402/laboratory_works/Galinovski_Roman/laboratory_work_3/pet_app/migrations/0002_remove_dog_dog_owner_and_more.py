from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='streinght',
        ),
        migrations.RemoveField(
            model_name='expertparticipation',
            name='num',
        ),
        migrations.RemoveField(
            model_name='expertparticipation',
            name='marks',
        ),
        migrations.RemoveField(
            model_name='sponsorship',
            name='add',
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='owner', related_query_name='owner', to='pet_app.owner', verbose_name='Owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expertparticipation',
            name='dateof_reg_exp',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expertparticipation',
            name='status',
            field=models.CharField(choices=[('Participated', 'Participated'), ('Suspended', 'Suspended'), ('Not allowed', 'Not allowed'), ('Absence', 'Absence')], default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='dateof_sign',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='club',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(choices=[('Achihuahua', 'Achihuahua'), ('Apchihuahua', 'Apchihuahua'), ('Pudel', 'Pudel'), ('Sobaka', 'Sobaka'), ('Dobel', 'Dobel'), ('Ovcharka', 'Ovcharka'), ('Doberman', 'Doberman')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='classof_dog',
            field=models.CharField(choices=[('Show', 'Dogs of show class'), ('Breed', 'Dogs of breed class'), ('Pet', 'Dogs of pet class')], max_length=250),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dad_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='document',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='dog',
            name='full_age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='info',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='dog',
            name='last_vaccination',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dog',
            name='mom_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='month_age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='bill',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not paid', 'Not paid')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='checkup',
            field=models.CharField(choices=[('Passed', 'Medical examination was successfully passed'), ('Not passed', 'Medical examination was not passed')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='dateof_checkup',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='dateof_reg_dog',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='dog_status',
            field=models.CharField(choices=[('Participated', 'Participated'), ('Suspended', 'Suspended'), ('Not allowed', 'Not allowed'), ('Absence', 'Absence')], max_length=100),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='show_dog_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dogparticipation',
            name='show_medal',
            field=models.CharField(choices=[('Gold', 'Gold for first place'), ('Silver', 'Silver for second place'), ('Bronze', 'Bronze for third place'), ('Audience award', 'Medal as audience sympathy prize')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_club', related_query_name='exp_club', to='pet_app.club', verbose_name='Club'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='expert',
            name='passport',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='expert',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='expert',
            name='surname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='expertparticipation',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grading',
            name='first_grade',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='grading',
            name='second_grade',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='grading',
            name='sum',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='grading',
            name='third_grade',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='passport',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='surname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='owner',
            name='passport',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='surname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='show',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='show',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='show',
            name='dateof_begin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='dateof_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='show',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', related_query_name='org', to=settings.AUTH_USER_MODEL, verbose_name='Organizer'),
        ),
        migrations.AlterField(
            model_name='show',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='show',
            name='typeof_show',
            field=models.CharField(choices=[('Mono', 'Monobreed exhibition'), ('Poly', 'Polybreed exhibition')], max_length=250),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='breedof_show',
            field=models.CharField(choices=[('Corgi', 'Corgi'), ('German shepherd', 'German shepherd'), ('Beagle', 'Beagle'), ('Poodle', 'Poodle'), ('Retriever', 'Retriever'), ('Samoyed', 'Samoyed'), ('Doberman', 'Doberman')], max_length=50),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='numberof_ring',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='show_class',
            field=models.CharField(choices=[('Puppy', '1-9 m.o'), ('Junior', '9-24 m.o'), ('Open', '15+ m.o'), ('Work', '15+ m.o with certificate'), ('Champions', '15+ m.o with champion certificate'), ('Veteran', '8+ y.o')], max_length=200),
        ),
        migrations.AlterField(
            model_name='showschedule',
            name='timeof_show',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='contract_number',
            field=models.IntegerField(unique=True),
        ),
    ]
