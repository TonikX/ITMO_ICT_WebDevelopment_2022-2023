# Практическая работа №3

## Задание 3.1.1
`Описание:` напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, 
каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. 
Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. 
Результатом должны стать запросы и отображение созданных объектов. 

`models.py`

```python
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class Owner(models.Model):
    id_owner = models.IntegerField(primary_key = True)
    last_name = models.CharField(max_length = 30, null = False)
    first_name = models.CharField(max_length = 30, null = False)
    birth_day = models.DateField(null = True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"ID:{self.id_owner} ({self.first_name} {self.last_name})"


class Certificate(models.Model):
    #OwnerUser = get_user_model()
    id_owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    cert_number = models.CharField(max_length = 10, null = False)
    cert_type = models.CharField(max_length = 10, null = False)
    date_of_issue = models.DateField()

    def __str__(self):
        return self.number


class Car(models.Model):
    #OwnerUser = get_user_model()
    id_car = models.IntegerField(primary_key = True)
    state_number = models.CharField(max_length = 15, null = False)
    brand = models.CharField(max_length = 20, null = False)
    model = models.CharField(max_length = 20, null = False)
    color =  models.CharField(max_length = 30, null = True)
    owner = models.ManyToManyField(Owner, through='Ownership')

    def __str__(self):
        return self.state_number


class Ownership(models.Model):
    id_ownership = models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null = True)

    def __str__(self):
        return f"{self.id_owner} | {self.id_car}"
```

> Для начала взглянем на уже имеющихся автовладельцев:
```python
>>> for i in Owner.objects.all():
...     print(i)
...
ID:0 (Sofia Shikalova)
ID:1 (Igor Polyakov)
ID:2 (Alisher Morgenshtern)
ID:3 (Maria Bobrova)
ID:4 (Sofia Bykova)
ID:5 (Ekaterina Tretyakova)
```

> Создадим ещё 6 автовладельцев:
```python
>>> Owner(6, 'Aniston', 'Jennifer').save()
>>> Owner(7, 'Pitt', 'Brad').save()
>>> Owner(8, 'DiCaprio', 'Leonardo').save()
>>> Owner(9, 'Damon', 'Matt').save()
>>> Owner(10, 'Bullok', 'Sandra').save()
>>> Owner(11, 'Witherspoon', 'Reese').save()
>>>
>>> for i in Owner.objects.all():
...     print(i)
...
ID:0 (Sofia Shikalova)
ID:1 (Igor Polyakov)
ID:2 (Alisher Morgenshtern)
ID:3 (Maria Bobrova)
ID:4 (Sofia Bykova)
ID:5 (Ekaterina Tretyakova)
ID:6 (Jennifer Aniston)
ID:7 (Brad Pitt)
ID:8 (Leonardo DiCaprio)
ID:9 (Matt Damon)
ID:10 (Sandra Bullok)
ID:11 (Reese Witherspoon)
```

> Посмотрим на уже имеющиеся автомобили:
```python
>>> for i in Car.objects.all():
...     print(i)
...
ID:0 (Alfa Romeo Giulietta H534KH)
ID:1 (Chrysler Crossfire O092EE)
ID:2 (Jaguar F-Type Roadster B926OK)
ID:3 (Bentley Continential GT C106AA)
ID:4 (Bugatti Chiron K492OO)
ID:5 (Rolls-Royce Phantom M333ME)
ID:6 (Lamborghini Huracan T019CX)
```

> Создадим ещё 5 автомобилей:
```python
>>> Car(7, 'O925HA', 'Tesla', 'Model S', 'violet').save()
>>> Car(8, 'P6883BT', 'Cadillac', 'LYRIQ', 'gray').save()
>>> Car(9, 'M305CC', 'Audi', 'Q6', 'white').save()
>>> Car(10, 'X656AP', 'Ferrari', '488', 'red').save()
>>> Car(11, 'T915TM', 'Maybach', 'Exelero', 'black').save()
>>>
>>> for i in Car.objects.all():
...     print(i)
...
ID:0 (Alfa Romeo Giulietta H534KH)
ID:1 (Chrysler Crossfire O092EE)
ID:2 (Jaguar F-Type Roadster B926OK)
ID:3 (Bentley Continential GT C106AA)
ID:4 (Bugatti Chiron K492OO)
ID:5 (Rolls-Royce Phantom M333ME)
ID:6 (Lamborghini Huracan T019CX)
ID:7 (Tesla Model S O925HA)
ID:8 (Cadillac LYRIQ P6883BT)
ID:9 (Audi Q6 M305CC)
ID:10 (Ferrari 488 X656AP)
ID:11 (Maybach Exelero T915TM)
```

> Создадим права для автовладельцев:
```python
>>> Certificate(0, '0', 'B', '2020-05-17').save()
>>> Certificate(1, '1', 'B', '2015-03-22').save()
>>> Certificate(2, '2', 'B', '2019-11-02').save()
>>> Certificate(3, '3', 'B', '2021-04-12').save()
>>> Certificate(4, '4', 'B', '2021-02-27').save()
>>> Certificate(5, '5', 'B', '2020-08-17').save()
>>> Certificate(6, '6', 'B', '1992-08-08').save()
>>> Certificate(7, '7', 'B', '1990-06-14').save()
>>> Certificate(8, '8', 'B', '1989-12-15').save()
>>> Certificate(9, '9', 'B', '1989-07-07').save()
>>> Certificate(10, '10', 'B', '1994-05-25').save()
>>> Certificate(11, '11', 'B', '1997-09-10').save()
>>>
>>> from project_first_app.models import *
>>> for i in Certificate.objects.all():
...     print(i)
...
Owner ID:ID:0 (Sofia Shikalova) (0)
Owner ID:ID:1 (Igor Polyakov) (1)
Owner ID:ID:2 (Alisher Morgenshtern) (2)
Owner ID:ID:3 (Maria Bobrova) (3)
Owner ID:ID:4 (Sofia Bykova) (4)
Owner ID:ID:5 (Ekaterina Tretyakova) (5)
Owner ID:ID:6 (Jennifer Aniston) (6)
Owner ID:ID:7 (Brad Pitt) (7)
Owner ID:ID:8 (Leonardo DiCaprio) (8)
Owner ID:ID:9 (Matt Damon) (9)
Owner ID:ID:10 (Sandra Bullok) (10)
Owner ID:ID:11 (Reese Witherspoon) (11)
```

> Посмотрим имеющиеся записи о владении:
```python
>>> for i in Ownership.objects.all():
...     print(i)
...
Owner:ID:0 (Sofia Shikalova) | Car:ID:0 (Alfa Romeo Giulietta H534KH)
Owner:ID:0 (Sofia Shikalova) | Car:ID:1 (Chrysler Crossfire O092EE)
Owner:ID:0 (Sofia Shikalova) | Car:ID:2 (Jaguar F-Type Roadster B926OK)
Owner:ID:1 (Igor Polyakov) | Car:ID:1 (Chrysler Crossfire O092EE)
Owner:ID:1 (Igor Polyakov) | Car:ID:2 (Jaguar F-Type Roadster B926OK)
Owner:ID:1 (Igor Polyakov) | Car:ID:3 (Bentley Continential GT C106AA)
```

> Назначим владельцам автомобили:
```python
>>> Ownership(6, 5, 5, '2023-01-13').save()
>>> Ownership(7, 6, 6, '2023-01-13').save()
>>> Ownership(8, 7, 7, '2023-01-13').save()
>>> Ownership(9, 8, 8, '2023-01-13').save()
>>> Ownership(10, 9, 9, '2023-01-13').save()
>>> Ownership(11, 10, 10, '2023-01-13').save()
>>> Ownership(12, 11, 11, '2023-01-13').save()
>>>
>>> for i in Ownership.objects.all():
...     print(i)
...
Owner:ID:0 (Sofia Shikalova) | Car:ID:0 (Alfa Romeo Giulietta H534KH)
Owner:ID:0 (Sofia Shikalova) | Car:ID:1 (Chrysler Crossfire O092EE)
Owner:ID:0 (Sofia Shikalova) | Car:ID:2 (Jaguar F-Type Roadster B926OK)
Owner:ID:1 (Igor Polyakov) | Car:ID:1 (Chrysler Crossfire O092EE)
Owner:ID:1 (Igor Polyakov) | Car:ID:2 (Jaguar F-Type Roadster B926OK)
Owner:ID:1 (Igor Polyakov) | Car:ID:3 (Bentley Continential GT C106AA)
Owner:ID:5 (Ekaterina Tretyakova) | Car:ID:5 (Rolls-Royce Phantom M333ME)
Owner:ID:6 (Jennifer Aniston) | Car:ID:6 (Lamborghini Huracan T019CX)
Owner:ID:7 (Brad Pitt) | Car:ID:7 (Tesla Model S O925HA)
Owner:ID:8 (Leonardo DiCaprio) | Car:ID:8 (Cadillac LYRIQ P6883BT)
Owner:ID:9 (Matt Damon) | Car:ID:9 (Audi Q6 M305CC)
Owner:ID:10 (Sandra Bullok) | Car:ID:10 (Ferrari 488 X656AP)
Owner:ID:11 (Reese Witherspoon) | Car:ID:11 (Maybach Exelero T915TM)
```

## Задание 3.1.1
`Описание:`По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
```python
>>> Car.objects.filter(brand="Jaguar")
<QuerySet [<Car: ID:2 (Jaguar F-Type Roadster B926OK)>]>
```

- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```python
>>> Owner.objects.filter(first_name="Sofia")
<QuerySet [<Owner: ID:0 (Sofia Shikalova)>, <Owner: ID:4 (Sofia Bykova)>]>
```

- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```python
>>> target_id = Owner.objects.all()[9].id_owner
>>> Certificate.objects.get(id_owner=target_id)
<Certificate: Owner ID:ID:9 (Matt Damon) (9)>
```

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
Сначала добавим 'related_name' в модель Ownership для владельца:
```python
class Ownership(models.Model):
    id_ownership = models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Owner, on_delete = models.CASCADE, related_name="owner_ownership")
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null = True)

    def __str__(self):
        return f"Owner:{self.id_owner} | Car:{self.id_car}"
```
```python
>>> Owner.objects.filter(owner_ownership__id_car__color="red")
<QuerySet [<Owner: ID:10 (Sandra Bullok)>]>
```

- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```python
>>> Owner.objects.filter(owner_ownership__start_date__gte="2023-01-01")
<QuerySet [<Owner: ID:5 (Ekaterina Tretyakova)>, <Owner: ID:6 (Jennifer Aniston)>, <Owner: ID:7 (Brad Pitt)>, <Owner: ID:8 (Leonardo DiCaprio)>, <Owner: ID:9 (Matt Damon)>, <Owner: ID:10 (Sandra Bullok)>, <Owner: ID:11 (Reese Witherspoon)>]>
```

## Задание 3.1.3
`Описание:` необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения:
```python
>>> from django.db.models import Min
>>> Certificate.objects.aggregate(start_date=Min("date_of_issue"))
{'start_date': datetime.date(1989, 7, 7)}
```

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```python
from django.db.models import Max
>>> Ownership.objects.aggregate(start_date=Max("start_date"))
{'start_date': datetime.date(2023, 1, 13)}
```

- Выведите количество машин для каждого водителя:
```python
>>> from django.db.models import Count
>>> Ownership.objects.values("id_owner").annotate(Count("id_car"))
<QuerySet [{'id_owner': 0, 'id_car__count': 3}, {'id_owner': 1, 'id_car__count': 3}, {'id_owner': 5, 'id_car__count': 1}, {'id_owner': 6, 'id_car__count': 1}, {'id_owner': 7, 'id_car__count': 1}, {'id_owner': 8, 'id_car__count': 1}, {'id_owner': 9, 'id_car__count': 1}, {'id_owner': 10, 'id_car__count': 1}, {'id_owner': 11, 'id_car__count': 1}]>
```

- Подсчитайте количество машин каждой марки:
```python
>>> Car.objects.values("brand").annotate(Count("id_car"))
<QuerySet [{'brand': 'Alfa Romeo', 'id_car__count': 1}, {'brand': 'Audi', 'id_car__count': 1}, {'brand': 'Bentley', 'id_car__count': 1}, {'brand': 'Bugatti', 'id_car__count': 1}, {'brand': 'Cadillac', 'id_car__count': 1}, {'brand': 'Chrysler', 'id_car__count': 1}, {'brand': 'Ferrari', 'id_car__count': 1}, {'brand': 'Jaguar', 'id_car__count': 1}, {'brand': 'Lamborghini', 'id_car__count': 1}, {'brand': 'Maybach', 'id_car__count': 1}, {'brand': 'Rolls-Royce', 'id_car__count': 1}, {'brand': 'Tesla', 'id_car__count': 1}]>
```

- Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```python
>>> sort_by_date = Certificate.objects.all().order_by("date_of_issue")
>>> for i in sort_by_date:
...     target_id = i.id_owner.id_owner
...     print(Ownership.objects.filter(id_owner__id_owner=target_id))
...
<QuerySet [<Ownership: Owner:ID:9 (Matt Damon) | Car:ID:9 (Audi Q6 M305CC)>]>
<QuerySet [<Ownership: Owner:ID:8 (Leonardo DiCaprio) | Car:ID:8 (Cadillac LYRIQ P6883BT)>]>
<QuerySet [<Ownership: Owner:ID:7 (Brad Pitt) | Car:ID:7 (Tesla Model S O925HA)>]>
<QuerySet [<Ownership: Owner:ID:6 (Jennifer Aniston) | Car:ID:6 (Lamborghini Huracan T019CX)>]>
<QuerySet [<Ownership: Owner:ID:10 (Sandra Bullok) | Car:ID:10 (Ferrari 488 X656AP)>]>
<QuerySet [<Ownership: Owner:ID:11 (Reese Witherspoon) | Car:ID:11 (Maybach Exelero T915TM)>]>
<QuerySet [<Ownership: Owner:ID:1 (Igor Polyakov) | Car:ID:1 (Chrysler Crossfire O092EE)>, <Ownership: Owner:ID:1 (Igor Polyakov) | Car:ID:2 (Jaguar F-Type Roadster B926OK)>, <Ownership: Owner:ID:1 (Igor Polyakov) | Car:ID:3 (Bentley Continential GT C106AA)>]>
<QuerySet []>
<QuerySet [<Ownership: Owner:ID:0 (Sofia Shikalova) | Car:ID:0 (Alfa Romeo Giulietta H534KH)>, <Ownership: Owner:ID:0 (Sofia Shikalova) | Car:ID:1 (Chrysler Crossfire O092EE)>, <Ownership: Owner:ID:0 (Sofia Shikalova) | Car:ID:2 (Jaguar F-Type Roadster B926OK)>]>
<QuerySet [<Ownership: Owner:ID:5 (Ekaterina Tretyakova) | Car:ID:5 (Rolls-Royce Phantom M333ME)>]>
```