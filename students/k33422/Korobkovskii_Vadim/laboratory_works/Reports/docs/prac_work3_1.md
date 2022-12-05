# Практическая работа №3.1

## Задание №3.1.1

### Условие задания №3.1.1
Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и 
от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. 
Результатом должны стать запросы и отображение созданных объектов.

### Реализация задания №3.1.1
* `Файл с моделями (базами данных) models.py`
``` python
from django.db import models


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    birthday_date = models.DateField(null=True, blank=True)


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=15, null=False, blank=False)
    brand = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=30, null=True, blank=True)


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class DrivingLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.OneToOneField(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False, blank=False)
    type = models.CharField(max_length=10, null=False, blank=False)
    date_of_issue = models.DateField(null=False, blank=True)
```
* `Команды для заполнения таблицы Owner`
``` python
from project.models import Owner
first_owner = Owner.objects.create(owner_id=1, surname="Kuborskii", name="Artem", birthday_date="2002-08-12")
first_owner.save()
second_owner = Owner.objects.create(owner_id=2, surname="Korobkovskii", name="Vadim", birthday_date="2002-10-25")
second_owner.save()
third_owner = Owner.objects.create(owner_id=3, surname="Pozdnyakov", name="Aleksey", birthday_date="1951-04-01")
third_owner.save()
fourth_owner = Owner.objects.create(owner_id=4, surname="Bolshakova", name="Elena", birthday_date="1951-07-25")
fourth_owner.save()
fifth_owner = Owner.objects.create(owner_id=5, surname="Korobkovskii", name="Andrey", birthday_date="1972-10-19")
fifth_owner.save()
sixth_owner = Owner.objects.create(owner_id=6, surname="Korobkovskaya", name="Natalia", birthday_date="1973-01-08")
sixth_owner.save()
```
* `Команды для заполнения таблицы Car`
``` python
from project.models import Car
first_car = Car.objects.create(car_id=1, number="A222AA", brand="Ferrari", model="La Ferrari", color="yellow")
first_car.save()
second_car = Car.objects.create(car_id=2, number="P444XT", brand="Honda", model="CRV", color="white")
second_car.save()
third_car = Car.objects.create(car_id=3, number="P468IP", brand="BMW", model="X5", color="black")
third_car.save()
fourth_car = Car.objects.create(car_id=4, number="N000IK", brand="Skoda", model="Octavia", color="white")
fourth_car.save()
fifth_car = Car.objects.create(car_id=5, number="N444AT", brand="Mercedes", model="E-Class", color="white")
fifth_car.save()
sixth_car = Car.objects.create(car_id=6, number="B090OT", brand="Jeep", model="Cherokee", color="black")
sixth_car.save()
```
* `Команды для заполнения таблицы Ownership`
``` python
from project.models import Ownership
first_ownership = Ownership.objects.create(owner_car_id=1, owner_id=Owner.objects.get(owner_id=1), car_id=Car.objects.get(car_id=6), start_date="2020-01-02")
first_ownership.save()
second_ownership = Ownership.objects.create(owner_car_id=2, owner_id=Owner.objects.get(owner_id=2), car_id=Car.objects.get(car_id=1), start_date="2022-11-16")
second_ownership.save()
third_ownership = Ownership.objects.create(owner_car_id=3, owner_id=Owner.objects.get(owner_id=3), car_id=Car.objects.get(car_id=2), start_date="2019-06-20")
third_ownership.save()
fourth_ownership = Ownership.objects.create(owner_car_id=4, owner_id=Owner.objects.get(owner_id=4), car_id=Car.objects.get(car_id=4), start_date="2022-11-16")
fourth_ownership.save()
fifth_ownership = Ownership.objects.create(owner_car_id=5, owner_id=Owner.objects.get(owner_id=5), car_id=Car.objects.get(car_id=3), start_date="2018-07-10")
fifth_ownership.save()
sixth_ownership = Ownership.objects.create(owner_car_id=6, owner_id=Owner.objects.get(owner_id=6), car_id=Car.objects.get(car_id=5), start_date="2022-11-16")
sixth_ownership.save()
```
* `Команды для заполнения таблицы DrivingLicense`
``` python
from project.models import DrivingLicense
first_license = DrivingLicense.objects.create(license_id=1, owner_id=Owner.objects.get(owner_id=1), license_number="1234567890", type="B", date_of_issue="2022-01-01")
first_license.save()
second_license = DrivingLicense.objects.create(license_id=2, owner_id=Owner.objects.get(owner_id=2), license_number="1234567891", type="B", date_of_issue="2022-01-01")
second_license.save()
third_license = DrivingLicense.objects.create(license_id=3, owner_id=Owner.objects.get(owner_id=3), license_number="1234567892", type="B", date_of_issue="2021-01-01")
third_olicense.save()
fourth_license = DrivingLicense.objects.create(license_id=4,owner_id=Owner.objects.get(owner_id=4), license_number="1234567893", type="B", date_of_issue="2022-01-01")
fourth_license.save()
fifth_license = DrivingLicense.objects.create(license_id=5, owner_id=Owner.objects.get(owner_id=5), license_number="1234567894", type="B", date_of_issue="2022-01-01")
fifth_license.save()
sixth_license = DrivingLicense.objects.create(license_id=6, owner_id=Owner.objects.get(owner_id=6), license_number="1234567895", type="B", date_of_issue="2020-01-01")
sixth_license.save()
```
## Задание №3.2.1

### Условие задания №3.2.1
Добавить related_name к полям модели там, где это необходимо.

### Реализация задания №3.2.1
* `Измененный файл с моделями (базами данных) models.py`
``` python
from django.db import models


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    birthday_date = models.DateField(null=True, blank=True)


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=15, null=False, blank=False)
    brand = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    color = models.CharField(max_length=30, null=True, blank=True)


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, related_name="hold_owners", related_query_name="hold_owner", on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, related_name="hold_cars", related_query_name="hold_car", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class DrivingLicense(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.OneToOneField(Owner, related_name="license_owner_guy", related_query_name="license_owner", on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False, blank=False)
    type = models.CharField(max_length=10, null=False, blank=False)
    date_of_issue = models.DateField(null=False, blank=True)
```
## Задание №3.2.2
### Условие задания №3.2.2
Вывести все машины марки Ferrari.
### Реализация задания №3.2.2
* `Код запроса`
``` python
Car.objects.filter(brand="Ferrari")
```
* `Вывод`
``` python
<QuerySet [<Car: Car object (1)>]>
```
## Задание №3.2.3
### Условие задания №3.2.3
Найти всех водителей с именем "Natalia".
### Реализация задания №3.2.3
* `Код запроса`
``` python
Owner.objects.filter(name="Natalia")
```
* `Вывод`
``` python
<QuerySet [<Owner: Owner object (6)>]>
```
## Задание №3.2.4
### Условие задания №3.2.4
Взять любого случайного владельца, получить его id, по которому получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса).
### Реализация задания №3.2.4
* `Код запроса`
``` python
id = Owner.objects.filter(surname="Pozdnyakov", name="Aleksey")[0].owner_id
DrivingLicense.objects.get(owner_id=id)
```
* `Вывод`
``` python
<DrivingLicense: DrivingLicense object (3)>
```
## Задание №3.2.5
### Условие задания №3.2.5
Вывести всех владельцев белых машин.
### Реализация задания №3.2.5
* `Код запроса`
``` python
Owner.objects.filter(hold_owner__car_id__color="white")
```
* `Вывод`
``` python
<QuerySet [<Owner: Owner object (3)>, <Owner: Owner object (4)>, <Owner: Owner object (6)>]>
```
## Задание №3.2.6
### Условие задания №3.2.6
Найти всех владельцев, чей год владения машиной начинается с 2022.
### Реализация задания №3.2.6
* `Код запроса`
``` python
Owner.objects.filter(hold_owner__start_date__year__gte=2022)
```
* `Вывод`
``` python
<QuerySet [<Owner: Owner object (2)>, <Owner: Owner object (4)>, <Owner: Owner object (6)>, <Owner: Owner object (7)>]>
```
## Задание №3.3.1
### Условие задания №3.3.1
Вывести дату выдачи самого старшего водительского удостоверения.
### Реализация задания №3.3.1
* `Код запроса`
``` python
from django.db.models import Min
DrivingLicense.objects.aggregate(Min("date_of_issue"))
```
* `Вывод`
``` python
{'date_of_issue__min': datetime.date(2020, 1, 1)}
```

## Задание №3.3.2
### Условие задания №3.3.2
Вывести самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе.
### Реализация задания №3.3.2
* `Код запроса`
``` python
from django.db.models import Max
Ownership.objects.filter(car_id__model="CRV").aggregate(Max("start_date"))
```
* `Вывод`
``` python
{'start_date__max': datetime.date(2019, 6, 20)}
```
## Задание №3.3.3
### Условие задания №3.3.3
Вывести количество машин для каждого водителя.
### Реализация задания №3.3.3
* `Код запроса`
``` python
from django.db.models import Count
Owner.objects.values("owner_id").annotate(Count("hold_owner__car_id"))
```
* `Вывод`
``` python
<QuerySet [{'owner_id': 1, 'hold_owner__car_id__count': 1}, {'owner_id': 2, 'hold_owner__car_id__count': 1}, {'owner_id': 3, 'hold_owner__car_id__count': 1}, {'owner_id': 4, 'hold_owner__car_id__count': 1}, {'owner_id': 5, 'hold_owner__car_id__count': 1}, {'owner_id': 6, 'hold_owner__car_id__count': 1}, {'owner_id': 7, 'hold_owner__car_id__count': 1}]>
```
## Задание №3.3.4
### Условие задания №3.3.4
Вывести количество машин каждой марки.
### Реализация задания №3.3.4
* `Код запроса`
``` python
from django.db.models import Count
Car.objects.values("brand").annotate(Count("car_id"))
```
* `Вывод`
``` python
<QuerySet [{'brand': 'BMW', 'car_id__count': 1}, {'brand': 'Ferrari', 'car_id__count': 1}, {'brand': 'Honda', 'car_id__count': 1}, {'brand': 'Jeep', 'car_id__count': 1}, {'brand': 'Lada', 'car_id__count': 1}, {'brand': 'Mercedes', 'car_id__count': 1}, {'brand': 'Skoda', 'car_id__count': 1}]>
```
## Задание №3.3.5
### Условие задания №3.3.5
Отсортировать всех автовладельцев по дате выдачи удостоверения.
### Реализация задания №3.3.5
* `Код запроса`
``` python
Owner.objects.order_by("license_owner__date_of_issue")
```
* `Вывод`
``` python
<QuerySet [<Owner: Owner object (7)>, <Owner: Owner object (6)>, <Owner: Owner object (3)>, <Owner: Owner object (1)>, <Owner: Owner object (2)>, <Owner: Owner object (4)>, <Owner: Owner object (5)>]>
```

