# Практическая работа № 3.1

## Задание 3.1.1

* `models.py`
```python
class CarOwner(AbstractUser):
    id_owner = models.IntegerField(primary_key = True)
    last_name = models.CharField(max_length = 30, null = False)
    first_name = models.CharField(max_length = 30, null = False)
    birth_day = models.DateField(null = True)
    passport = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=20, null=True, blank=True)

class Car(models.Model):
    id_car = models.IntegerField(primary_key=True)
    state_number = models.CharField(max_length=15, null=False)
    mark_car = models.CharField(max_length=20, null=False)
    model_car = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=False)


class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class DriverLicense(models.Model):
    id_license = models.IntegerField(primary_key=True)
    id_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    date_of_license = models.DateField()
```
**Создание сущностей**

**Создание автовладельцев**
```
Car_owner(id_owner=1, last_name='LN1', first_name'FN1', birth_name='1990-01-1').save()
Car_owner(id_owner=2, last_name='LN2', first_name'FN2', birth_name='1990-01-2').save()
Car_owner(id_owner=3, last_name='LN3', first_name'FN3', birth_name='1990-01-3').save()
Car_owner(id_owner=4, last_name='LN4', first_name'FN4', birth_name='1990-01-4').save()
Car_owner(id_owner=5, last_name='LN5', first_name'FN5', birth_name='1990-01-5').save()
Car_owner(id_owner=6, last_name='LN6', first_name'FN6', birth_name='1990-01-6').save()

for i in Car_owner.objects.all():
    ...:     print(i.first_name)
    ...: 
FN1
FN2
FN3
FN4
FN5
FN6
```

**Создание автомобилей**

```
Car(id_car=1, state_number='a001aa', mark_car='BMW', model_car='Model1', color='green').save()
Car(id_car=2, state_number='a002aa', mark_car='BMW', model_car='Model2', color='green').save()
Car(id_car=3, state_number='a003aa', mark_car='BMW', model_car='Model3', color='blue').save()
Car(id_car=4, state_number='a004aa', mark_car='BMW', model_car='Model4', color='green').save()
Car(id_car=5, state_number='a005aa', mark_car='BMW', model_car='Model5', color='green').save()
Car(id_car=6, state_number='a006aa', mark_car='BMW', model_car='Model6', color='green').save()
```
**Создание водительских удостоверений**

```
Driver_license(1, 1, '123', 'A', '2010-01-01').save()
Driver_license(2, 2, '3214', 'B', '2011-01-02').save()
Driver_license(3, 3, '41421', 'C', '2012-01-03').save()
Driver_license(4, 4, '3212', 'A', '2013-01-04').save()
Driver_license(5, 5, '158143', 'B', '2014-01-05').save()
Driver_license(6, 6, '932188', 'C', '2015-01-06').save()
```

**Создание связи владения**
```
Ownerdhip(1, 1, 1, '2011-01-01', '2012-01-01').save()
Ownerdhip(2, 2, 2, '2012-01-01', '2013-01-01').save()
Ownerdhip(3, 3, 3, '2013-01-01', '2014-01-01').save()
Ownerdhip(4, 4, 4, '2014-01-01', '2015-01-01').save()
Ownerdhip(5, 5, 5, '2015-01-01', '2016-01-01').save()
Ownerdhip(6, 6, 6, '2016-01-01', '2017-01-01').save()
```
## Задание 3.1.2

Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:

**Запрос 1**

Выведете все машины марки “BMV” (или любой другой марки, которая у вас есть):
```
Car.objects.filter(mark_car="BMV")
```
**Запрос 2**

Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):
```
 Car_owner.objects.filter(first_name="FN1")
```

**Запрос 3**

Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):
```
take_id = Car_owner.objects.all()[3].id_owner
Driver_license.objects.get(id_owner=take_id)
```
**Запрос 4**

Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):


```
CarOwner.objects.filter(ownership__id__car__color="green")
```
**Запрос 5**

Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):
```
Ownerdhip.objects.filter(start_date__gte="2013-01-01")
```

## Задание 3.1.3

**Запрос 1**

Вывод даты выдачи самого старшего водительского удостоверения:
```
from django.db.models import Min, Max

Driver_license.objects.aggregate(date_of_license=Min("date_of_license"))
```
**Запрос 2**

Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
```
Ownerdhip.objects.aggregate(start_date=Max("start_date"))
```
**Запрос 3**

Выведите количество машин для каждого водителя:
```
from django.db.models import Count

Ownerdhip.objects.values("id_owner").annotate(Count("id_car"))
```
**Запрос 4**

Подсчитайте количество машин каждой марки:
```
Car.objects.values("mark_car").annotate(Count("id_car"))
```
**Запрос 5**

Отсортируйте всех автовладельцев по дате выдачи удостоверения:
```
Car_owner.objects.order_by("driver_license__date_of_license")
```