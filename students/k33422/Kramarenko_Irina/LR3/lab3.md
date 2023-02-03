# **Лабораторная работа 3**

-------------------------

## Задание 
Создать программную систему, предназначенную для администрации аэропорта
некоторой компании-авиаперевозчика.
Рейсы обслуживаются бортами, принадлежащими разным авиаперевозчикам. О каждом самолете необходима следующая минимальная информация: номер самолета, тип, число мест, скорость полета, компания-авиаперевозчик. Один тип самолета может летать на разных маршрутах и по одному маршруту могут летать разные типы самолетов.
О каждом рейсе необходима следующая информация: номер рейса, расстояние до пункта назначения, пункт вылета, пункт назначения; дата и время вылета, дата и время прилета, транзитные посадки (если есть), пункты посадки, дата и время транзитных посадок и дат и время их вылета, количество проданных билетов. Каждый рейс обслуживается определенным экипажем, в состав которого входят командир корабля, второй пилот, штурман и стюардессы или стюарды. Каждый экипаж может обслуживать разные рейсы на разных самолетах. Необходимо предусмотреть наличие информации о допуске члена экипажа к рейсу.
Администрация компании-владельца аэропорта должна иметь возможность принять работника на работу или уволить. При этом необходима следующая информация: ФИО, возраст, образование, стаж работы, паспортные данные. Эта же информация необходима для сотрудников сторонних компаний.

## Основные файлы
* `models.py`
```python
class Manager(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, primary_key=True)
    datetime_start = models.DateTimeField()
    datetime_fin = models.DateTimeField()
    distance = models.IntegerField()
    airport_start = models.ForeignKey('Airport', on_delete=models.CASCADE,
        related_name='airp1')
    airport_fin = models.ForeignKey('Airport', on_delete=models.CASCADE,
        related_name='airp2')
    sold_tickets = models.IntegerField()
    transit_code = models.ForeignKey('Transit', on_delete=models.CASCADE,
        blank=True, null=True)
    plane_number = models.ForeignKey('Airplane', on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.flight_number,
            self.datetime_start, self.datetime_fin, self.distance,
            self.airport_start, self.airport_fin, self.sold_tickets,
            self.transit_code, self.plane_number)

class Airport(models.Model):
    airport_name = models.CharField(max_length=3, primary_key=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    def __str__(self):
        return "{} {} {}".format(self.airport_name, self.country, self.city)

class Airplane(models.Model):
    STATUS = (('OPERATIONAL', 'operational'), ('REPAIR', 'repair'),
        ('RETIRED', 'retired'))
    BRAND = (('AIRBUS', 'Airbus S.A.S.'), ('BOEING', 'Boeing'),
        ('SUPERJET', 'Superjet'))
    COMPANY = (('S7', 'S7'), ('POBEDA', 'Победа'), ('AEROFLOT', 'Аэрофлот'),
        ('NORDSTAR', 'Nordstar'))
    plane_number = models.CharField(max_length=20, primary_key=True)
    brand = models.CharField(max_length=20, choices=BRAND)
    speed = models.IntegerField(blank=True)
    status = models.CharField(max_length=11, choices=STATUS)
    seats = models.IntegerField()
    company = models.CharField(max_length=20, choices=COMPANY)
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.plane_number, self.brand,
            self.speed, self.status, self.seats, self.company)

class Crew(models.Model):
    crew_number = models.CharField(max_length=10, primary_key=True)
    flight_number = models.ForeignKey('Flight', on_delete=models.CASCADE,
        blank=True, null=True)
    worker_id = models.ForeignKey('Worker', on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {}".format(self.crew_number,
            self.flight_number,
            self.worker_id)

class Worker(models.Model):
    OCCUP = (('COMMANDER', 'commander'), ('RELIEF PILOT', 'Relief pilot'),
        ('NAVIGATOR', 'navigator'), ('ATTENDANT', 'attendant'))
    COMPANY = (('S7', 'S7'), ('POBEDA', 'Победа'), ('AEROFLOT', 'Аэрофлот'),
        ('NORDSTAR', 'Nordstar'))
    STATUS = (('WORKING', 'working'), ('RETIRED', 'retired'), ('FIRED', 'fired'))
    worker_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    education = models.CharField(max_length=100)
    work_exp = models.IntegerField()
    passport = models.IntegerField()
    occupation = models.CharField(max_length=15, choices=OCCUP)
    access = models.BooleanField()
    employer = models.CharField(max_length=10, choices=COMPANY)
    status = models.CharField(max_length=7, choices=STATUS)
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {}".format(self.worker_id, self.name,
            self.age, self.education, self.work_exp, self.passport,
            self.occupation, self.access, self.employer, self.status)

class Transit(models.Model):
    transit_code = models.CharField(max_length=10, primary_key=True)
    datetime_start_tr = models.DateTimeField()
    datetime_fin_tr = models.DateTimeField()
    change_airport = models.ForeignKey('Airport', on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {}{}".format(self.transit_code,
            self.datetime_start_tr,
            self.datetime_fin_tr,
            self.change_airport)
```
* `views.py`
```python
from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import Worker, Airplane, Flight
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

# создание нового работника
class WorkerCreate(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

# удаление работника
class WorkerDelete(generics.DestroyAPIView):
    queryset = Worker.objects.all()

# изменение данных о работнике по id
class WorkerUpdate(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

# вывод данных о количестве бортов каждого бренда
class AirplaneBrandList(generics.ListAPIView):
    queryset = Airplane.objects.values("brand")
    serializer_class = AirplaneSerializer

# определить марку самолета, которая чаще всего летает по маршруту
class FrequentPlane(APIView):
    def get(self, request):
        airp = request.query_params.get('airports')
        airp1 = str(airp)[:3]
        airp2 = str(airp)[3:]
        queryset = Flight.objects.filter(airport_start=airp1, airport_fin=airp2)\
            .values("plane_number__brand")\
            .annotate(Count("plane_number__brand"))\
            .order_by("-plane_number__brand__count")[0]
        return Response(queryset)

# определить количество самолетов, находящихся в ремонте
class RepairAirplanes(APIView):
    def get(self, request):
        queryset = Airplane.objects.filter(status='REPAIR')\
            .aggregate(Count("plane_number"))
        return Response(queryset)

# определить количество работников компании-авиаперевозчика
class WorkersNumber(APIView):
    def get(self, request):
        company = request.query_params.get('employer')
        queryset = Worker.objects.filter(employer=company)\
            .aggregate(Count("worker_id"))
        return Response(queryset)

# определить общее количество бортов по каждой марке
class AirplaneBrand(APIView):
    def get(self, request):
        queryset = Airplane.objects.values('brand').annotate(Count('plane_number'))
        return Response(queryset)
```
* `serializers.py`
```python
from rest_framework import serializers
from .models import Worker, Airplane, Flight

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

class FlightPercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['airport_start', 'airport_fin']

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Flight
        fields = ['flight_number', 'number_seats']

class RepairAirplanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['plane_number__count']

class WorkersNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['worker_id__count']

class AirplaneBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['brand', 'plane_number__count']
```
* `urls.py`
```python
from django.urls import path
from .views import *

API_PREFIX = 'api/v1'
app_name = "led_app"

urlpatterns = [
    path('worker/create/', WorkerCreate.as_view()),
    path('worker/fire/<int:pk>/', WorkerDelete.as_view()),
    path('worker/update/<int:pk>/', WorkerUpdate.as_view()),
    path('brand_route/', FrequentPlane.as_view()),
    path('repair/', RepairAirplanes.as_view()),
    path('company/workers/', WorkersNumber.as_view()),
    path('company/airplanes/', AirplaneBrand.as_view()),
]
```