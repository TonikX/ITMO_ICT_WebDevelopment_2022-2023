# Практическая работа 3.1

## Задание 1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. 
Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. 
Результатом должны стать запросы и отображение созданных объектов.

### Модели


`models.py`

```python
from django.db import models


class Auto(models.Model):
    def __str__(self):
        return self.brand + " " + self.model

    state_num = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Owner(models.Model):
    def __str__(self):
        return self.last_name + " " + self.first_name

    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthdate = models.DateTimeField(null=True)


class Ownage(models.Model):
    def __str__(self):
        return self.auto_id.brand + ' ' + self.auto_id.model + ' is owned by ' + self.owner_id.last_name + ' ' + self.owner_id.first_name

    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, blank=True)
    auto_id = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True, blank=True)
    begin_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=True, blank=True)


class License(models.Model):
    def __str__(self):
        return 'License of: ' + self.owner_id.last_name + " " + self.owner_id.first_name

    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    license_num = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    issue_date = models.DateTimeField(null=False)

```

Перейдем в shell и создадим автовладельцев

```python
from simple_drf_project.models import *
Owner(1, 'Ivanov', 'Ivan', '2000-05-05').save()
Owner(2, 'Ivanov', 'Boris', '2000-05-05').save()
Owner(3, 'Ivanov', 'Sergey', '2000-05-05').save()
Owner(4, 'Ivanov', 'Vladislav', '2000-05-05').save()
Owner(5, 'Ivanov', 'Timofey', '2000-05-05').save()
Owner(6, 'Ivanov', 'Nikolay', '2000-05-05').save() 
```

Создадим автомобили

```python
Auto(0, 'A000BC', 'Toyota', 'Corolla', 'black').save()
Auto(1, 'A001BC', 'Toyota', 'Camry', 'white').save()
Auto(2, 'A002BC', 'Toyota', 'RAV-4', 'yellow').save()
Auto(3, 'A003BC', 'Volkswagen', 'Polo', 'green').save()
Auto(4, 'A004BC', 'Skoda', 'Rapid', 'blue').save()
Auto(5, 'A005BC', 'Hyundai', 'Sonata', 'purple').save()
Auto(6, 'A006BC', 'Ferrari', 'Spider', 'red').save() 
```

Водительские права

```python
License('1', '1', 'number1', 'B' , '2020-05-05').save()
License('2', '2', 'number2', 'B' , '2020-05-05').save()
License('3', '3', 'number3', 'B' , '2020-05-05').save()
License('4', '4', 'number4', 'B' , '2020-05-05').save()
License('5', '5', 'number5', 'B' , '2020-05-05').save()
License('6', '6', 'number6', 'B' , '2020-05-05').save() 
```

Добавим владение автомобилями

```python
Ownage('1', '1', '1', '2020-05-05', '2030-05-05').save()
Ownage('2', '2', '2', '2020-05-05', '2030-05-05').save()
Ownage('3', '3', '3', '2020-05-05', '2030-05-05').save()
Ownage('4', '4', '4', '2020-05-05', '2030-05-05').save()
Ownage('5', '5', '5', '2020-05-05', '2030-05-05').save()
Ownage('6', '6', '6', '2020-05-05', '2030-05-05').save() 
```

## Задание 2

По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

```bash
>>> Auto.objects.filter(brand='Toyota') 
 <QuerySet [<Auto: Toyota Corolla>, <Auto: Toyota Camry>, <Auto: Toyota RAV-4>]> 
```

- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

```bash
>>> Owner.objects.filter(first_name='Ivan') 
 <QuerySet [<Owner: Ivanov Ivan>]> 
```

- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)

```bash
>>> License.objects.get(id=(Owner.objects.all()[1].id)) 
 <License: License of: Ivanov Boris> 
```

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

```bash
>>> Owner.objects.filter(ownage__auto_id_id__color='blue')
 <QuerySet [<Owner: Ivanov Vladislav>]>
```

- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

```bash
>>> Owner.objects.filter(ownage__begin_date__range=['2010-01-01', '2023-03-10'])
<QuerySet [
<Owner: Ivanov Ivan>, 
<Owner: Ivanov Boris>, 
<Owner: Ivanov Sergey>, 
<Owner: Ivanov Vladislav>, 
<Owner: Ivanov Timofey>, 
<Owner: Ivanov Nikolay>]>
```

## Задание 3

Необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения

```bash
>>> from django.db.models import Min, Max, Avg
>>> License.objects.aggregate(issue_date=Min('issue_date'))
{'issue_date': datetime.datetime(2020, 5, 5, 0, 0, tzinfo=datetime.timezone.utc)}
```

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе

```bash
>>> Ownage.objects.aggregate(begin_date=Max('begin_date'))
{'begin_date': datetime.datetime(2020, 5, 5, 0, 0, tzinfo=datetime.timezone.utc)} 
```

- Выведите количество машин для каждого водителя

```bash
>>> from django.db.models import Count 
>>> Ownage.objects.values('owner_id_id').annotate(Count("auto_id_id"))
<QuerySet [{'owner_id_id': 1, 'auto_id_id__count': 1}, 
{'owner_id_id': 2, 'auto_id_id__count': 1}, 
{'owner_id_id': 3, 'auto_id_id__count': 1}, 
{'owner_id_id': 4, 'auto_id_id__count': 1}, 
{'owner_id_id': 5, 'auto_id_id__count': 1}, 
{'owner_id_id': 6, 'auto_id_id__count': 1}]> 
```

- Подсчитайте количество машин каждой марки

```bash
>>> Auto.objects.values('brand').annotate(Count('id')) 
<QuerySet [
{'brand': 'Ferrari', 'id__count': 1}, 
{'brand': 'Hyundai', 'id__count': 1}, 
{'brand': 'Skoda', 'id__count': 1}, 
{'brand': 'Toyota', 'id__count': 3}, 
{'brand': 'Volkswagen', 'id__count': 1}]> 
```

- Отсортируйте всех автовладельцев по дате выдачи удостоверения 
(Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct()

```bash
>>> sort_by_date = License.objects.all().order_by('issue_date')
>>> for i in sort_by_date:
...   needed_id = i.owner_id.id
...   print(Ownage.objects.filter(owner_id__id=needed_id)) 
<QuerySet [<Ownage: Toyota Camry is owned by Ivanov Ivan>]>
<QuerySet [<Ownage: Toyota RAV-4 is owned by Ivanov Boris>]>
<QuerySet [<Ownage: Volkswagen Polo is owned by Ivanov Sergey>]>
<QuerySet [<Ownage: Skoda Rapid is owned by Ivanov Vladislav>]>
<QuerySet [<Ownage: Hyundai Sonata is owned by Ivanov Timofey>]>
<QuerySet [<Ownage: Ferrari Spider is owned by Ivanov Nikolay>]> 
```
