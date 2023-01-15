# Практическая работа №3



## Практика 3.2

Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:

### Запрос 1
> Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):

```python
>>> Auto.objects.filter(mark="Toyota")     
<QuerySet [<Auto: Toyota , T0008>, <Auto: Toyota , T009>]>

```
### Запрос 2
> Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```python
>>> Owner.objects.filter(first_name="Maria") 
<QuerySet [<Owner: maria>, <Owner: Maria_Drobisheva>]>

```
### Запрос 3
> Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```python
>>> License.objects.get(owner_id=Owner.objects.get(id=1))
<License: License object (1)>


```
### Запрос 4
> Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
```python
Owner.objects.filter(owner__auto_id__color='black')
<QuerySet [<Owner: Olga>, <Owner: Roman>, <Owner: Olga>]>

```
###Запрос 5
> Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```python
>>> Owner.objects.filter(owner__date_start__gte="2022-05-01")  
<QuerySet [<Owner: Olga>, <Owner: Roman>, <Owner: Egor>, <Owner: fluff>, <Owner: maria>, <Owner: Olga>]>

```
## Практика 3.3
Описание: необходимо реализовать следующие запросы:

Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:
```python
>>> License.objects.aggregate(date_of_license=Min("date_get"))
{'date_of_license': datetime.date(2022, 10, 2)}
```
Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```python
>>> Owning.objects.aggregate(start_date=Max("date_start"))   
{'start_date': datetime.date(2022, 12, 5)}

```
Запрос 3
Выведите количество машин для каждого водителя:
```python
>>> Owning.objects.values("owner_auto").annotate(Count("auto_id")) 
<QuerySet [{'owner_auto': 1, 'auto_id__count': 2}, {'owner_auto': 2, 'auto_id__count': 1}, {'owner_auto': 3, 'auto_id__count': 1}, {'owner_auto': 5, 'auto_id__count': 1}, {
'owner_auto': 6, 'auto_id__count': 1}]>

```
Запрос 4
Подсчитайте количество машин каждой марки:
```python
<QuerySet [{'mark': 'A', 'id__count': 5}, {'mark': 'Toyota', 'id__count': 2}]>

```
Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```python
>>> License.objects.values("owner_id").order_by("date_get") 
<QuerySet [{'owner_id': 1}, {'owner_id': 2}]>

```