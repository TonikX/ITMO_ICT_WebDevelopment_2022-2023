from simple_django_web_project.django_project_cars.cars_first_app.models import *


Car.objects.filter(car_brand="Prototype")

Driver.objects.filter(first_name="Stive")

rand_id_driver = Driver.objects.get(first_name="TestFN5").pk
DriverLicense.objects.get(id_driver=rand_id_driver)

Driver.objects.filter(driver_ownership__id_car__color="red")

Driver.objects.filter(driver_ownership__start_date__gte="2020-01-01")
