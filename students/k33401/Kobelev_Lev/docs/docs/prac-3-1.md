# Practical 3

Django запросы

## Models

Модели без методов:
``` python
class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    cars = models.ManyToManyField(Car, through='Ownership')
    passport = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=15, null=True, blank=True)


class DriverLicense(models.Model):
    license_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Ownership(models.Model):
    ownership_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ownership_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
```

Далее входим в интерактивный режим (запускаем `python console` в `pycharm`): 
``` python
python manage.py shell
from practical_work_1.models import *
```

## 3.1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей.

- Автовладельцы:
``` python
owner = Owner.objects.create(first_name='Mario', second_name='Mario', username='supermario', password='superpassword1')
owner = Owner.objects.create(first_name='Donkey', second_name='Kong', username='koong', password='superpassword2')
owner = Owner.objects.create(first_name='Bowser', second_name='Bowser', username='bo', password='superpassword3')
owner = Owner.objects.create(first_name='Yoshi', second_name='Yoshi', username='yoyo', password='superpassword4')
owner = Owner.objects.create(first_name='Princess', second_name='Daisy', username='daisy', password='superpassword5')
owner = Owner.objects.create(first_name='Princess', second_name='Peach', username='peach', password='superpassword6')
```

- Машины:
``` python
car = Car.objects.create(state_number='C031AP', brand='Mario Kart', model='MK Deluxe 8', color='red')
car = Car.objects.create(state_number='C032AP', brand='Mario Kart', model='MK 7', color='blue')
car = Car.objects.create(state_number='C033AP', brand='Mario Kart', model='MK 8', color='red')
car = Car.objects.create(state_number='C034AP', brand='Mario Kart', model='MK 8', color='green')
car = Car.objects.create(state_number='C035AP', brand='Mario Kart', model='MK DS', color='orange')
car = Car.objects.create(state_number='C036AP', brand='Mario Kart', model='MK 64', color='pink')
```

- Удостоверения:
``` python
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='supermario'), license_number='PW3001', type='MK', issue_date='2020-10-10')
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='koong'), license_number='PW3002', type='MK', issue_date='2019-10-10')
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='bo'), license_number='PW3003', type='MK', issue_date='2018-10-10')
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='yoyo'), license_number='PW3004', type='MK', issue_date='2017-10-10')
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='daisy'), license_number='PW3005', type='MK', issue_date='2016-10-10')
license = DriverLicense.objects.create(license_owner=Owner.objects.get(username='peach'), license_number='PW3006', type='MK', issue_date='2015-10-10')
```

- Владения:
``` python
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='supermario'), ownership_car=Car.objects.get(id=11), date_start='2021-10-10')
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='koong'), ownership_car=Car.objects.get(id=12), date_start='2021-10-10')
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='bo'), ownership_car=Car.objects.get(id=13), date_start='2021-10-10')
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='yoyo'), ownership_car=Car.objects.get(id=14), date_start='2021-10-10')
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='daisy'), ownership_car=Car.objects.get(id=15), date_start='2022-10-10')
ownership = Ownership.objects.create(ownership_owner=Owner.objects.get(username='peach'), ownership_car=Car.objects.get(id=16), date_start='2021-10-10')
```

## 3.2
1. Получение всех машин марки `Mario Kart`:
Запрос:
``` python
Car.objects.filter(brand = "Mario Kart")
```
Результат:
``` python
<QuerySet [<Car: Mario Kart MK Deluxe 8>, <Car: Mario Kart MK 7>, <Car: Mario Kart MK 8>, <Car: Mario Kart MK 8>, <Car: Mario Kart MK DS>, <Car: Mario Kart MK 64>]>
```

2. Получение всех водителей с именем `Mario`:
Запрос:
``` python
Owner.objects.filter(first_name = "Mario")
```
Результат:
``` python
<QuerySet [<Owner: Mario Mario>]>
```
**NB:** тут стоило было бы применить `first_name__contains`, если бы имя было составным, но для фамилии существует отдельное поле.

3. Получение удостоверения случайного водителя:
Запрос:
``` python
DriverLicense.objects.get(license_owner = Owner.objects.order_by("?").first().id)
```
Результат:
``` python
<DriverLicense: DriverLicense object (1)>
```

4. Получение всех владельцев машин с цветом `orange`:
Запрос:
``` python
Owner.objects.filter(cars__color__contains="orange")
```
Результат:
``` python
<QuerySet [<Owner: Princess Daisy>]>
```
**NB:** у машины может быть составной цвет, например, “Yellow, Red”, поэтому идет проверка на наличие, а не на эквивалентность.

5. Получить всех владельцев, чей год владения машиной начинается с 2022:
Запрос:
``` python
Owner.objects.filter(ownership__date_start__gte='2022-01-01')
```
Результат:
``` python
<QuerySet [<Owner: Princess Daisy>]>
```

## 3.3
1. Вывод даты выдачи самого старшего водительского удостоверения
Запрос:
``` python
DriverLicense.objects.aggregate(start_date=Min('issue_date'))
```
Результат:
``` python
{'start_date': datetime.date(2015, 10, 10)}
```
**NB:** необходимо сделать `from django.db.models import Min`

2. Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
Запрос:
``` python
Ownership.objects.aggregate(start_date=Max('date_start'))
```
Результат:
``` python
{'start_date': datetime.date(2022, 10, 20)}
```
**NB:** необходимо сделать `from django.db.models import Max`

3. Выведите количество машин для каждого водителя
Запрос:
``` python
Ownership.objects.values('ownership_owner__username').annotate(Count('ownership_car'))
```
Результат:
``` python
<QuerySet [{'ownership_owner__username': 'bo', 'ownership_car__count': 1}, {'ownership_owner__username': 'daisy', 'ownership_car__count': 1}, {'ownership_owner__username': 'koong', 'ownership_car__count': 1}, {'ownership_owner__username': 'peach', 'ownership_car__count': 1}, {'ownership_owner__username': 'supermario', 'ownership_car__count': 1}, {'ownership_owner__username': 'yoy', 'ownership_car__count': 1}]>
```
**NB:** необходимо сделать `from django.db.models import Count`

4. Подсчитайте количество машин каждой марки
Запрос:
``` python
Car.objects.values('brand').annotate(Count('id'))
```
Результат:
``` python
<QuerySet [{'brand': 'Mario Kart', 'id__count': 6}>
```

5. Отсортируйте всех автовладельцев по дате выдачи удостоверения 
Запрос:
``` python
DriverLicense.objects.values('license_owner__username').order_by('issue_date')
```
Результат:
``` python
<QuerySet [{'license_owner__username': 'peach'}, {'license_owner__username': 'daisy'}, {'license_owner__username': 'yoyo'}, {'license_owner__username': 'bo'}, {'license_owner__username': 'koong'}, {'license_owner__username': 'supermario'}]>
```