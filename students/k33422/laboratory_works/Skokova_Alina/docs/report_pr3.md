# Практическая работа № 3.1. Django Web framework. Запросы и их выполнение.

## Задание 1

- Напишите запрос на создание 6-7 новых автовладельцев

![Create owners](img\pr3\create_owners.PNG)

- и 5-6 автомобилей,

![Create cars](img\pr3\create_cars.PNG)

- каждому автовладельцу назначьте удостоверение

![Create license](img\pr3\create_license.PNG)

- и от 1 до 3 автомобилей.

![Create ownership](img\pr3\create_ownership.PNG)

## Задание 2

По созданным в задании 1 данным написать следующие запросы на фильтрацию:

- Где это необходимо, добавьте related_name к полям модели

```python
from django.db import models

class CarOwner(models.Model):
    id_owner = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class DriverLicense(models.Model):
    id_license = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(CarOwner, related_name="owner_license", on_delete=models.CASCADE)
    license_num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField(blank=False)

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    state_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(blank=True, max_length=30)
    owners = models.ManyToManyField(
        CarOwner,
        through='Ownership',
        through_fields=('id_car', 'id_owner'),
    )

    def __str__(self):
        return "{} {} {}".format(self.brand, self.model, self.state_num)


class Ownership(models.Model):
    id_owner_car = models.AutoField(primary_key=True)
    id_owner = models.ForeignKey(CarOwner, related_name="owner_ownership", on_delete=models.CASCADE)
    id_car = models.ForeignKey(Car,related_name="car_ownership", on_delete=models.CASCADE)
    date_start = models.DateField(blank=False)
    date_end = models.DateField(blank=True, null=True)
```

- Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

![2_1](img\pr3\2_1.PNG)

- Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

![2_2](img\pr3\2_2.PNG)

- Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)

![2_3](img\pr3\2_3.PNG)

- Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

![2_4](img\pr3\2_4.PNG)

- Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

![2_5](img\pr3\2_5.PNG)

## Задание 3

Необходимо реализовать следующие запросы:

- Вывод даты выдачи самого старшего водительского удостоверения

![3_1](img\pr3\3_1.PNG)

- Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе

![3_2](img\pr3\3_2.PNG)

- Выведите количество машин для каждого водителя

![3_3](img\pr3\3_3.PNG)

- Подсчитайте количество машин каждой марки

![3_4](img\pr3\3_4.PNG)

- Отсортируйте всех автовладельцев по дате выдачи удостоверения

![3_5](img\pr3\3_5.PNG)