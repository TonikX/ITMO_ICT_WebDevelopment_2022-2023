import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_entity', models.CharField(max_length=60, verbose_name='Юридическое лицо')),
                ('contact_person', models.CharField(max_length=60, verbose_name='Контактное лицо')),
                ('phone_num', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=30, verbose_name='Электронный адрес')),
                ('bank_details', models.CharField(max_length=30, verbose_name='Банковские реквизиты')),
            ],
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('phone_num', models.CharField(max_length=12, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_due', models.DateField(verbose_name='Срок платежа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.client', verbose_name='Клиент')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование материала')),
                ('description', models.CharField(max_length=150, verbose_name='Характеристики')),
                ('price', models.CharField(max_length=30, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_date', models.DateField(verbose_name='Дата заявки')),
                ('workload', models.CharField(max_length=30, verbose_name='Объем работ')),
                ('final_price', models.CharField(max_length=30, verbose_name='Итоговая стоимость')),
                ('status', models.CharField(choices=[('н', 'не оплачено'), ('о', 'оплачено')], max_length=20, verbose_name='Состояние')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.client', verbose_name='Заказчик')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesPL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('у', 'уличная реклама'), ('и', 'реклама в интерьере внутри помещения'), ('т', 'реклама на транспортных средствах'), ('п', 'печатная реклама')], max_length=20, verbose_name='Вид услуги')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование услуги')),
                ('price', models.CharField(max_length=30, verbose_name='Стоимость услуги')),
            ],
        ),
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала работы')),
                ('end_date', models.DateField(verbose_name='Дата окончания работы')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.executor', verbose_name='Исполнитель')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.request', verbose_name='Заявка')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(verbose_name='Дата оплаты')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.client', verbose_name='Клиент')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.invoice', verbose_name='Счет на оплату')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.request', verbose_name='Заявка')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='req',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.request', verbose_name='Заявка'),
        ),
        migrations.CreateModel(
            name='ChosenServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.CharField(max_length=30, verbose_name='Общая стоимость услуг')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.request', verbose_name='Заявка')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.servicespl', verbose_name='Выбранная услуга')),
            ],
        ),
        migrations.CreateModel(
            name='ChosenMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.CharField(max_length=30, verbose_name='Общая стоимость материалов')),
                ('amount', models.IntegerField(verbose_name='Количество материалов(шт.)')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.materialspl', verbose_name='Выбранный материал')),
                ('req', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adv_app.request', verbose_name='Заявка')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tel', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('role', models.CharField(choices=[('ad', 'admin'), ('ma', 'manager'), ('ac', 'accountant')], max_length=20)),
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
    ]