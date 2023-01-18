from lab3.models import *
from datetime import datetime

Alex = Driver.objects.create(first_name="Alex", second_name="Clemens", birthday="1998-01-01 12:12")
Eartha = Driver.objects.create(first_name="Eartha", second_name="Nicholas", birthday="1998-01-01 12:12")
May = Driver.objects.create(first_name="May", second_name="Adela", birthday="1998-01-01 12:12")
Tommy = Driver.objects.create(first_name="Tommy", second_name="Finger", birthday="1998-01-01 12:12")
Dewar = Driver.objects.create(first_name="Dewar", second_name="Goldsmith", birthday="1998-01-01 12:12")
Flower = Driver.objects.create(first_name="Flower", second_name="Roger", birthday="1998-01-01 12:12")

lic1 = License.objects.create(id_Driver=Alex, number_license="123", data_got="1998-01-01 12:12")
lic2 = License.objects.create(id_Driver=Eartha, number_license="123123", data_got="1998-02-02 12:12")
lic3 = License.objects.create(id_Driver=May, number_license="1234", data_got="1998-03-03 12:12")
lic4 = License.objects.create(id_Driver=Tommy, number_license="132513", data_got="1998-04-04 12:12")
lic5 = License.objects.create(id_Driver=Dewar, number_license="32453", data_got="1998-05-05 12:12")
lic6 = License.objects.create(id_Driver=Flower, number_license="67856", data_got="1998-06-06 12:12")

Audi_1 = Car.objects.create(number="A1", marka="Audi", model="A6", color="black")
Audi_2 = Car.objects.create(number="A2", marka="Audi", model="A6l", color="purple")
BMW_1 = Car.objects.create(number="A3", marka="BMW", model="B4", color="black")
Bugatti_2 = Car.objects.create(number="B1", marka="Bugatti", model="F1", color="black")
Bugatti_3 = Car.objects.create(number="B2", marka="Bugatti", model="F2", color="red")

owner1 = Owner.objects.create(id_Driver=Alex, id_Car=Audi_1, data_start="1998-01-01 12:12",
                              data_end="1999-03-25 12:12")
owner2 = Owner.objects.create(id_Driver=Eartha, id_Car=Audi_1, data_start="1998-01-06 12:12",
                              data_end="1999-05-11 12:12")
owner3 = Owner.objects.create(id_Driver=May, id_Car=BMW_1, data_start="1998-01-01 12:12",
                              data_end="1999-01-21 12:12")
owner4 = Owner.objects.create(id_Driver=Tommy, id_Car=Bugatti_2, data_start="1998-01-12 12:12",
                              data_end="1999-01-21 12:12")
owner5 = Owner.objects.create(id_Driver=Dewar, id_Car=Bugatti_3, data_start="1998-05-12 12:12",
                              data_end="1999-02-21 12:12")
owner6 = Owner.objects.create(id_Driver=Flower, id_Car=BMW_1, data_start="1999-12-05 12:12",
                              data_end="2000-11-11 15:12")
from django.db.models import Max, Count, Min, Avg
Car.objects.filter(marka="BMW")
Driver.objects.filter(first_name__regex="Alex")
Owner.objects.filter(id_Car__color="red")
Owner.objects.filter(data_start__year__gte=1999)
License.objects.aggregate(Min("data_got"))
count_cars = Owner.objects.annotate(Count("id_car"))
for count in count_cars:
    print(count.id_driver, count.id_car__count)

Car.objects.values("marka").annotate(Count("marka"))

Licenses = License.objects.order_by("data_got")
for license in Licenses:
    print(license.id_driver)
