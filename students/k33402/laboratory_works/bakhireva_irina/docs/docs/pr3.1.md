# Практическая работа 3.1

## Задание 1

```py
from project_first_app.models import *
from django.utils import timezone

""" 3.1.1
Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей,
каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей.
Задание можете выполнить либо в интерактивном режиме интерпретатора,
либо в отдельном python-файле.
Результатом должны стать запросы и отображение созданных объектов.
"""

for i in range(6):
	Property.objects.create(
		owner=License.objects.create(
			owner=Owner.objects.create(
				username='new_batch_user' + str(i),
				first_name=['Владислав', 'Анатолий',
				            'Степан', 'Евгений', 'Олег', 'Сергей'][i],
				last_name=['Петров', 'Попов', 'Антонов',
				           'Иванов', 'Егоров', 'Орлов'][i]
			),
			license_number='1234567' + str(i),
			issue_date=timezone.now()).owner,
		car=Car.objects.create(
			number='AO17' + str(i),
			manufacturer='Ford',
			model='Focus',
			color=['Красный', 'Синий', 'Белый',
			       'Серый', 'Желтый', 'Оранжевый'][i]
		), start_date=timezone.now()
	)
```

## Задание 2

```py
from project_first_app.models import *
from django.utils import timezone

""" 3.1.2
По созданным в пр.1 данным написать следующие запросы на фильтрацию:

 - Где это необходимо, добавьте related_name к полям модели
 - Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
 - Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
 - Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
 - Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
 - Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)
"""

# Выбираем автомобили, у которых "manufacturer" - LADA
Car.objects.filter(manufacturer='LADA')
# Выбираем владельцев, у которых имя "Олег"
Owner.objects.filter(first_name='Олег')
# Выбираем лицензии, у которых владалец равен последнему добавленному владельцу в базу данных
License.objects.get(owner=Owner.objects.last())
# Выбираем владельцев, у которых в собственности (owner_property) есть автомобиль (car) с нужным цветом (color)
Owner.objects.filter(owner_property__car__color='Синий')
# Выбираем владельцев, у которых есть собственность (owner_property), полученная после 2010 года (start_date - начало владения, gte - greater_than or equals, больше или равно) 
Owner.objects.filter(owner_property__start_date__gte=timezone.date(2010, 1, 1))
```

## Задание 3

```py
from django.db.models import Count
from project_first_app.models import *

""" 3.1.3
Необходимо реализовать следующие запросы:
 - Вывод даты выдачи самого старшего водительского удостоверения
 - Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
 - Выведите количество машин для каждого водителя
 - Подсчитайте количество машин каждой марки
 - Отсортируйте всех автовладельцев по дате выдачи удостоверения 
(Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct())
"""

# Выбираем все лицензии, сортируем (order_by) по дате выдачи (issue_date) и берем самую первую ([0]). Сортировка по дефолту - по возрастанию, поэтому получим самое старшее удостоверение
License.objects.order_by("issue_date")[0]
# Выбираем собственность, у которой модель автомобиля - Focus, сортируем по дате владения (order_by и start_date), но по убыванию (знак "-" gthtl start_date). Берем первую собственность, поле с датой начала собственности (start_date) и выбираем дату (date())
Property.objects.filter(car__model="Focus").order_by("-start_date")[0].start_date.date()
# Берем всех владельцев и у каждого считаем количество автомобилей (Owner.objects.annotate(Count("car"))), потом составляем пары "Имя Фамилия": "Количество машин во владении" (f'{owner.first_name} {owner.last_name}': owner.car__count})
[{f'{owner.first_name} {owner.last_name}': owner.car__count} for owner in Owner.objects.annotate(Count("car"))]
# Выбираем поле manufacturer у всех автомобилей, считаем, сколько автомобилей нашлось на каждое значение поля, выводим парами "марка" - "количество"
[{car.get('manufacturer'): car.get('id__count')} for car in Car.objects.values("manufacturer").annotate(Count("id"))]
# Выбираем владельцев, сортируем (order_by) по дате выдачи лицензии (license__issue_date) и берем уникальных (distinct()), потому что может быть несколько удостоверений
Owner.objects.order_by("license__issue_date").distinct()
```