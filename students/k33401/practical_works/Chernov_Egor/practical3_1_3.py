from simple_django_web_project.django_project_cars.cars_first_app.models import *
from django.db.models import Max, Min, Count

DriverLicense.objects.aggregate(oldest_license=Min('issue_date'))

Ownership.objects.aggregate(oldest_license=Max('start_date'))

counter_car = Driver.objects.annotate(count_car=Count("driver_ownership"))
for driver in counter_car:
    print(driver.pk, driver.count_car)

Car.objects.values("car_brand").annotate(count=Count("id"))


Driver.objects.order_by('driver_license__issue_date')
