# Отчет

## Задание 1. Добавление данных

```python
def task1():
    for i in range(1, 7):
        owner = CarOwner(first_name=f"owner_{i}_name", last_name=f"last_name_{i}", birthdate=f"2002-01-0{i}")
        owner.save()

    for i, owner in enumerate(CarOwner.objects.all()):
        license = License(car_owner=owner, license_number=1000+i, reg_date="2020-01-01")
        license.save()

    for i in range(1,6):
        car = Car(car_number=1000+i, brand=f"brand_{i}", model=f"model_{i}", color="black")
        car.save()

    for i, owner in enumerate(CarOwner.objects.all()):
        license = License(car_owner=owner, license_number=1000+i, reg_date="2020-01-01")
        license.save()

    for owner, car in zip(CarOwner.objects.all(), Car.objects.all()):
        own = Own(car=car, car_owner=owner, start_own_date="2022-01-01")
        own.save()

    for own in Own.objects.all():
        print(f"{own}: {own.car_owner} {own.car}")
```

Вывод

```shell
(pw3) ➜  pw3 git:(main) ✗ ./manage.py runscript pw3
Владение №1: Водитель owner_1_name Машина №1001
Владение №2: Водитель owner_2_name Машина №1002
Владение №3: Водитель owner_3_name Машина №1003
Владение №4: Водитель owner_4_name Машина №1004
Владение №5: Водитель owner_5_name Машина №1005
```

## Задание 2. Фильтрация

1. Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
2. Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
3. Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
4. Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
5. Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

```python
def task2():
    print(Car.objects.filter(model="model_3"))
    print(CarOwner.objects.filter(first_name="owner_4_name"))
    print(CarOwner.objects.get(pk=2).license.all())
    print(CarOwner.objects.filter(own__car__color="black"))
    print(CarOwner.objects.filter(own__start_own_date__gte="2022-01-01"))
```

Вывод

```shell
(pw3) ➜  pw3 git:(main) ✗ ./manage.py runscript pw3
<QuerySet [<Car: Машина №1003>]>
<QuerySet [<CarOwner: Водитель owner_4_name>]>
<QuerySet [<License: Лицензия №1001>]>
<QuerySet [<CarOwner: Водитель owner_1_name>, <CarOwner: Водитель owner_2_name>, <CarOwner: Водитель owner_3_name>, <CarOwner: Водитель owner_4_name>, <CarOwner: Водитель owner_5_name>]>
<QuerySet [<CarOwner: Водитель owner_1_name>, <CarOwner: Водитель owner_2_name>, <CarOwner: Водитель owner_3_name>, <CarOwner: Водитель owner_4_name>, <CarOwner: Водитель owner_5_name>]>
```

## Задание 2. Агрегация и аннотация

1. Вывод даты выдачи самого старшего водительского удостоверения 
2. Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе 
3. Выведите количество машин для каждого водителя 
4. Подсчитайте количество машин каждой марки 
5. Отсортируйте всех автовладельцев по дате выдачи удостоверения 


```python
def task3():
    print(License.objects.aggregate(oldest_lisense=Min("reg_date")))
    print(Own.objects.aggregate(youngest_own=Max("start_own_date")))
    print(CarOwner.objects.values("id").annotate(Count("own__car")))
    print(Car.objects.values("brand").annotate(count=Count("id")))
    print(CarOwner.objects.order_by('license__reg_date').values_list("id", "license__reg_date"))
```

Вывод

```shell
(pw3) ➜  pw3 git:(main) ✗ ./manage.py runscript pw3
{'oldest_lisense': datetime.date(2020, 1, 1)}
{'youngest_own': datetime.date(2022, 1, 1)}
<QuerySet [{'id': 1, 'own__car__count': 1}, {'id': 2, 'own__car__count': 1}, {'id': 3, 'own__car__count': 1}, {'id': 4, 'own__car__count': 1}, {'id': 5, 'own__car__count': 1}, {'id': 6, 'own__car__count': 0}]>
<QuerySet [{'brand': 'brand_1', 'count': 1}, {'brand': 'brand_2', 'count': 1}, {'brand': 'brand_3', 'count': 1}, {'brand': 'brand_4', 'count': 1}, {'brand': 'brand_5', 'count': 1}]>
<QuerySet [(1, datetime.date(2020, 1, 1)), (2, datetime.date(2020, 1, 1)), (3, datetime.date(2020, 1, 1)), (4, datetime.date(2020, 1, 1)), (5, datetime.date(2020, 1, 1)), (6, datetime.date(2020, 1, 1))]>
```