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

Car.objects.filter(manufacturer='LADA')
Owner.objects.filter(first_name='Олег')
License.objects.get(owner=Owner.objects.last())
Owner.objects.filter(owner_property__car__color='Синий')
Owner.objects.filter(owner_property__start_date__gte=timezone.date(2010,1,1))
