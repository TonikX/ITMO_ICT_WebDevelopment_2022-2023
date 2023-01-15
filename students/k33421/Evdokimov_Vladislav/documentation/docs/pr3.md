#Практическая работа №3.1

Модель БД.
```
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
    id_owner = models.ForeignKey(Transport_owner, on_delete=models.CASCADE)
    number_doc = models.CharField(max_length=10, null=False)
    type_doc = models.CharField(max_length=10, null=False)
    date_start_doc = models.DateField()
```
===========================================================================

## Практическое задание 1:

### Создание сущностей


● Добавление автовладельцев.

```
Transport_owner(1, 'Surname1', 'Name1', '1992-01-1').save()
Transport_owner(2, 'Surname2', 'Name2', '1932-01-2').save()
Transport_owner(3, 'Surname3', 'Name3', '1942-01-3').save()
Transport_owner(4, 'Surname4', 'Name4', '1952-01-4').save()
Transport_owner(5, 'Surname5', 'Name5', '1962-01-5').save()
Transport_owner(6, 'Surname6', 'Name6', '1972-01-6').save()
```
● Добавление транспорта.
```
Transport(0, 'AAA0', 'Mark0', 'Model0', 'color').save()
Transport(1, 'AAA1', 'Mark1', 'Model1', 'color').save()
Transport(2, 'AAA2', 'Mark2', 'Model2', 'color').save()
Transport(3, 'AAA3', 'Mark3', 'Model3', 'color').save()
Transport(4, 'AAA4', 'Mark4', 'Model4', 'color').save()
Transport(5, 'AAA5', 'Mark5', 'Model5', 'color').save()
Transport(6, 'AAA6', 'Mark6', 'Model6', 'color').save()
```

● Связывание владельцев и автомобилей.
```
Ownership('1', '1', '1', '2000-01-1', '2004-01-1').save()
Ownership('2', '2', '2', '2000-01-1', '2004-01-1').save()
Ownership('3', '3', '3', '2000-01-1', '2004-01-1').save()
Ownership('4', '4', '4', '2000-01-1', '2004-01-1').save()
Ownership('5', '5', '5', '2000-01-1', '2004-01-1').save()
Ownership('6', '6', '6', '2000-01-1', '2004-01-1').save()
```

● Добавление водительских прав.
```
Driver_doc('1', '1', 'num1', 'type1', '2000-01-1').save()
Driver_doc('2', '2', 'num2', 'type2', '2000-01-1').save()
Driver_doc('3', '3', 'num3', 'type3', '2000-01-1').save()
Driver_doc('4', '4', 'num4', 'type4', '2000-01-1').save()
Driver_doc('5', '5', 'num5', 'type5', '2000-01-1').save()
Driver_doc('6', '6', 'num6', 'type6', '2000-01-1').save()
Driver_doc('7', '6', 'num7', 'type7', '1996-01-1').save()
```

===========================================================================
## Практическое задание 2:

● Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
```
>>> Transport.objects.filter(marka="Mark5") 
<QuerySet [<Transport: Transport object (5)>]>
```
● Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):

```
>>> Transport_owner.objects.filter(first_name="Name2") 
<QuerySet [<Transport_owner: Transport_owner object (2)>]>
```

● Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):

```
>>> get_id = Transport_owner.objects.all()[3].id_owner 
>>> Driver_doc.objects.get(id_owner=get_id)            
<Driver_doc: Driver_doc object (4)>
```

● Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):

```
>>> Transport_owner.objects.filter(ownership__id_car__color='color')
<QuerySet [<Transport_owner: Transport_owner object (1)>, <Transport_owner: Transport_owner object (2)>, <Transport_owner: Transport_owner object (3)>, <Transport_owner: Transpo
rt_owner object (4)>, <Transport_owner: Transport_owner object (5)>, <Transport_owner: Transport_owner object (6)>]>
```

● Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):

```
>>> Transport_owner.objects.filter(ownership__date_start='2000-01-01') 
<QuerySet [<Transport_owner: Transport_owner object (1)>, <Transport_owner: Transport_owner object (2)>, <Transport_owner: Transport_owner object (3)>, <Transport_owner: Transpo
rt_owner object (4)>, <Transport_owner: Transport_owner object (5)>, <Transport_owner: Transport_owner object (6)>]>
```

===========================================================================
## Практическое задание 3:

● Вывод даты выдачи самого старшего водительского удостоверения:
```
>>> Driver_doc.objects.aggregate(date_start_doc=Min("date_start_doc"))  
{'date_start_doc': datetime.date(1996, 1, 1)}
```
● Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:

```
>>> Ownership.objects.aggregate(date_start=Max("date_start"))
{'date_start': datetime.date(2000, 1, 1)}
```

● Выведите количество машин для каждого водителя:

```
>>> Ownership.objects.values("id_owner").annotate(Count("id_car"))
<QuerySet [{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1}, {'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1}, {'id_owner': 5, 'i
d_car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]>
```

● Подсчитайте количество машин каждой марки:

```
>>> Transport.objects.values("marka").annotate(Count("id_car"))
<QuerySet [{'marka': 'Mark0', 'id_car__count': 1}, {'marka': 'Mark1', 'id_car__count': 1}, {'marka': 'Mark2', 'id_car__count': 1}, {'marka': 'Mark3', 'id_car__count': 1}, {'mark
a': 'Mark4', 'id_car__count': 1}, {'marka': 'Mark5', 'id_car__count': 1}, {'marka': 'Mark6', 'id_car__count': 1}]>
```


● Отсортируйте всех автовладельцев по дате выдачи удостоверения:

```
>>> Driver_doc.objects.all().order_by("date_start_doc")
<QuerySet [<Driver_doc: Driver_doc object (7)>, <Driver_doc: Driver_doc object (1)>, <Driver_doc: Driver_doc object (2)>, <Driver_doc: Driver_doc object (3)>, <Driver_doc: Drive
r_doc object (4)>, <Driver_doc: Driver_doc object (5)>, <Driver_doc: Driver_doc object (6)>]>
```

