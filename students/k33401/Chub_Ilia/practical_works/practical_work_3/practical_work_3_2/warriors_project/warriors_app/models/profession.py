from django.db.models import Model, CharField, TextField


class Profession(Model):
    title = CharField(max_length=120, verbose_name='Название')
    description = TextField(verbose_name='Описание')
