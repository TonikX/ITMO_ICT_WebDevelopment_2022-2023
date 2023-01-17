from django.db.models import Min, Max, Count

from drivers.models import *


def task1():
    for i in range(1, 7):
        owner = CarOwner(first_name=f"owner_{i}_name", last_name=f"last_name_{i}", birthdate=f"2002-01-0{i}")
        owner.save()

    for i, owner in enumerate(CarOwner.objects.all()):
        license = License(car_owner=owner, license_number=1000 + i, reg_date="2020-01-01")
        license.save()

    for i in range(1, 6):
        car = Car(car_number=1000 + i, brand=f"brand_{i}", model=f"model_{i}", color="black")
        car.save()

    for i, owner in enumerate(CarOwner.objects.all()):
        license = License(car_owner=owner, license_number=1000 + i, reg_date="2020-01-01")
        license.save()

    for owner, car in zip(CarOwner.objects.all(), Car.objects.all()):
        own = Own(car=car, car_owner=owner, start_own_date="2022-01-01")
        own.save()

    for own in Own.objects.all():
        print(f"{own}: {own.car_owner} {own.car}")


def task2():
    print(Car.objects.filter(model="model_3"))
    print(CarOwner.objects.filter(first_name="owner_4_name"))
    print(CarOwner.objects.get(pk=2).license.all())
    print(CarOwner.objects.filter(own__car__color="black"))
    print(CarOwner.objects.filter(own__start_own_date__gte="2022-01-01"))


def task3():
    print(License.objects.aggregate(oldest_lisense=Min("reg_date")))
    print(Own.objects.aggregate(youngest_own=Max("start_own_date")))
    print(CarOwner.objects.values("id").annotate(Count("own__car")))
    print(Car.objects.values("brand").annotate(count=Count("id")))
    print(CarOwner.objects.order_by('license__reg_date').values_list("id", "license__reg_date"))


def run():
    task3()
