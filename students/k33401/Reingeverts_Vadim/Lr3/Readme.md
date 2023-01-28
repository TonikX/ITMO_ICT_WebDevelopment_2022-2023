# Laboratory work 3
> Рейнгеверц В.А. - K33401



## Practical part

![](https://i.imgur.com/IGscva6.png)


### 3.1.1

```bash
python manage.py shell
```

```python
from project_first_app.models import *

Car.objects.create(license_plate="x000xx", brand="Mitsubishi", model="Mitsubishi Lancer 2017", color="#000000")

>>> Car.objects.all()
<QuerySet [<Car: Ford Tahoe 2021>, <Car: Ford F-150 2012>, <Car: Ford Explorer 2010>, <Car: KIA Rio 2010>, <Car: Hyundai Elantra 2012>, <Car: Renault Duster 2005>, <Car: Honda Civic 2007>, <Car: Mitsubishi Lancer 2017>]>

Car.objects.create(license_plate="x001xx", brand="Mitsubishi", model="Mitsubishi Outlander 2017", color="#000000")



```

## Lab work part
