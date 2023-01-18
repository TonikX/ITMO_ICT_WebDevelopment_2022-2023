# Практическая работа 3.1

Импортируем необходимые для выполнения объекты: `datetime` (работа с датами и временем), `random` (для случайной генерации объектов), `Count` из `django.db.models` (для подсчета объектов в запросе), `timezone` из `django.utils` и все модели из лабораторной работы 2.

```py
import datetime
from random import choice, randint

from django.db.models import Count
from django.utils import timezone

from project_first_app.models import *
```

## Задание 1

### Код

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов. 

```py 

new_owners = [
	Owner.objects.create(username="User1", first_name="User", last_name="1"),
	Owner.objects.create(username="User2", first_name="User", last_name="2"),
	Owner.objects.create(username="User3", first_name="User", last_name="3"),
	Owner.objects.create(username="User4", first_name="User", last_name="4"),
	Owner.objects.create(username="User5", first_name="User", last_name="5"),
	Owner.objects.create(username="User6", first_name="User", last_name="6")
]

colors = ["white", "red"]
vehicles = [
	{"manufacturer": "Toyota", "model": "Trueno"},
	{"manufacturer": "Mazda", "model": "RX6"},
]

for owner in new_owners:
	license = License.objects.create(owner_id=owner, license_number=str(owner.id),
	                                 issue_date=timezone.now() - datetime.timedelta(days=randint(0, 256)))
	vehicle = Vehicle.objects.create(registration_number="123", color=choice(colors), **choice(vehicles))
	property = Property.objects.create(owner_id=owner, vehicle_id=vehicle,
	                                   start_date=timezone.now() - datetime.timedelta(days=randint(0, 256)))

	print("Owner:", owner)
	print("License:", license, f"(issue date is {license.issue_date} )")
	print("Vehicle:", vehicle)
	print("Property:", property, f"(start date is {property.start_date} )")
	print(owner.property_set)
	print()
```

### Описание

Создаем массив с новыми автовладельцами.

```py
new_owners = [
	Owner.objects.create(username="User1", first_name="User", last_name="1"),
	Owner.objects.create(username="User2", first_name="User", last_name="2"),
	Owner.objects.create(username="User3", first_name="User", last_name="3"),
	Owner.objects.create(username="User4", first_name="User", last_name="4"),
	Owner.objects.create(username="User5", first_name="User", last_name="5"),
	Owner.objects.create(username="User6", first_name="User", last_name="6")
]
```

Запрос `create` - создает в базе и возвращает в качестве объекта новый объект. В параметрах указаны поля и их значения, которые получит новый объект.

Перечисления для случайной генерации данных в базу.
```py
colors = ["white", "red"]
vehicles = [
	{"manufacturer": "Toyota", "model": "Trueno"},
	{"manufacturer": "Mazda", "model": "RX6"},
]
```

Для каждого пользователя...

Создаем водительское удостоверение
```py
	license = License.objects.create(
        owner_id=owner, 
        license_number=str(owner.id),
	    issue_date=timezone.now() - datetime.timedelta(days=randint(0, 256)))
    )
```

`timezone.now() - datetime.timedelta(days=randint(0, 256)))` - устанавливает случайное время выдачи удостоверения. Между текущим временем и 256 днями ранее текущего времени.

Создаем случайных автомобиль. Регистрационный номер "123", цвет - случайный из возможных, которые мы указали ранее. Остальные параметры - случайных из тех, которые мы указали ранее.
```py
	vehicle = Vehicle.objects.create(
        registration_number="123", 
        color=choice(colors), 
        **choice(vehicles)
    )
```

`**choice(vehicles)` - распаковываем выбранный случайным образом объект с данными о производителе и модели 

Создаем запись о владении автомобилем для текущего пользователя и созданного ранее автомобиля.
```py
	property = Property.objects.create(
        owner_id=owner, 
        vehicle_id=vehicle,
        start_date=timezone.now() - datetime.timedelta(days=randint(0, 256)))
```

`timezone.now() - datetime.timedelta(days=randint(0, 256)))` - через вспомогательный объект `timezone` из Джанго берем текущее время с указанием таймзоны и выбираем случайную дату начала владения автомобилем. Между текущим временем и 256 днями ранее текущего времени.

Выводим данные о созданных объектах.
```py
	print("Owner:", owner)
	print("License:", license, f"(issue date is {license.issue_date} )")
	print("Vehicle:", vehicle)
	print("Property:", property, f"(start date is {property.start_date} )")
	print(owner.property_set)
	print()
```

## Задание 2

### Код

По созданным в пр.1 данным написать следующие запросы на фильтрацию:

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

```py
print("Vehicle \"Toyota\":", Vehicle.objects.filter(manufacturer="Toyota"))
print("Owner \"User\":", Owner.objects.filter(first_name="User"))
print("Owner \"6\":", Owner.objects.get(last_name="6"))
print("License of owner \"6\":", License.objects.filter(owner_id__id=Owner.objects.get(last_name="6").id))
print("Red vehicles owners:", Owner.objects.filter(vehicle__color="red"))
print("Owners since 2022:", Owner.objects.filter(property__start_date__year__gte="2022").distinct())
print()
```

### Описание

- `Vehicle.objects.filter(manufacturer="Toyota")` - запрос `filter` фильтрует список всех объектов и возвращает те, которые соответствуют запросу. В нашем случае - производитель должен быть "Тойота".
- `Owner.objects.filter(first_name="User")` - пользователи, чье имя "User"
- `Owner.objects.get(last_name="6")` - один пользователь, чья фамилия "6"
- `License.objects.filter(owner_id__id=Owner.objects.get(last_name="6").id)` - выбираем водительское удостоверение для пользователя, чей идентификатор равен идентификатору пользователя с фамилией "6".
- `Vehicle.objects.filter(color="red")` - выбираем автомобили с красным цветом
- `Owner.objects.filter(property__start_date__year="2022").distinct()` - выбираем пользователей, у которых в смежной таблице `Property` есть запись, в которой поле `start_date` имеет 2022 год (поле `year` у объекта даты/времени). `distinct` убирает все дубликаты пользователей из возвращаемого списка.

## Задание 3

### Код

Необходимо реализовать следующие запросы:
- Вывод даты выдачи самого старшего водительского удостоверения
- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
- Выведите количество машин для каждого водителя
- Подсчитайте количество машин каждой марки
- Отсортируйте всех автовладельцев по дате выдачи удостоверения 

```py
print("Oldest license date:", License.objects.order_by("issue_date")[0])
print("Newest Trueno car property date:", Property.objects.filter(vehicle_id__model="Trueno").order_by("-start_date")[0].start_date.isoformat())
print("Car count:", [f"{owner.username}: {owner.vehicle__count}" for owner in Owner.objects.annotate(Count("vehicle"))])
print("Vehicle count:", [f"{vehicle.get('manufacturer')}: {vehicle.get('id__count')}" for vehicle in Vehicle.objects.values("manufacturer").annotate(Count("id"))])
print("Owners' licenses:", Owner.objects.order_by("license__issue_date").distinct())
print()
```

### Описание

- `License.objects.order_by("issue_date")[0]` - выбираем первое водительское удостоверение среди отсортированных по возврастанию даты выдачи (сортировка по умолчанию - по возрастанию)
- `Property.objects.filter(vehicle_id__model="Trueno").order_by("-start_date")[0].start_date.isoformat()` - выбираем владения автомобилями с моделью "Труено", сортируем по дате начала владения по убыванию (знак "-" перед именем поля) ши выбираем первое из выданных объектов владений. Из него берем дату и выводим в ИСО формате.
- `[f"{owner.username}: {owner.vehicle__count}" for owner in Owner.objects.annotate(Count("vehicle"))]` - генератор, в котором мы при помощи запроса `annotate` для каждого из пользователей считаем количество записей об автомобилях `Count("vehicle")` и выводим вместе с фамилией пользователя
- `[f"{vehicle.get('manufacturer')}: {vehicle.get('id__count')}" for vehicle in Vehicle.objects.values("manufacturer").annotate(Count("id"))]` - генератор, в котором мы при помощи запроса `values` группируем все автомобили по производителю и запросом `annotate` для каждой из групп считаем количество уникальных идентификаторов (`Count("id")`). Выодим вместе с каждым именем производителя
- `Owner.objects.order_by("license__issue_date").distinct()` - выбираем владельцев и сортируем по дате выдачи водительского удостоверения (поле `issue_date` в таблице `license`). Убираем из результатов дубликаты запросом `distinct`