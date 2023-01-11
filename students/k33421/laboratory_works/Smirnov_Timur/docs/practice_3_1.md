# Практическая работа 3.1

## Задание 1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.

### Модели


`models.py`

```python
from django.db import models

class Transport_owner(models.Model):
    id_owner = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    date_birthday = models.DateField()


class Transport(models.Model):
    id_car = models.IntegerField(primary_key=True)
    gov_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE, related_name="ownership")
    id_car = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date_start = models.DateField()
    sate_end = models.DateField(null=True)


class License(models.Model):
    id_doc = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE)
    number_doc = models.CharField(max_length=10, null=False)
    type_doc = models.CharField(max_length=10, null=False)
    date_start_doc = models.DateField()
```

Перейдем в shell и создадим автовладельцев

```python
Transport_owner(1, 'Фамилия1', 'Имя1', '1902-01-1').save()
Transport_owner(2, 'Фамилия2', 'Имя2', '1902-01-2').save()
Transport_owner(3, 'Фамилия3', 'Имя3', '1902-01-3').save()
Transport_owner(4, 'Фамилия4', 'Имя4', '1902-01-4').save()
Transport_owner(5, 'Фамилия5', 'Имя5', '1902-01-5').save()
Transport_owner(6, 'Фамилия6', 'Имя6', '1902-01-6').save()
```

Создадим автомобили

```python
Transport(0, 'A123BC', 'Brand0', 'Model0', 'green').save()
Transport(1, 'A124BC', 'Brand1', 'Model1', 'red').save()
Transport(2, 'A125BC', 'Brand2', 'Model2', 'black').save()
Transport(3, 'A126BC', 'Brand3', 'Model3', 'blue').save()
Transport(4, 'A127BC', 'Brand4', 'Model4', 'blue').save()
Transport(5, 'A128BC', 'Brand5', 'Model5', 'black').save()
Transport(6, 'A129BC', 'Brand6', 'Model6', 'blue').save()
```

Водительские права

```python
License('1', '1', 'num1', 'type1', '1995-05-1').save()
License('2', '2', 'num2', 'type2', '1995-05-2').save()
License('3', '3', 'num3', 'type3', '1995-05-3').save()
License('4', '4', 'num4', 'type4', '1995-05-4').save()
License('5', '5', 'num5', 'type5', '1995-05-5').save()
License('6', '6', 'num6', 'type6', '1995-05-6').save()
```

Добавим владение автомобилями

```python
Ownership('1', '1', '1', '2000-08-1', '2010-08-1').save()
Ownership('2', '2', '2', '2000-08-2', '2010-08-2').save()
Ownership('3', '3', '3', '2000-08-3', '2010-08-3').save()
Ownership('4', '4', '4', '2000-08-4', '2010-08-4').save()
Ownership('5', '5', '5', '2000-08-5', '2010-08-5').save()
Ownership('6', '6', '6', '2000-08-6', '2010-08-6').save()
```

## Задание 2

По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

```bash
>>> Transport.objects.filter(brand="Brand3")
<QuerySet [<Transport: Transport object (3)>]>
```

- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

```bash
>>> Transport_owner.objects.filter(first_name="Имя5")
<QuerySet [<Transport_owner: Transport_owner object (5)>]>
```

- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)

```bash
>>> needed_id = Transport_owner.objects.all()[2].id_owner
>>> License.objects.get(id_owner=needed_id)
<License: License object (3)>
```

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

```bash
>>> Transport_owner.objects.filter(ownership__id_car__color='blue')
<QuerySet [
<Transport_owner: Transport_owner object (3)>,
<Transport_owner: Transport_owner object (4)>,
<Transport_owner: Transport_owner object (6)>]>
```

- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

```bash
>>> Transport_owner.objects.filter(ownership__date_start='2000-01-01')
<QuerySet [<Transport_owner: Transport_owner object (1)>, <Transport_owner: Transport_owner object (2)>,
<Transport_owner: Transport_owner object (3)>,
<Transport_owner: Transport_owner object (4)>,
<Transport_owner: Transport_owner object (5)>,
<Transport_owner: Transport_owner object (6)>]>
```

## Задание 3

Необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения

```bash
>>> License.objects.aggregate(date_start_doc=Min("date_start_doc"))
{'date_start_doc': datetime.date(1995, 5, 1)}
```

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе

```bash
>>> Ownership.objects.aggregate(date_start=Max("date_start"))
{'date_start': datetime.date(2000, 8, 6)}
```

- Выведите количество машин для каждого водителя

```bash
>>> Ownership.objects.values("id_owner").annotate(Count("id_car"))
<QuerySet
[{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1},
{'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1},
{'id_owner': 5, 'id_car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]
```

- Подсчитайте количество машин каждой марки

```bash
>>> Transport.objects.values("brand").annotate(Count("id_car"))
<QuerySet
[{'brand': 'Brand3', 'id_car__count': 1}, {'brand': 'Brand4', 'id_car__count': 3},
{'brand': 'Brand5', 'id_car__count': 1}, {'brand': 'Brand6', 'id_car__count': 1}]
```

- Отсортируйте всех автовладельцев по дате выдачи удостоверения (Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct()

```bash
>>> sort_by_date = License.objects.all().order_by("date_start_doc")
>>> for i in sort_by_date:
...     needed_id = i.id_owner.id_owner
...     print( Ownership.objects.filter(id_owner__id_owner=needed_id) )
<QuerySet [<Ownership: Ownership object (4)>]>
<QuerySet [<Ownership: Ownership object (1)>]>
<QuerySet [<Ownership: Ownership object (2)>]>
<QuerySet [<Ownership: Ownership object (3)>]>
<QuerySet [<Ownership: Ownership object (5)>]>
<QuerySet [<Ownership: Ownership object (6)>]>
```
