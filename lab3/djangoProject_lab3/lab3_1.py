from lab3.models import *
from datetime import datetime

driver1 = Driver.objects.create(username="driver1")
driver2 = Driver.objects.create(username="driver2")
driver3 = Driver.objects.create(username="driver3")
driver4 = Driver.objects.create(username="driver4")
driver5 = Driver.objects.create(username="driver5")
driver6 = Driver.objects.create(username="driver6")

lic1 = Driver_license.objects.create(id_Driver=driver1, number_license="1", data_got="2022-01-01 10:10")
lic2 = Driver_license.objects.create(id_Driver=driver2, number_license="2", data_got="2022-02-02 10:10")
lic3 = Driver_license.objects.create(id_Driver=driver3, number_license="3", data_got="2022-03-03 10:10")
lic4 = Driver_license.objects.create(id_Driver=driver4, number_license="4", data_got="2022-04-04 10:10")
lic5 = Driver_license.objects.create(id_Driver=driver5, number_license="5", data_got="2022-05-05 10:10")
lic6 = Driver_license.objects.create(id_Driver=driver6, number_license="6", data_got="2022-06-06 10:10")

car1 = Car.objects.create(number="111", marka="bmw", model="A", color="red")
car2 = Car.objects.create(number="222", marka="ford", model="B", color="green")
car3 = Car.objects.create(number="333", marka="jeep", model="C", color="yellow")
car4 = Car.objects.create(number="444", marka="jeep", model="C", color="yellow")
car5 = Car.objects.create(number="555", marka="jeep", model="D", color="purple")

owner1 = Owner.objects.create(id_Driver=driver1, id_Car=car1, data_start="2022-01-01 10:10",
                              data_end="2022-02-05 10:10")
owner2 = Owner.objects.create(id_Driver=driver2, id_Car=car2, data_start="2022-01-06 10:10",
                              data_end="2022-03-01 10:10")
owner3 = Owner.objects.create(id_Driver=driver3, id_Car=car3, data_start="2022-01-01 10:10",
                              data_end="2022-05-01 10:10")
owner4 = Owner.objects.create(id_Driver=driver4, id_Car=car4, data_start="2022-01-12 10:10",
                              data_end="2022-01-01 10:10")
owner5 = Owner.objects.create(id_Driver=driver5, id_Car=car5, data_start="2022-05-12 10:10",
                              data_end="2022-02-01 10:10")
owner6 = Owner.objects.create(id_Driver=driver6, id_Car=car1, data_start="2022-02-05 10:10",
                              data_end="2022-11-01 10:10")

#●	Выведете все машины марки “jeep”
Car.objects.filter(marka="jeep")
#●	Найти всех водителей с именем “driver n”
Driver.objects.filter(username__regex="driver[1-9]")
#●	Вывести всех владельцев красных машин
Owner.objects.filter(id_Car__color="red")
#●	Найти всех владельцев, чей год владения машиной начинается с 2022
Owner.objects.filter(data_start__year__gte=2022)

from django.db.models import Max, Count, Min, Avg

# ●	Вывод даты выдачи самого старшего водительского удостоверения
Driver_license.objects.aggregate(Min("data_got"))
# ●	Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
Owner.objects.aggregate(Max("data_start"))
# ●	Выведите количество машин для каждого водителя
count_cars = Owner.objects.annotate(Count("id_Car"))
for c in count_cars:
    print(c.id_Driver, c.id_Car__count)

# ●	Подсчитайте количество машин каждой марки
Car.objects.values("marka").annotate(Count("marka"))

# Отсортируйте всех автовладельцев по дате выдачи удостоверения
lics = Driver_license.objects.order_by("data_got")
for lic in lics:
    print(lic.id_Driver)
