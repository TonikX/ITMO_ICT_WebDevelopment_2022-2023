# Laboratory work 3
> Рейнгеверц В.А. - K33401



## Practical part
![](https://i.imgur.com/IGscva6.png)



### 3.1.1
> [models.py](Pr\django_project_reingeverts\project_first_app\models.py)

Напишите запрос на создание 6-7 новых автовладельцев и 5-6 автомобилей, каждому автовладельцу назначьте удостоверение и от 1 до 3 автомобилей.

```bash
python manage.py shell
```

Автомобили
```python
from project_first_app.models import *

Car.objects.create(license_plate="x000xx", brand="Mitsubishi", model="Mitsubishi Lancer 2017", color="#000000")

# <Car: 8 Mitsubishi Lancer 2017>

Car.objects.create(license_plate="x001xx", brand="Mitsubishi", model="Mitsubishi Outlander 2017", color="#000000")

Car.objects.create(license_plate="x002xx", brand="Lexus", model="Lexus ES 2015", color="#ffffff")

Car.objects.create(license_plate="x003xx", brand="Lexus", model="Lincoln MKZ 2015", color="#ffffff")

Car.objects.create(license_plate="x004xx", brand="Toyota", model="Toyota Land Cruiser 2008", color="#000000")

Car.objects.create(license_plate="x005xx", brand="Toyota", model="Toyota Tundra 2010", color="#ffffff")

# >>> Car.objects.all()
# <QuerySet [<Car: 8 Mitsubishi Lancer 2017>, <Car: 9 Mitsubishi Outlander 2017>, <Car: 10 Lexus ES 2015>, 
# <Car: 11 Lincoln MKZ 2015>, <Car: 12 Toyota Land Cruiser 2008>, <Car: 13 Toyota Tundra 2010>]>
```

Владения
```python
from project_first_app.models import *
import datetime

Ownership.objects.create(car_id=Car.objects.get(pk=8), start_date=datetime.datetime(2018, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=9), start_date=datetime.datetime(2018, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=10), start_date=datetime.datetime(2017, 1, 1), end_date=(datetime.datetime(2018, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=11), start_date=datetime.datetime(2020, 1, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=12), start_date=datetime.datetime(2020, 1, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=13), start_date=datetime.datetime(2010, 1, 1), end_date=(datetime.datetime(2015, 1, 1)) + datetime.timedelta(days=700))

Ownership.objects.create(car_id=Car.objects.get(pk=13), start_date=datetime.datetime(2015, 2, 1), end_date=(datetime.datetime(2020, 1, 1)) + datetime.timedelta(days=700))


# >>> Ownership.objects.all()  
# <QuerySet [<Ownership: 10 - 8 Mitsubishi Lancer 2017 (2018-2019)>, <Ownership: 11 - 9 Mitsubishi Outlander 2017 (2018-2019)>, <Ownership: 12 - 10 Lexus ES 2015 (2017-2019)>, <Ownership: 13 - 11 Lincoln MKZ 2015 (2020-2021)>, <Ownership: 14 - 12 Toyota Land Cruiser 2008 (2020-2021)>, <Ownership: 15 - 13 Toyota Tundra 2010 (2010-2016)>, <Ownership: 16 - 13 Toyota Tundra 2010 (2015-2021)>]>
```

Автовладельцы
```python
from project_first_app.models import *
import datetime

owner = CarOwner.objects.create(first_name="Erin", last_name="Solstice", username="erin1",date_of_birth=datetime.datetime(1999, 1, 1), passport="1234", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=10))

owner = CarOwner.objects.create(first_name="Zorian", last_name="Kazinski", username="zorian1",date_of_birth=datetime.datetime(1992, 1, 1), passport="1111", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=11))

owner = CarOwner.objects.create(first_name="Garen", last_name="Redfang", username="garen1",date_of_birth=datetime.datetime(2005, 1, 1), passport="2222", address="", nationality="goblin")
owner.ownership_id.set(Ownership.objects.filter(pk=12))

owner = CarOwner.objects.create(first_name="Juniper", last_name="Smith", username="juniper1",date_of_birth=datetime.datetime(1998, 1, 1), passport="3333", address="", nationality="USA")
owner.ownership_id.set(Ownership.objects.filter(pk=13))

owner = CarOwner.objects.create(first_name="Ivan", last_name="Petrov", username="ivan1",date_of_birth=datetime.datetime(2000, 1, 1), passport="4444", address="", nationality="")
owner.ownership_id.set(Ownership.objects.filter(pk=14))

owner = CarOwner.objects.create(first_name="James", last_name="Garfield", username="garfield1",date_of_birth=datetime.datetime(1980, 1, 1), passport="5555", address="", nationality="cat")
owner.ownership_id.set(Ownership.objects.filter(pk__in=[15, 16]))

# >>> CarOwner.objects.all()
# <QuerySet [<CarOwner: 2 - admin ( )>, <CarOwner: 10 - erin1 (Erin Solstice)>, <CarOwner: 11 - zorian1 (Zorian Kazinski)>, <CarOwner: 12 - garen1 (Garen Redfang)>, <CarOwner: 13 - juniper1 (Juniper Smith)>, <CarOwner: 14 - ivan1 (Ivan Petrov)>, <CarOwner: 15 - garfield1 (James Garfield)>]>

```

Удостоверения
```python

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=10), serial_number="111111", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=11), serial_number="222222", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=12), serial_number="333333", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=13), serial_number="444444", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=14), serial_number="555555", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

DriverLicense.objects.create(car_owner_id=CarOwner.objects.get(pk=15), serial_number="666666", license_type="B", issue_date=datetime.datetime(2019, 1, 1))

# >>> DriverLicense.objects.all()
# <QuerySet [<DriverLicense: B - 10 - erin1 (Erin Solstice) (111111)>, <DriverLicense: B - 11 - zorian1 (Zorian Kazinski) (222222)>, <DriverLicense: B - 12 - garen1 (Garen Redfang) (333333)>, <DriverLicense: B - 
# 13 - juniper1 (Juniper Smith) (444444)>, <DriverLicense: B - 14 - ivan1 (Ivan Petrov) (555555)>, <DriverLicense: B - 15 - garfield1 (James Garfield) (666666)>]>
```

## Lab work part
