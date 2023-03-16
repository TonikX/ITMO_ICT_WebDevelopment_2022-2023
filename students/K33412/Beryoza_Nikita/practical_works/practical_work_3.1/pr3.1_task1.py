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
                username='new_batch_user'+str(i),
                first_name=['Владислав', 'Анатолий',
                            'Степан', 'Евгений', 'Олег', 'Сергей'][i],
                last_name=['Петров', 'Попов', 'Антонов',
                           'Иванов', 'Егоров', 'Орлов'][i]
            ),
            license_number='1234567'+str(i),
            issue_date=timezone.now()).owner,
        car=Car.objects.create(
            number='AO17'+str(i),
            manufacturer='Ford',
            model='Focus',
            color=['Красный', 'Синий', 'Белый',
                   'Серый', 'Желтый', 'Оранжевый'][i]
        ), start_date=timezone.now()
    )
