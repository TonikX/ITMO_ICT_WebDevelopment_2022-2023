# **Практическая работа №3.1**
Django заапросы и их выполнение.

-------------------------

## **Задание 3.1.1**
Описание: напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей. Задание можете выполнить либо в интерактивном режиме интерпретатора, либо в отдельном python-файле. Результатом должны стать запросы и отображение созданных объектов.

* `models.py` - модель базы данных
```python
class Car_owner(models.Model):
    id_owner = models.IntegerField(primary_key = True)
    last_name = models.CharField(max_length = 30, null = False)
    first_name = models.CharField(max_length = 30, null = False)
    birth_day = models.DateField(null = True)

class Car(models.Model):
    id_car = models.IntegerField(primary_key = True)
    state_number = models.CharField(max_length = 15, null = False)
    mark_car = models.CharField(max_length = 20, null = False)
    model_car = models.CharField(max_length = 20, null = False)
    color =  models.CharField(max_length = 30, null = True)

class Ownership(models.Model):
    id_owner_car = models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE, related_name='owner')
    id_car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name='car')
    start_date = models.DateField()
    end_date = models.DateField(null = True)

class Driver_license(models.Model):
    id_license =  models.IntegerField(primary_key = True)
    id_owner = models.ForeignKey(Car_owner, on_delete = models.CASCADE, related_name='car_owner')
    license_number = models.CharField(max_length = 10, null = False)
    category = models.CharField(max_length = 10, null = False)
    date_of_license= models.DateField()
```

-------------------------

### Создание сущностей 

* Создание владельцев автомибилей 

![Процесс создания владельцев](https://sun9-north.userapi.com/sun9-88/s/v1/ig2/8Wj9MQ-W4qQMSEGOf1mN2UYe5fnXuzbGywb6t3a7bXwI0o7mE1xvUPRB2d7BYjXKHEYPT67ctInbCj2hK4GBpDWA.jpg?size=1468x220&quality=96&type=album)

* Создание автомибилей 

![Процесс создания автомобилей](https://sun9-north.userapi.com/sun9-81/s/v1/ig2/xQJ0X7hd46gJqGYnjyInGvthbEBVW86NB1JZ-rk4R5zVVdR5bEw3FuDh8qn-wgG4GaHl4fU-zRMkVCUn9ioYP851.jpg?size=1454x167&quality=96&type=album)

* Создание прав 

![Процесс создания прав](https://sun9-west.userapi.com/sun9-46/s/v1/ig2/WF9OAU5YY1yra3Cb5DTB2xra7nheVyz3z-TEU15NRMXP_UCwMOv2TBvFY6bY-vCiq99WEndwRjbqRPaaZl8ZKgUc.jpg?size=1499x290&quality=96&type=album)

* Связь между владельцем и автомобилем 

![Связываем владельца и автомобилиста](https://sun9-north.userapi.com/sun9-81/s/v1/ig2/6vWL-HIJyNHWpu3PkRY8AJF47sDQK5mHCcDGiSJ8hcQZkFILkoXvAWzl_tyPtMcDD1AAewsmsZjqzKeLTrtbCCOY.jpg?size=1480x295&quality=96&type=album)

-------------------------

## **Задание 3.1.2**
Описание: По созданным в пр.1 данным написать следующие запросы на фильтрацию:


* Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть):

![Запрос с машинами](https://sun9-north.userapi.com/sun9-86/s/v1/ig2/jjszv9yj9pd8NQE9UN9CMPc2fB7ZalKwZKGW1OTRqdussL49SL4OSpQuBjMlMNCVyuK26ehtBWTPNxhCKC1ohBJo.jpg?size=495x56&quality=96&type=album)


* Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение):

![Запрос с именами](https://sun9-west.userapi.com/sun9-56/s/v1/ig2/KtcmJ4VJ_yoHRwv2NoBz3z6O1T6ad4tvT62VtwNkCrOiv5QretFSQQ_mepY_VIBkYyMD5evK2r8BqxLM6DtzNXU-.jpg?size=579x55&quality=96&type=album)

* Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса):

![Запрос с id](https://sun9-west.userapi.com/sun9-7/s/v1/ig2/93NnUGlxCGNxRJRsei0AhBOzL1WvIz3SfZeSjWXA8iH6oWKu3drXiZCDfrwkAg0MKJvoT0NZHizNVRjAyR1zsLL6.jpg?size=928x50&quality=96&type=album)

* Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует):

![Запрос с владельцами машин определенного цвета](https://sun9-west.userapi.com/sun9-1/s/v1/ig2/i138JCeUXMdWcE-9cxJ087WNzlcbzdMvimnUK1wczY1dfxw6lszcRV--1Ukh0tv2E46xa4U2_Yz7dnVyvQjQCqc4.jpg?size=1430x54&quality=96&type=album)

* Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе):

![Запрос с годом владения](https://sun9-east.userapi.com/sun9-36/s/v1/ig2/MH6oWEBeabqvU7Y2eI0toCZxYKuTTknxGvdX4LN2-s2x--j1bfPB1y8n-W0pdK0eSwlt3XPmM4ZeTJOozoNDjzZG.jpg?size=1321x58&quality=96&type=album)

-------------------------

## **Задание 3.1.3**

Описание: необходимо реализовать следующие запросы:

* Вывод даты выдачи самого старшего водительского удостоверения:

![Запрос со старшим удостоверением](https://sun9-west.userapi.com/sun9-63/s/v1/ig2/Zd2BjN1ydeacIiOHqsXkPUxxQwszd3luvnu88I4leibhv2BRHoW1N9Txv7HqnmRKZYxoZ3KDGmFhWr2AKH0OIGWG.jpg?size=875x79&quality=96&type=album)


* Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе:

![Запрос с поздней датой](https://sun9-west.userapi.com/sun9-65/s/v1/ig2/1ThPPBiFiteYu3IwAMCw5DCQVfMJsJ7OW9opAg0zxPjbwiiz0sIlAOFr1kQ-vqSnVKfaN1oQQMRAkTT-raqJZmoS.jpg?size=746x47&quality=96&type=album)

* Выведите количество машин для каждого водителя:

![Запрос с количеством машин](https://sun9-north.userapi.com/sun9-82/s/v1/ig2/RBtbp0VMnwxy86W3AH_GhheXMtsmdlUOF2sVpWWdlc0Fsw9b-jQZLvypd02XN5ccOAFjV2sC7ulRlr26ESI1QGd9.jpg?size=1474x88&quality=96&type=album)

* Подсчитайте количество машин каждой марки:

![Запрос с количеством машин](https://sun9-west.userapi.com/sun9-56/s/v1/ig2/DpuUFCUZvP5DTiuj8zCL8mseKO2imnePp9lzCczGD6jBAW1ulA6DHNSfKaqh_OEju3KAwzGaUC39rK4MXe3XBCol.jpg?size=1484x78&quality=96&type=album)

* Отсортируйте всех автовладельцев по дате выдачи удостоверения:

![Запрос с сортировкой автовладельцев](https://sun9-west.userapi.com/sun9-15/s/v1/ig2/XodPjyzaPrfbhZ2-_3RU_dpRvwiPR8DM9YD3jutAkx7LymfDYALGXj6E0wPahWFNhJ-Q-gqhp21ifviU_fWh2YBS.jpg?size=1318x60&quality=96&type=album) 