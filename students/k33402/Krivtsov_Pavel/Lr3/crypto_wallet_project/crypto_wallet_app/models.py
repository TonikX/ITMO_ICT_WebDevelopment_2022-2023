from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Currency(models.Model):
    users = models.ManyToManyField(User, verbose_name="Владельцы", through="Ownership")
    name = models.CharField(verbose_name="Название", max_length=30, unique=True)
    abbreviation = models.CharField(verbose_name="Сокращение", max_length=5, unique=True)
    price = models.DecimalField(verbose_name="Цена за единицу", max_digits=19, decimal_places=10)
    count = models.IntegerField(verbose_name="Количество в обращении")
    daily_changes = models.FloatField(verbose_name="Изменение цены за день (%)")
    weekly_changes = models.FloatField(verbose_name="Изменение цены за неделю (%)")
    date_added = models.DateTimeField(verbose_name="Дата появления", auto_now=True)
    coinlib_id = models.PositiveIntegerField(verbose_name="Id на сайте Coinlib.io")
    image = models.CharField(verbose_name="Ссылка на изображение", max_length=1000)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Ownership(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, verbose_name="Валюта", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Количество валюты у пользователя", default=0)

    class Meta:
        unique_together = ('user', 'currency')

    def __str__(self):
        return f"{self.user.username} - {self.currency.name}"


class Tag(models.Model):
    title = models.CharField(verbose_name="Название", max_length=15, unique=True)

    def __str__(self):
        return self.title


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")
    title = models.CharField(verbose_name="Тема обсуждения", max_length=80)
    description = models.TextField(verbose_name="Описание")
    date_added = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.date_added}: {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)
    discussion = models.ForeignKey(Discussion, verbose_name="Обсуждение", on_delete=models.CASCADE)
    body = models.TextField(verbose_name="Тело сообщения")
    date_added = models.DateTimeField(verbose_name="Дата публикации", auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.date_added})"


class Transaction(models.Model):
    TR_TYPE = (
        ('b', 'buy'),
        ('s', 'sell')
    )

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    currency = models.ForeignKey(Currency, on_delete=models.RESTRICT)
    transaction_type = models.CharField(max_length=1, choices=TR_TYPE)
    count = models.IntegerField()
    transaction_amount = models.DecimalField(max_digits=40, decimal_places=20)
    transaction_time = models.DateTimeField(auto_now=True)
