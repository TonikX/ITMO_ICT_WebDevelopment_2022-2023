# Laboratory work 3
> Рейнгеверц В.А. - K33401



## Practical part
> [models.py](Pr/django_project_reingeverts/project_first_app/models.py)

![](https://i.imgur.com/IGscva6.png)



### 3.1.1

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей.

```bash
python manage.py shell
```

Автомобили
```python
from project_first_app.models import *

Car.objects.create(license_plate="x000xx", brand="Mitsubishi", model="Mitsubishi Lancer 2017", color="#000000")

# <Car: 8 Mitsubishi Lancer 2017>

Car.objects.create(license_plate="x001xx", brand="Mitsubishi", model="Mitsubishi Outlander 2017", color="#000000")

Car.objects.create(license_plate="x002xx", brand="Lexus", model="Lexus ES 2015", color="#ffffff")

Car.objects.create(license_plate="x003xx", brand="Lexus", model="Lincoln MKZ 2015", color="#ffffff")

Car.objects.create(license_plate="x004xx", brand="Toyota", model="Toyota Land Cruiser 2008", color="#000000")

Car.objects.create(license_plate="x005xx", brand="Toyota", model="Toyota Tundra 2010", color="#ffffff")

# >>> Car.objects.all()
# <QuerySet [<Car: 8 Mitsubishi Lancer 2017>, <Car: 9 Mitsubishi Outlander 2017>, <Car: 10 Lexus ES 2015>, 
# <Car: 11 Lincoln MKZ 2015>, <Car: 12 Toyota Land Cruiser 2008>, <Car: 13 Toyota Tundra 2010>]>
```

Владения
```python
from project_first_app.models import *
import datetime

Ownership.objects.create(car_id=Car.objects.get(pk=8), start_date=datetime.datetime(2018, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=9), start_date=datetime.datetime(2018, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=10), start_date=datetime.datetime(2017, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=11), start_date=datetime.datetime(2020, 1, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=12), start_date=datetime.datetime(2020, 1, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=13), start_date=datetime.datetime(2010, 1, 1), end_date=(datetime.datetime(2015, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=13), start_date=datetime.datetime(2015, 2, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))


# >>> Ownership.objects.all()  
# <QuerySet [<Ownership: 10 - 8 Mitsubishi Lancer 2017 (2018-2019)>, <Ownership: 11 - 9 Mitsubishi Outlander 2017 (2018-2019)>, <Ownership: 12 - 10 Lexus ES 2015 (2017-2019)>, <Ownership: 13 - 11 Lincoln MKZ 2015 (2020-2021)>, <Ownership: 14 - 12 Toyota Land Cruiser 2008 (2020-2021)>, <Ownership: 15 - 13 Toyota Tundra 2010 (2010-2016)>, <Ownership: 16 - 13 Toyota Tundra 2010 (2015-2021)>]>
```

Автовладельцы
```python
from project_first_app.models import *
import datetime

owner = CarOwner.objects.create(first_name="Erin", last_name="Solstice", username="erin1",date_of_birth=datetime.datetime(1999, 1, 1), passport="1234", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=10))

owner = CarOwner.objects.create(first_name="Zorian", last_name="Kazinski", username="zorian1",date_of_birth=datetime.datetime(1992, 1, 1), passport="1111", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=11))

owner = CarOwner.objects.create(first_name="Garen", last_name="Redfang", username="garen1",date_of_birth=datetime.datetime(2005, 1, 1), passport="2222", address="", nationality="goblin")
owner.ownership_id.set(Ownership.objects.filter(pk=12))

owner = CarOwner.objects.create(first_name="Juniper", last_name="Smith", username="juniper1",date_of_birth=datetime.datetime(1998, 1, 1), passport="3333", address="", nationality="USA")
owner.ownership_id.set(Ownership.objects.filter(pk=13))

owner = CarOwner.objects.create(first_name="Ivan", last_name="Petrov", username="ivan1",date_of_birth=datetime.datetime(2000, 1, 1), passport="4444", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=14))

owner = CarOwner.objects.create(first_name="James", last_name="Garfield", username="garfield1",date_of_birth=datetime.datetime(1980, 1, 1), passport="5555", address="", nationality="cat")
owner.ownership_id.set(Ownership.objects.filter(pk__in=[15, 16]))

# >>> CarOwner.objects.all()
# <QuerySet [<CarOwner: 2 - admin ( )>, <CarOwner: 10 - erin1 (Erin Solstice)>, <CarOwner: 11 - zorian1 (Zorian Kazinski)>, <CarOwner: 12 - garen1 (Garen Redfang)>, <CarOwner: 13 - juniper1 (Juniper Smith)>, <CarOwner: 14 - ivan1 (Ivan Petrov)>, <CarOwner: 15 - garfield1 (James Garfield)>]>

```

Удостоверения
```python
from project_first_app.models import *
import datetime


DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=10), serial_number="111111", license_type="B", issue_date=datetime.datetime(2018, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=11), serial_number="222222", license_type="B", issue_date=datetime.datetime(2018, 5, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=12), serial_number="333333", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=13), serial_number="444444", license_type="B", issue_date=datetime.datetime(2019, 5, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=14), serial_number="555555", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=15), serial_number="666666", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

# >>> DriverLicense.objects.all()
# <QuerySet [<DriverLicense: B - 10 - erin1 (Erin Solstice) (111111)>, <DriverLicense: B - 11 - zorian1 (Zorian Kazinski) (222222)>, <DriverLicense: B - 12 - garen1 (Garen Redfang) (333333)>, <DriverLicense: B - 
# 13 - juniper1 (Juniper Smith) (444444)>, <DriverLicense: B - 14 - ivan1 (Ivan Petrov) (555555)>, <DriverLicense: B - 15 - garfield1 (James Garfield) (666666)>]>
```

### 3.1.2

[related_name | Stackoverflow](https://stackoverflow.com/a/2642645)

По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Где это необходимо, добавьте related_name к полям модели
- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

```python
from project_first_app.models import *

Car.objects.filter(brand="Toyota")

# <QuerySet [<Car: 12 Toyota Land Cruiser 2008>, <Car: 13 Toyota Tundra 2010>]>
```


- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

```python
from project_first_app.models import *

CarOwner.objects.filter(first_name="Erin")
# <QuerySet [<CarOwner: 10 - erin1 (Erin Solstice)>]>
```


- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)


```python
from project_first_app.models import *
import random

owners = list(CarOwner.objects.all())
random_owner = random.choice(owners)

# >>> random_owner
# <CarOwner: 11 - zorian1 (Zorian Kazinski)>

DriverLicense.objects.filter(car_owner_id=random_owner.pk).first()
# <DriverLicense: B - 11 - zorian1 (Zorian Kazinski) (222222)>

```

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

```python
from project_first_app.models import *

CarOwner.objects.filter(ownership_id__car_id__color="#000000")
# <QuerySet [<CarOwner: 10 - erin1 (Erin Solstice)>, <CarOwner: 11 - zorian1 (Zorian Kazinski)>, <CarOwner: 14 - ivan1 (Ivan Petrov)>]>
```


- Найти всех владельцев, чей [год владения машиной](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#year) начинается с 2010 (или любой другой год, который присутствует у вас в базе)

```python
from project_first_app.models import *
import datetime

CarOwner.objects.filter(ownership_id__start_date__gte=datetime.datetime(2018, 1, 1))
# <QuerySet [<CarOwner: 10 - erin1 (Erin Solstice)>, <CarOwner: 11 - zorian1 (Zorian Kazinski)>, <CarOwner: 13 - juniper1 (Juniper Smith)>, <CarOwner: 14 - ivan1 (Ivan Petrov)>]>
```


### 3.1.3


Необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения
```python
from project_first_app.models import *

DriverLicense.objects.all().order_by("issue_date").first().issue_date.strftime("%Y.%m.%d")
# '2018.01.01'
```

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
```python
from project_first_app.models import *
import datetime


Ownership.objects.all().order_by('-end_date').first().end_date.strftime("%Y.%m.%d")
# '2021.12.01'

# Или же имелось ввиду?: 

Ownership.objects.filter(end_date__gte=datetime.datetime(2021, 12, 1))
# <QuerySet [<Ownership: 13 - 11 Lincoln MKZ 2015 (2020-2021)>, <Ownership: 14 - 12 Toyota Land Cruiser 2008 (2020-2021)>, <Ownership: 16 - 13 Toyota Tundra 2010 (2015-2021)>]>
```

- Выведите количество машин для каждого водителя
```python
from project_first_app.models import *
from django.db.models import Count

CarOwner.objects.values('username').annotate(car_count=Count("ownership_id"))
# <QuerySet [{'username': 'admin', 'car_count': 0}, {'username': 'erin1', 'car_count': 1}, {'username': 'garen1', 'car_count': 1}, {'username': 'garfield1', 'car_count': 2}, {'username': 'ivan1', 'car_count': 1}, {'username': 'juniper1', 'car_count': 1}, {'username': 'zorian1', 'car_count': 1}]>
```

- Подсчитайте количество машин каждой марки
```python
from project_first_app.models import *
from django.db.models import Count

Car.objects.values('brand').annotate(brand_count=Count("brand"))
# <QuerySet [{'brand': 'Lexus', 'brand_count': 2}, {'brand': 'Mitsubishi', 'brand_count': 2}, {'brand': 'Toyota', 'brand_count': 2}]>
```

- Отсортируйте всех автовладельцев по дате выдачи удостоверения

```python
from project_first_app.models import *

CarOwner.objects.all().order_by('driverlicense__issue_date')
# <QuerySet [<CarOwner: 2 - admin ( )>, <CarOwner: 10 - erin1 (Erin Solstice)>, <CarOwner: 11 - zorian1 (Zorian Kazinski)>, <CarOwner: 12 - garen1 (Garen Redfang)>, <CarOwner: 14 - ivan1 (Ivan Petrov)>, <CarOwner: 15 - garfield1 (James Garfield)>, <CarOwner: 13 - juniper1 (Juniper Smith)>]>
```

(Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом [.distinct()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.distinct))

### 3.2.1
> [views.py](Pr/warriors_project/warriors_app/views.py), [serializers.py](Pr/warriors_project/warriors_app/serializers.py), [urls.py](Pr/warriors_project/warriors_app/urls.py)


Реализовать ендпоинты для добавления и просмотра скилов методом, описанным в пункте выше.

![](https://i.imgur.com/I6YxsvD.png)

![](https://i.imgur.com/el1jQjO.png)

### 3.2.2
Реализовать ендпоинты:
- Вывод полной информации о всех войнах и их профессиях (в одном запросе).
![](https://i.imgur.com/Qt9YzC6.png)

- Вывод полной информации о всех войнах и их скилах (в одном запросе).
![](https://i.imgur.com/k1TuV5w.png)

- Вывод полной информации о войне (по id), его профессиях и скилах.
![](https://i.imgur.com/pm9fWLm.png)

- Удаление война по id.
![](https://i.imgur.com/Yt9jPej.png)

- Редактирование информации о войне.
![](https://i.imgur.com/apAL1To.png)
![](https://i.imgur.com/Hh7ZQCA.png)

### 3.3


## Lab work part

ER Diagram
![](https://i.imgur.com/X3vlFdG.png)

Urls
![](https://i.imgur.com/nEVRsl4.png)

Swagger API Docs
![](https://i.imgur.com/bANA2wt.png)

### Description
> Задание 2

Создать программную систему, предназначенную для работников библиотеки. Такая система должна обеспечивать хранение сведений об имеющихся в библиотеке книгах, о читателях библиотеки и читальных залах.

Для каждой книги в БД должны храниться следующие сведения: название книги, автор (ы), издательство, год издания, раздел, число экземпляров этой книги в каждом зале библиотеки, а также шифр книги и дата закрепления книги за читателем. Книги могут перерегистрироваться в другом зале.

Сведения о читателях библиотеки должны включать номер читательского билета, ФИО читателя, номер паспорта, дату рождения, адрес, номер телефона, образование, наличие ученой степени.

Читатели закрепляются за определенным залом, могут переписаться в другой зал и могут записываться и выписываться из библиотеки. 

Библиотека имеет несколько читальных залов, которые характеризуются номером, названием и вместимостью, то есть количеством людей, которые могут одновременно работать в зале.

Библиотека может получать новые книги и списывать старые. Шифр книги может измениться в результате переклассификации, а номер читательского билета в результате перерегистрации.

Библиотекарю могут потребоваться следующие сведения о текущем состоянии библиотеки:
- Какие книги закреплены за заданным читателем?
- Кто из читателей взял книгу более месяца тому назад?
- За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?
- Сколько в библиотеке читателей младше 20 лет?
- Сколько читателей в процентном отношении имеют начальное образование, среднее, высшее, ученую степень?

Библиотекарь может выполнять следующие операции:
- Записать в библиотеку нового читателя.
- Исключить из списка читателей людей, записавшихся в библиотеку более года назад и не прошедших - перерегистрацию.
- Списать старую или потерянную книгу.
- Принять книгу в фонд библиотеки.

Необходимо предусмотреть возможность выдачи отчета о работе библиотеки в течение месяца. Отчет должен включать в себя следующую информацию: 
- Количество книг и читателей на каждый день в каждом из залов и в библиотеке в целом
- Количество читателей, записавшихся в библиотеку в каждый зал и в библиотеку за отчетный месяц.


### Requirements

- django-phonenumber-field[phonenumberslite]
- djoser
- djangorestframework_simplejwt
- drf_yasg

##### docs
- mkdocs
- mkdocs-material
- mkdocs-jupyter