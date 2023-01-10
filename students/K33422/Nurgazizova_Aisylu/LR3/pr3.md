Web-программирование 2023
========================
Нургазизова Айсылу, Куканова Ульяна K33422
-------------------------
Практическая работа 3.1
Задание 3.1.1
Описание: напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.
- models.py 
```python
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class OwnerUser(AbstractUser):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class License(models.Model):
    user = get_user_model()
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=False)
    number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date = models.DateField(null=False)

    def __str__(self):
        return self.number

class Car(models.Model):
    gos_number = models.CharField(max_length=15, null=False)
    mark = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)
    user = get_user_model()
    owner = models.ManyToManyField(user, through='Ownership')

    def __str__(self):
        return self.gos_number

class Ownership(models.Model):
    user = get_user_model()
    owner = models.ForeignKey(user, on_delete=models.CASCADE, related_name="start_d", null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    date_start = models.DateField(null=False)
    date_end = models.DateField(null=True)
```
Создание автовладельцев, автомобилей, водительских прав, владения автомобилями(шаблон)
```python
Car.objects.create(gos_number="", mark="", model="", color="", owner_id = "")
OwnerUser.objects.create(username="", first_name="", last_name="")
License.objects.create(number="", type = "", date = "")
Ownership.objects.create(car = "", date_start = "")
```
Задание 3.1.2
Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:
Запрос 1
Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
```python
In [12]: Car.objects.filter(mark='Chevrolet')
Out[12]: <QuerySet [<Car: 0412>, <Car: 0903>, <Car: 0908>, <Car: 0908>]>
```
Запрос 2
Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```python
In [15]: OwnerUser.objects.filter(first_name='Aisylu')
Out[15]: <QuerySet [<OwnerUser: Nurgazizova, Aisylu>]>
```
Запрос 3
Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```python
In [17]: License.objects.filter(owner_id=6)
Out[17]: <QuerySet [<License: 06130>]>
```
Запрос 4
Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
```python
In [18]: OwnerUser.objects.filter(car__color = 'brown')
Out[18]: <QuerySet [<OwnerUser: Nurgazizova, Aisylu>]>
```
Запрос 5
Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```python
In [19]: OwnerUser.objects.filter(start_d__date_start__year__gt="2018")
Out[19]: <QuerySet [<OwnerUser: Nurgazizova, Aisylu>, <OwnerUser: Kim, Seokjin>, <OwnerUser: Kim, Seokjin>]>
```
Задание 3.1.3
Описание: необходимо реализовать следующие запросы:
Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:
```python
In [23]: License.objects.aggregate(high=Min("date"))
Out[23]: {'high': datetime.date(2017, 3, 4)}
```
Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```python
In [24]: Ownership.objects.aggregate(high=Max("date_start"))
Out[24]: {'high': datetime.date(2021, 9, 7)}
```
Запрос 3
Выведите количество машин для каждого водителя:
```python
In [25]: Car.objects.values("owner").annotate(Count("id"))
Out[25]: <QuerySet [{'owner': None, 'id__count': 2}, {'owner': 1, 'id__count': 1}, {'owner': 6, 'id__count': 2}]>
```
Запрос 4
Подсчитайте количество машин каждой марки:
```python
In [26]: Car.objects.values("mark").annotate(Count("id"))
Out[26]: <QuerySet [{'mark': 'Chevrolet', 'id__count': 4}, {'mark': 'КАМАЗ', 'id__count': 1}]>
```
Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```python
In [27]: License.objects.order_by("date")
Out[27]: <QuerySet [<License: 06130>, <License: 3456>, <License: 12345>]>
```