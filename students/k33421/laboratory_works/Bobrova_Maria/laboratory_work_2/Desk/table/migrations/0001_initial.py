# Generated by Django 3.0.3 on 2022-11-08 19:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('with_additional_info', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Математика', 'Математика'), ('История', 'История'), ('КИГ', 'КИГ'), ('Программирование', 'Программирование'), ('Информатика', 'Информатика')], max_length=30, verbose_name='Предмет')),
                ('start_date', models.DateTimeField(verbose_name='Дата выдачи')),
                ('end_date', models.DateTimeField(verbose_name='Сдать до')),
                ('task_description', models.TextField(verbose_name='Описание')),
                ('fine_info', models.CharField(max_length=150, verbose_name='Информация о штрафах')),
                ('max_points', models.IntegerField(verbose_name='Максимальное количество баллов')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Homework')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(choices=[('K', 'K')], default='K', max_length=1, verbose_name='Литера')),
                ('number', models.IntegerField(choices=[(1, '3241'), (2, '3242')], default=1, verbose_name='Номер')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('subject', models.CharField(choices=[('Математика', 'Математика'), ('История', 'История'), ('КИГ', 'КИГ'), ('Программирование', 'Программирование'), ('Информатика', 'Информатика')], max_length=30, verbose_name='Предмет')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table.StudentGroup'),
        ),
        migrations.CreateModel(
            name='TeacherAnswerOnHomework',
            fields=[
                ('homework_answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='table.HomeworkAnswer')),
                ('points', models.IntegerField(default=0, verbose_name='Баллы')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('date', models.DateTimeField(auto_now=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table.StudentGroup')),
            ],
        ),
        migrations.AddField(
            model_name='homeworkanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Student'),
        ),
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='table.Teacher'),
        ),
    ]