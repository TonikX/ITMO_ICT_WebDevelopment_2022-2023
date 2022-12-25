##  Structure of practical works

* **PW 3.1** - Django Web framework
* **PW 3.2** - Django rest framework
* **PW 3.3** - Documentation

## PW 3.1
### 1 task

* `practical3_1_1.py`

Script for adding data:
```python
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

### 2 task

* `models.py`

Add related_name into DriverLicense, Ownership models:
```python
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

* `practical3_1_2.py`

Get all cars with "Prototype" brand:
```python
Car.objects.filter(car_brand="Prototype")
```

Get all drivers with "Stive" name:
```python
Driver.objects.filter(first_name="Stive")
```

Get driver license for random driver id:
```python
rand_id_driver = Driver.objects.get(first_name="TestFN5").pk
DriverLicense.objects.get(id_driver=rand_id_driver)
```

Get all drivers who have a red car:
```python
Driver.objects.filter(driver_ownership__id_car__color="red")
```

Get all drivers who have car from 2020 year:
```python
Driver.objects.filter(driver_ownership__start_date__gte="2020-01-01")
```

### 3 task

* `practical3_1_3.py`

Get date of the oldest driver license:
```python
DriverLicense.objects.aggregate(oldest_license=Min('issue_date'))
```

Get last date of ownership: 
```python
Ownership.objects.aggregate(oldest_license=Max('start_date'))
```

Get drivers and their ownerships:
```python
counter_car = Driver.objects.annotate(count_car=Count("driver_ownership"))
for driver in counter_car:
    print(driver.pk, driver.count_car)
```

Get count of each brand cars:
```python
Car.objects.values("car_brand").annotate(count=Count("id"))
```

Get drivers who sorted by issue date of license:
```python
Driver.objects.order_by('driver_license__issue_date')
```

## PW 3.2
### 1 task

* `views.py`

Add two classes for GET and POST request for driver:
```python
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

* `serializes.py`

For these classes serializers:
```python
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

### 2 task

Get drivers with license:

* `views.py`

```python
class DriverAndLicenseAPIView(generics.ListAPIView):
    serializer_class = DriverAndLicenseSerializer
    queryset = Driver.objects.all()
```

* `serializes.py`

```python
class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicense
        fields = ("pk", "license_number", "type", "issue_date")


class DriverAndLicenseSerializer(serializers.ModelSerializer):
    driver_license = DriverLicenseSerializer(many=True)

    class Meta:
        model = Driver
        fields = ("pk", "username", "first_name", "last_name", "email", "birthday",
                  "passport", "address", "nationality", "driver_license")
```

Get driver with license and ownerships:

* `views.py`

```python
class RetrieveDriverAPIView(generics.RetrieveAPIView):
    serializer_class = RetrieveDriverSerializer
    queryset = Driver.objects.all()
```

* `serializers.py`

```python
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

* `views.py`

```python
class RetrieveDriverUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RetrieveDriverUpdateDestroySerializer
    queryset = Driver.objects.all()
```

* `serializer.py`

```python
class RetrieveDriverUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"
```

## PW 3.3
### 1 task

