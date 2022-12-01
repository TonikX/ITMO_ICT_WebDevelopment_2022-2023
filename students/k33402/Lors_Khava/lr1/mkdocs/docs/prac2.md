# Практическая работа 3.1
## Задание 3.1.1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.

* `models.py`

```python 
from django.db import models

class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField()


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    state_num = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)


class Ownership(models.Model):
    owner_car_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class License(models.Model):
    license_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='car_owner')
    license_num = models.CharField(max_length=10, null=False)
    type = models.CharField(max_length=10, null=False)
    start_date_license = models.DateField()
```

### Создание автовладельцев:

```
>>> owner1=Owner.objects.create(owner_id = 1, last_name="Popova",first_name="Masha", birthday="2000-10-10")
>>> owner2=Owner.objects.create(owner_id = 2, last_name="Ivanov", first_name="Ivan", birthday="1990-10-10")
>>> owner3=Owner.objects.create(owner_id = 3, last_name="Pupkin", first_name="Oleg", birthday="1995-10-10")
>>> owner4=Owner.objects.create(owner_id = 4, last_name="Markov", first_name="Max", birthday="2000-10-10")
>>> owner5=Owner.objects.create(owner_id = 5, last_name="Borisov", first_name="Boris", birtday="1985-10-10")
>>> owner6=Owner.objects.create(owner_id = 6, last_name="Smirnova", first_name="Dasha", birthday="1990-10-10")
```

### Создание автомобилей: 

```
car1=Car.objects.create(car_id=1, state_num="A111AA1", brand="Tayota", model="1", color="black")
>>> car2=Car.objects.create(car_id=2, state_num="A222AA1",brand="BMW", model="1", color="red")
>>> car3=Car.objects.create(car_id=3, state_num="A333AA1", brand="BMW", model="2", color="white")
>>> car4=Car.objects.create(car_id=4, state_num="A444AA1", brand="Tayota", model="2", color="blue")
>>> car5=Car.objects.create(car_id=5, state_num="A555AA1", brand="Audi", model="1", color="black")
>>> car6=Car.objects.create(car_id=6, state_num="A666AA1", brand="Audi", model="2", color="black")
```

### Создание водительских прав: 

```
>>> license1=License.objects.create(license_id=1, owner_id=owner1, license_num="123456789", type="B", start_date_license="2020-10-10")
>>> license2=License.objects.create(license_id=2, owner_id=owner2, license_num="123456666", type="B", start_date_license="2010-10-10")
>>> license3=License.objects.create(license_id=3, owner_id=owner3, license_num="123456777", type="B", start_date_license="2010-10-10")
>>> license4=License.objects.create(license_id=4, owner_id=owner4, license_num="123456888", type="B", start_date_license="2020-10-10")
>>> license5=License.objects.create(license_id=5, owner_id=owner5, license_num="123456999", type="B", start_date_license="2005-10-10")
>>> license6=License.objects.create(license_id=6, owner_id=owner6, license_num="123457111", type="B", start_date_license="2008-10-10")
```

### Владение автомобилей: 

```
>>> Ownership(1, 1, 1, "2021-10-10", "2022-10-10").save() 
>>> Ownership(2, 2, 2, "2011-10-10", "2012-10-10").save() 
>>> Ownership(3, 3, 3, "2011-10-10", "2012-10-10").save() 
>>> Ownership(4, 4, 4, "2021-10-10", "2022-10-10").save() 
>>> Ownership(5, 5, 5, "2006-10-10", "2007-10-10").save() 
>>> Ownership(6, 6, 6, "2009-10-10", "2010-10-10").save() 
```


## Задание 3.1.2
По созданным в пр.1 данным написать следующие запросы на фильтрацию: 

### Запрос 1
Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):

```
>>> Car.objects.filter(brand="Tayota")
<QuerySet [<Car: Car object (1)>, <Car: Car object (4)>]>
```

### Запрос 2
Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):

```
>>> Owner.objects.filter(first_name="Oleg")
<QuerySet [<Owner: Owner object (3)>]>
```

### Запрос 3
Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):

```
>>> take_id=Owner.objects.all()[0].owner_id
>>> License.objects.get(owner_id=take_id)
<License: License object (1)>
```

### Запрос 4
Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):

```
>>> Owner.objects.filter(owner__car_id__color="black")
<QuerySet [<Owner: Owner object (1)>, <Owner: Owner object (5)>, <Owner: Owner object (6)>]>  
```

### Запрос 5
Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):

```
>>> Owner.objects.filter(car_owner__start_date_license__gte="2010-01-01")
<QuerySet [<Owner: Owner object (1)>, <Owner: Owner object (2)>, <Owner: Owner object (3)>, <Owner: Owner object (4)>]>
```

## Задание 3.1.3

Необходимо реализовать следующие запросы:

### Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:

```
>>> from django.db.models import Min, Max
>>> License.objects.aggregate(start_date_license=Min("start_date_license"))
{'start_date_license': datetime.date(2005, 10, 10)}
```

### Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:

```
>>> Ownership.objects.aggregate(start_date=Max("start_date"))
{'start_date': datetime.date(2021, 10, 10)}
```

### Запрос 3
Выведите количество машин для каждого водителя:

```
>>> from django.db.models import Count
>>> Ownership.objects.values("owner_id").annotate(Count("car_id"))
<QuerySet [{'owner_id': 1, 'car_id__count': 1}, {'owner_id': 2, 'car_id__count': 1}, {'owner_id': 3, 'car_id__count': 1}, {'owner_id': 4, 'car_id__count': 1}, {'owner_id': 5, 'car_id__count': 1}, {'owner_id': 6, 'car_id__count': 1}]>
```

### Запрос 4
Подсчитайте количество машин каждой марки:

```
>>> Car.objects.values("brand").annotate(Count("car_id"))
<QuerySet [{'brand': 'Audi', 'car_id__count': 2}, {'brand': 'BMW', 'car_id__count': 2}, {'brand': 'Tayota', 'car_id__count': 2}]>
```

### Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:

```
>>> Owner.objects.order_by("license__start_date_license")
<QuerySet [<Owner: Owner object (5)>, <Owner: Owner object (6)>, <Owner: Owner object (2)>, <Owner: Owner object (3)>, <Owner: Owner object (1)>, <Owner: Owner object (4)>]>
```



