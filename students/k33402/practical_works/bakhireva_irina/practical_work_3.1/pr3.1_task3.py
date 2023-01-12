from project_first_app.models import *
from django.utils import timezone
from django.db.models import Count

""" 3.1.3
Необходимо реализовать следующие запросы:
 - Вывод даты выдачи самого старшего водительского удостоверения
 - Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
 - Выведите количество машин для каждого водителя
 - Подсчитайте количество машин каждой марки
 - Отсортируйте всех автовладельцев по дате выдачи удостоверения 
(Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct())
"""

License.objects.order_by("issue_date")[0]
Property.objects.filter(car__model="Focus").order_by("-start_date")[0].start_date.date()
[{f'{owner.first_name} {owner.last_name}': owner.car__count} for owner in Owner.objects.annotate(Count("car"))]
[{car.get('manufacturer'): car.get('id__count')} for car in Car.objects.values("manufacturer").annotate(Count("id"))]
Owner.objects.order_by("license__issue_date").distinct()