## Описание 3.1 практической работы
Django заапросы и их выполнение.

<hr>

## Задание 3.1.1
`Описание:` напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, 
каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. 
Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. 
Результатом должны стать запросы и отображение созданных объектов. 

- `models.py`

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
    marka = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Transport, on_delete=models.CASCADE)
    date_start = models.DateField()
    sate_end = models.DateField(null=True)


class Driver_doc(models.Model):
    id_doc = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE, related_name="docs")
    number_doc = models.CharField(max_length=10, null=False)
    type_doc = models.CharField(max_length=10, null=False)
    date_start_doc = models.DateField()

```

> Создание автовладельцев
```python
Transport_owner(1, 'Alekseev', 'Paul', '2002-09-27').save()
Transport_owner(2, 'Knyezeva', 'Alisa', '2002-06-07').save()
Transport_owner(3, 'Alekseev', 'Aleksey', '1972-12-08').save()
Transport_owner(4, 'Alekseeva', 'Ekaterina', '1980-01-14').save()
Transport_owner(5, 'Svyatko', 'Paul', '2002-07-08').save()
Transport_owner(6, 'Kirichenko', 'Vladislav', '2003-11-18').save()
```
```python
for i in Transport_owner.objects.all():
    print(i)
    
Transport_owner object (1)
Transport_owner object (2)
Transport_owner object (3)
Transport_owner object (4)
Transport_owner object (5)
Transport_owner object (6)
```

> Создание автомобилей
```python
Transport(0, 'A001', 'MERSEDES-BENZ', 'GLE', 'BLACK').save()
Transport(1, 'B002', 'MERSEDES-BENZ', 'GLS', 'BLACK').save()
Transport(2, 'C003', 'MERSEDES-BENZ', 'Model2', 'BLACK').save()
Transport(3, 'D004', 'MERSEDES-BENZ', 'Model3', 'BLACK').save()
Transport(4, 'E005', 'PORSHE', 'PANAMERA', 'GREY').save()
Transport(5, 'F006', 'TAYOTA', 'LAND CRUSER PRADA', 'BLACK').save()
Transport(6, 'G007', 'LEXSUS', 'LX60', 'BLACK').save()
```

> Создание водительских прав
```python
Driver_doc('1', '1', '001', 'B', '2020-08-07').save()
Driver_doc('2', '2', '002', 'B', '2021-09-20').save()
Driver_doc('3', '3', '003', 'B', '1980-09-21').save()
Driver_doc('4', '4', '004', 'B', '1999-10-01').save()
Driver_doc('5', '5', '005', 'B', '2018-08-10').save()
Driver_doc('6', '6', '006', 'B', '2017-10-11').save()
```

> Присваивания автовладельцам автомобили
```python
Ownership('1', '1', '1', '2000-01-01', '2200-01-01').save()
Ownership('2', '2', '2', '2000-01-01', '2200-01-01').save()
Ownership('3', '3', '3', '2000-01-01', '2200-01-01').save()
Ownership('4', '4', '4', '2000-01-01', '2200-01-01').save()
Ownership('5', '5', '5', '2000-01-01', '2200-01-01').save()
Ownership('6', '6', '6', '2000-01-01', '2200-01-01').save()
```
<hr>

## Задание 3.1.2
`Описание:`По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
```python
Transport.objects.filter(marka="MERSEDES-BENZ")
<QuerySet [<Transport: Transport object (0)>, <Transport: Transport object (1)>, <Transport: Transport object (2)>, <Transport: Transport object (3)>]>
```

- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```python
Transport_owner.objects.filter(first_name="Paul")
<QuerySet [<Transport_owner: Transport_owner object (1)>, <Transport_owner: Transport_owner object (5)>]>
```

- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```python
needed_id = Transport_owner.objects.all()[2].id_owner
Driver_doc.objects.get(id_owner=needed_id)
<Driver_doc: Driver_doc object (3)>
```

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
```python
for i in range(len(Transport.objects.filter(color="BLACK"))):
...     print(Transport.objects.filter(color="BLACK")[i])
... 
Transport object (3)
Transport object (4)
Transport object (6)
```

- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```python
Ownership.objects.filter(date_start__gte="1936-01-01")
<QuerySet [<Ownership: Ownership object (1)>, <Ownership: Ownership object (2)>, <Ownership: Ownership object (3)>, 
<Ownership: Ownership object (4)>, <Ownership: Ownership object (5)>, 
<Ownership: Ownership object (6)>]>
```
<hr>

## Задание 3.1.3
`Описание:` необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения:
```python
Driver_doc.objects.aggregate(date_start_doc=Min("date_start_doc"))
{'date_start_doc': datetime.date(1933, 5, 1)}
```

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```python
Ownership.objects.aggregate(date_start=Max("date_start"))
{'date_start': datetime.date(1936, 9, 16)}
```

- Выведите количество машин для каждого водителя:
```python
Ownership.objects.values("id_owner").annotate(Count("id_car"))
<QuerySet 
[{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1}, 
{'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1}, 
{'id_owner': 5, 'id_car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]
>
```

- Подсчитайте количество машин каждой марки:
```python
Transport.objects.values("marka").annotate(Count("id_car"))
<QuerySet [{'marka': 'LEXSUS', 'id_car__count': 1}, {'marka': 'MERSEDES-BENZ', 'id_car__count': 4}, {'marka': 'PORSHE', 'id_car__count': 1}, {'marka': 'TAYOTA', 'id_car__count': 1}]>

```

- Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```python
sort_by_date = Driver_doc.objects.all().order_by("date_start_doc")
for i in sort_by_date:
...     needed_id = i.id_owner.id_owner
...     print( Ownership.objects.filter(id_owner__id_owner=needed_id) )
<QuerySet [<Ownership: Ownership object (4)>]>
<QuerySet [<Ownership: Ownership object (1)>]>
<QuerySet [<Ownership: Ownership object (2)>]>
<QuerySet [<Ownership: Ownership object (3)>]>
<QuerySet [<Ownership: Ownership object (5)>]>
<QuerySet [<Ownership: Ownership object (6)>]>
```
<hr>
