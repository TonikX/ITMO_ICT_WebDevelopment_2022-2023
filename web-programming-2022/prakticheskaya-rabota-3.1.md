---
description: ПР3.1 - Django Web framework
---

# Практическая работа 3.1

### Practice 1

* practice1.py

Script for adding data:

```
from cars_first_app.models import *

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
```

### Practice 2

* models.py

Add related\_name into DriverLicense, Ownership models:

```
class DriverLicense(models.Model):
    id_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driver_license")
    license_number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()


class Ownership(models.Model):
    id_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driver_ownership")
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_ownership")
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
```

* practic2.py

Get all cars with "Prototype" brand:

```
Car.objects.filter(car_brand="Prototype")
```

Get all drivers with "Stive" name:

```
Driver.objects.filter(first_name="Stive")
```

Get driver license for random driver id:

```
rand_id_driver = Driver.objects.get(first_name="TestFN5").pk
DriverLicense.objects.get(id_driver=rand_id_driver)
```

Get all drivers who have a red car:

```
Driver.objects.filter(driver_ownership__id_car__color="red")
```

Get all drivers who have car from 2020 year:

```
Driver.objects.filter(driver_ownership__start_date__gte="2020-01-01")
```

#### Practice 3 <a href="#3-task" id="3-task"></a>

* practic3.py

Get date of the oldest driver license:

```
DriverLicense.objects.aggregate(oldest_license=Min('issue_date'))
```

Get last date of ownership:

```
Ownership.objects.aggregate(oldest_license=Max('start_date'))
```

Get drivers and their ownerships:

```
counter_car = Driver.objects.annotate(count_car=Count("driver_ownership"))
for driver in counter_car:
    print(driver.pk, driver.count_car)
```

Get drivers who sorted by issue date of license:

```
Driver.objects.order_by('driver_license__issue_date')
```

### Practice 3.2 <a href="#pw-32" id="pw-32"></a>

#### 1. <a href="#1-task_1" id="1-task_1"></a>

* views.py

Add two classes for GET and POST request for driver:

```
class DriverAPIView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response({"Drivers": serializer.data})


class CreateDriverAPIView(APIView):
    def post(self, request):
        driver = request.data.get("driver")
        serializer = CreateDriverSerializer(data=driver)

        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()

        return Response({"Success": "Driver '{}' created succesfully.".format(driver_saved.username)})
```

* serializer.py

For these classes serializers:

```
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class CreateDriverSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Driver.objects.create(**validated_data)

    class Meta:
        model = Driver
        fields = "__all__"
```

### 2.

Get driver with license and ownerships:

* views.py

```
class RetrieveDriverAPIView(generics.RetrieveAPIView):
    serializer_class = RetrieveDriverSerializer
    queryset = Driver.objects.all()
```

* serializers.py

```
class DriverOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownership
        fields = "__all__"


class RetrieveDriverSerializer(serializers.ModelSerializer):
    driver_ownership = DriverOwnershipSerializer(many=True, read_only=True)
    driver_license = DriverLicenseSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ("pk", "username", "first_name", "last_name", "email", "birthday",
                  "passport", "address", "nationality", "driver_license", "driver_ownership")
```

PUT and DELETE requests for driver:

* views.py

```
class RetrieveDriverUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetrieveDriverUpdateDestroySerializer
    queryset = Driver.objects.all()
```

* serializer.py

```
class RetrieveDriverUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"
```

### Practice 3.3

* settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cars_first_app',
    'rest_framework',
    'drf_yasg',
]
```

* urls.py

```
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nathanbounkouta8@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...,
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```
