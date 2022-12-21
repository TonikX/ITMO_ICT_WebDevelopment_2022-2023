# Практическая работа №3

## Практика 3.2

Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:

### Запрос 1
> Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):

```python
In [22]: Auto.objects.filter(mark_car="Toyota")
Out[22]: <QuerySet [<Auto: Auto object (5)>, <Auto: Auto object (6)>]>
```
### Запрос 2
> Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```python
In [46]: Owner.objects.filter(first_name="Anna")
Out[46]: <QuerySet [<Owner: Owner object (1)>]>
```
### Запрос 3
> Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```python
In [50]: id_get = Owner.objects.all()[2].id
In [51]: License.objects.get(id_owner=id_get)
Out[51]: <License: License object (2)>
```
### Запрос 4
> Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
```python
for i in range(len(Car.objects.filter(color="red"))):
    print(Car.objects.filter(color="red")[i])

>>> Car object (5)
>>> Car object (8)
```
###Запрос 5
> Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```python
In [53]: Owning.objects.filter(start_date__gte="2020-01-01")
Out[53]: <QuerySet [<Owning: Owning object (3)>, <Owning: Owning object (4)>, <Ownerdhip: Ownerdhip object (5)>, <Ownerdhip: Ownerdhip object (6)>]>
```
## Практика 3.3
Описание: необходимо реализовать следующие запросы:

Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:
```python
In [60]: License.objects.aggregate(date_of_license=Min("date_of_license"))
Out[60]: {'date_of_license': datetime.date(2010, 1, 1)}
```
Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```python
In [62]: Owning.objects.aggregate(start_date=Max("start_date"))
Out[62]: {'start_date': datetime.date(2016, 1, 1)}
```
Запрос 3
Выведите количество машин для каждого водителя:
```python
In [64]: from django.db.models import Count

In [65]: Owning.objects.values("id_owner").annotate(Count("id_car"))
Out[65]: <QuerySet [{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1}, {'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1}, {'id_owner': 5, 'id
_car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]>
```
Запрос 4
Подсчитайте количество машин каждой марки:
```python
In [66]: Auto.objects.values("mark_car").annotate(Count("id_car"))
Out[66]: <QuerySet [{'mark_car': 'Audi', 'id_car__count': 2}, {'mark_car': 'BMW', 'id_car__count': 2}, {'mark_car': 'Toyota', 'id_car__count': 2}]>
```
Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```python
In [79]: Owner.objects.order_by("driver_license__date_of_license")
Out[79]: <QuerySet [<Owner: Owner object (1)>, <Owner: Owner object (2)>, <Owner: Owner object (3)>, <Owner: Owner object (4)>, <Owner: Owner objec
t (5)>, <Owner: Owner object (6)>]>
```