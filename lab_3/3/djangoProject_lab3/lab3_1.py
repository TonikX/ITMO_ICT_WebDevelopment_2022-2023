from lab3.models import *
from datetime import datetime

D1 = Driver.objects.create(first_name="D1", second_name="Clemens", birthday=datetime.now())
D2 = Driver.objects.create(first_name="D2", second_name="Nicholas", birthday=datetime.now())
D3 = Driver.objects.create(first_name="D3", second_name="Adela", birthday=datetime.now())
D5 = Driver.objects.create(first_name="D5", second_name="Finger", birthday=datetime.now())
D6 = Driver.objects.create(first_name="D6", second_name="Goldsmith", birthday=datetime.now())
D7 = Driver.objects.create(first_name="D7", second_name="Roger", birthday=datetime.now())

C1 = Car.objects.create(number="A1", marka="Audi", model="Audi1", color="black")
C2 = Car.objects.create(number="A2", marka="Audi", model="Audi2", color="write")
C3 = Car.objects.create(number="A3", marka="Audi", model="Audi1", color="green")
C4 = Car.objects.create(number="B1", marka="Audi", model="Audi1", color="black")
C5 = Car.objects.create(number="B2", marka="BAOMA", model="baoma", color="red")

L1 = License.objects.create(id_Driver=D1, number_license="123", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))
L2 = License.objects.create(id_Driver=D2, number_license="123123", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))
L3 = License.objects.create(id_Driver=D3, number_license="1234", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))
L4 = License.objects.create(id_Driver=D5, number_license="132513", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))
L5 = License.objects.create(id_Driver=D6, number_license="32453", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))
L6 = License.objects.create(id_Driver=D7, number_license="67856", data_got=datetime.datetime(2013, 11, 20, 20, 9, 26, 423063))



owner1 = Owner.objects.create(id_Driver=D1, id_Car=C1, data_start=datetime.datetime(2015, 10, 20, 20, 9, 26, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))
owner2 = Owner.objects.create(id_Driver=D2, id_Car=C1, data_start=datetime.datetime(2017, 11, 20, 20, 9, 16, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))
owner3 = Owner.objects.create(id_Driver=D3, id_Car=C3, data_start=datetime.datetime(2013, 10, 20, 20, 10, 26, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))
owner4 = Owner.objects.create(id_Driver=D5, id_Car=C4, data_start=datetime.datetime(2010, 11, 20, 20, 5, 26, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))
owner5 = Owner.objects.create(id_Driver=D6, id_Car=C5, data_start=datetime.datetime(2010, 11, 20, 20, 9, 26, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))
owner6 = Owner.objects.create(id_Driver=D7, id_Car=C3, data_start=datetime.datetime(2011, 11, 20, 20, 9, 26, 423063),
                              data_end=datetime.datetime(2019, 11, 20, 20, 9, 26, 423063))

from django.db.models import Max, Count, Min, Avg
Car.objects.filter(marka="BAOMA")
Driver.objects.filter(first_name="D1")
Owner.objects.filter(id_car__color="red")
Owner.objects.filter(data_start__year__lt=1999)
License.objects.aggregate(Min("data_got"))
count_cars = Owner.objects.annotate(Count("id_car"))
for count in count_cars:
    print(count.id_driver, count.id_car__count)

Car.objects.values("marka").annotate(Count("marka"))

Licenses = License.objects.order_by("data_got")
for license in Licenses:
    print(license.id_driver)
