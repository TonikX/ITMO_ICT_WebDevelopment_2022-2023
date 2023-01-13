# Практическая работа 3.1

##Задание 3.1.1
Описание: напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.
###models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    # Create your models here.
    
    
    class Car_owner(models.Model):
        id_owner = models.IntegerField(primary_key = True)
        last_name = models.CharField(max_length = 30, null = False)
        first_name = models.CharField(max_length = 30, null = False)
        birth_day = models.DateField(null = True)
        passport = models.IntegerField(null=True)
        address = models.CharField(max_length=50, null=True, blank=True)
        nationality = models.CharField(max_length=20, null=True, blank=True)
    
    class Car(models.Model):
        id_car = models.IntegerField(primary_key = True)
        state_number = models.CharField(max_length = 15, null = False)
        mark_car = models.CharField(max_length = 20, null = False)
        model_car = models.CharField(max_length = 20, null = False)
        color =  models.CharField(max_length = 30, null = True)
    
    class Ownership(models.Model):
        id_owner_car = models.IntegerField(primary_key = True)
        id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
        id_car = models.ForeignKey(Car, on_delete = models.CASCADE)
        start_date = models.DateField()
        end_date = models.DateField(null = True)
    
    class Driver_license(models.Model):
        id_license =  models.IntegerField(primary_key = True)
        id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE)
        license_number = models.CharField(max_length = 10, null = False)
        type = models.CharField(max_length = 10, null = False)
        date_of_license= models.DateField()

###Создание автовладельцев:
    Car_owner(1, 'Царьков', 'Григорий', '1990-01-1').save()
    Car_owner(2, 'Герасимов', 'Максим', '1991-01-1').save()
    Car_owner(3, 'Захаров', 'Таир', '1992-01-1').save()
    Car_owner(4, 'Костень', 'Анна', '1993-01-1').save()
    Car_owner(5, 'Дальше', 'Лень', '1994-01-1').save()

    for i in Car_owner.objects.all():
        ...:     print(i)
        ...: 
    Car_owner object (1)
    Car_owner object (2)
    Car_owner object (3)
    Car_owner object (4)
    Car_owner object (5)

    for i in Car_owner.objects.all():
    ...:     print(i.id_owner)
    ...: 
    1
    2
    3
    4
    5

###Создание автомобилей
    Car(1, 'A1A1', 'BMW', 'Model1', 'white').save()
    Car(2, 'B2B2', 'BMW', 'Model2', 'black').save()
    Car(3, 'C3C3', 'Toyota', 'Model3', 'blue').save()
    Car(4, 'D4D4', 'Toyota', 'Model4', 'white').save()
    Car(5, 'E5E5', 'Audi', 'Model5', 'red').save()
    Car(6, 'F6F6', 'Audi', 'Model6', 'balck').save()

###Создание водительских прав
    Driver_license(1, 1, '1234567', 'B', '2010-01-01').save()
    Driver_license(2, 2, '4567890', 'B', '2011-01-01').save()
    Driver_license(3, 3, '6527810', 'B', '2012-01-01').save()
    Driver_license(4, 4, '65228340', 'B', '2013-01-01').save()
    Driver_license(5, 5, '15228143', 'B', '2014-01-01').save()
    Driver_license(6, 6, '13298123', 'B', '2015-01-01').save()

###Владение автомобилей
    Ownership(1, 1, 1, '2011-01-01', '2012-01-01').save()
    Ownership(2, 2, 2, '2012-01-01', '2013-01-01').save()
    Ownership(3, 3, 3, '2013-01-01', '2014-01-01').save()
    Ownership(4, 4, 4, '2014-01-01', '2015-01-01').save()
    Ownership(5, 5, 5, '2015-01-01', '2016-01-01').save()
    Ownership(6, 6, 6, '2016-01-01', '2017-01-01').save()



##Задание 3.1.2
Описание: по созданным в пр.1 данным написать следующие запросы на фильтрацию:

###Запрос 1
Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):
   
    In [45]: Car.objects.filter(mark_car="Toyota")
    
    Out[45]: <QuerySet [<Car: Car object (3)>, <Car: Car object (4)>]>

###Запрос 2
Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):

    In [46]: Car_owner.objects.filter(first_name="FN3")
    Out[46]: <QuerySet [<Car_owner: Car_owner object (3)>]>

###Запрос 3
Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):

    In [48]: take_id = Car_owner.objects.all()[1].id_owner
    In [49]: Driver_license.objects.get(id_owner=take_id)
    Out[49]: <Driver_license: Driver_license object (2)>

###Запрос 4
Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):
 
    In [2]: Car_owner.objects.filter(ownership__id_car__color = 'red')
    Out[2]: <QuerySet [<Car_owner: Car_owner object (5)>]>


###Запрос 5
Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):

    In [3]: Car_owner.objects.filter(ownership__start_date__gte>"2010-01-01")
    Out[3]: <QuerySet [<Car_owner: Car_owner object (3)>, <Car_owner: Car_owner object (4)>, <Car_owner: Car_owner object (5)>, <Car_owner: Car_owner object (6)>]>



##Задание 3.1.3
Описание: необходимо реализовать следующие запросы:

###Запрос 1
Вывод даты выдачи самого старшего водительского удостоверения:

    In [59]: from django.db.models import Min, Max
    
    In [60]: Driver_license.objects.aggregate(date_of_license=Min("date_of_license"))
    Out[60]: {'date_of_license': datetime.date(2010, 1, 1)}

###Запрос 2
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:
 
    In [62]: Ownerdhip.objects.aggregate(start_date=Max("start_date"))
    Out[62]: {'start_date': datetime.date(2016, 1, 1)}

###Запрос 3
Выведите количество машин для каждого водителя:

    In [64]: from django.db.models import Count
    
    In [65]: Ownerdhip.objects.values("id_owner").annotate(Count("id_car"))
    Out[65]: <QuerySet [{'id_owner': 1, 'id_car__count': 1}, {'id_owner': 2, 'id_car__count': 1}, {'id_owner': 3, 'id_car__count': 1}, {'id_owner': 4, 'id_car__count': 1}, {'id_owner': 5, 'id
    _car__count': 1}, {'id_owner': 6, 'id_car__count': 1}]>

###Запрос 4
Подсчитайте количество машин каждой марки:

    In [66]: Car.objects.values("mark_car").annotate(Count("id_car"))
    Out[66]: <QuerySet [{'mark_car': 'Audi', 'id_car__count': 2}, {'mark_car': 'BMW', 'id_car__count': 2}, {'mark_car': 'Toyota', 'id_car__count': 2}]>

###Запрос 5
Отсортируйте всех автовладельцев по дате выдачи удостоверения:

    In [79]: Car_owner.objects.order_by("driver_license__date_of_license")
    Out[79]: <QuerySet [<Car_owner: Car_owner object (1)>, <Car_owner: Car_owner object (2)>, <Car_owner: Car_owner object (3)>, <Car_owner: Car_owner object (4)>, <Car_owner: Car_owner objec
    t (5)>, <Car_owner: Car_owner object (6)>]>