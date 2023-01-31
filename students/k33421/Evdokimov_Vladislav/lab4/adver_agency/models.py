from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    tel = models.CharField("Телефон", max_length=12, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return "{}".format(self.username)


class Client(models.Model):

    legal_entity = models.CharField(max_length=60, verbose_name='Юридическое лицо')
    contact_person = models.CharField(max_length=60, verbose_name='Контактное лицо')
    phone_num = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(max_length=30, verbose_name='Электронный адрес')
    bank_details = models.CharField(max_length=30, verbose_name='Банковские реквизиты')

    def __str__(self):
        return "{}-{}".format(self.contact_person, self.legal_entity)


class ServicesPL(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование услуги')
    description_service = models.CharField(max_length=150, verbose_name='Характеристики')
    price = models.CharField(max_length=30, verbose_name='Стоимость услуги')

    def __str__(self):
        return self.title


class MaterialsPL(models.Model):

    title = models.CharField(max_length=50, verbose_name='Наименование материала')
    description_material = models.CharField(max_length=150, verbose_name='Характеристики')
    price = models.CharField(max_length=30, verbose_name='Цена')

    def __str__(self):
        return self.title


class Staff(models.Model):

    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    phone_num = models.CharField(max_length=12, verbose_name='Номер телефона')
    specialty = models.CharField(max_length=50, verbose_name='Специализация')

    def __str__(self):
        return self.full_name


class Request(models.Model):

    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Заказчик', related_name="requests_of_user")
    req_date = models.DateField(verbose_name='Дата заявки')
    workload = models.CharField(max_length=30, verbose_name='Объем работ')
    start_date = models.DateField(verbose_name='Дата начала работы')
    end_date = models.DateField(verbose_name='Дата окончания работы')
    final_price = models.CharField(max_length=30, verbose_name='Итоговая стоимость')
    status_types = (
        ('Не оплачено', 'Не оплачено'),
        ('Оплачено', 'Оплачено'),
    )
    status = models.CharField(max_length=20, choices=status_types, verbose_name='Состояние')
    payment = models.DateField(verbose_name='Дата оплаты', null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.client.legal_entity, self.req_date)


class ChosenServices(models.Model):

    service = models.ForeignKey('ServicesPL', verbose_name='Выбранная услуга', on_delete=models.CASCADE)
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE, related_name="services_in_request")
    total_cost = models.CharField(max_length=30, verbose_name='Общая стоимость услуг')


class ChosenMaterials(models.Model):

    material = models.ForeignKey('MaterialsPL', verbose_name='Выбранный материал', on_delete=models.CASCADE)
    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    total_cost = models.CharField(max_length=30, verbose_name='Общая стоимость материалов')
    amount = models.IntegerField(verbose_name='Количество материалов(шт.)')


class WorkGroup(models.Model):

    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', verbose_name='Сотрудники', on_delete=models.CASCADE)


class PaymentOrder(models.Model):

    req = models.ForeignKey('Request', verbose_name='Заявка', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', verbose_name='Клиент', on_delete=models.CASCADE)
    pay_date = models.DateField(verbose_name='Оплатить до')
