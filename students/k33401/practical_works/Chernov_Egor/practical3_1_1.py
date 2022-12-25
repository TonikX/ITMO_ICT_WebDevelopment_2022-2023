from simple_django_web_project.django_project_cars.cars_first_app.models import *

drivers = []
for i in range(1, 7):
    new_driver = Driver(username=f"driver{i}", first_name=f"TestFN{i}", last_name=f"TestSN{i}", birthday=f"2000-07-0{i}", passport=f"111111111{i}", password="123")
    drivers.append(new_driver)
    new_driver.save()

i = 1
for driver in drivers:
    new_license = DriverLicense(id_driver=driver, license_number=f"111111111{i}", type='B', issue_date=f"2022-12-0{i}")
    new_license.save()
    i += 1

cars = []
for i in range(1, 7):
    new_car = Car(license_plate=f"a00{i}aa", car_brand='Prototype', model=f"v{i}")
    cars.append(new_car)
    new_car.save()

for i in range(len(drivers)):
    new_ownership = Ownership(id_driver=drivers[i], id_car=cars[i], start_date=f"2020-01-0{i+1}", end_date=f"2022-12-0{i+1}")
    new_ownership.save()
