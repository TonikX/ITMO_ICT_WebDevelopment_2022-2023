# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

#Основные файлы

## Models.py

    from django.db import models
    from django.contrib.auth.models import AbstractUser


    class Employee(AbstractUser):
    id = models.AutoField(unique=True, primary_key=True)
    passport = models.CharField(max_length=10, verbose_name='Паспортные данные', unique=True)
    full_name = models.CharField(max_length=120, null=False, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст', default=18)
    education = models.CharField(choices=[('СПО', 'среднее профессиональное'), ('ВО', 'высшее')], max_length=3,
    verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы в годах')
    in_crew = models.IntegerField(verbose_name='Состоит в экипаже под номером', default=0)

    REQUIRED_FIELDS = ['email', 'full_name', 'experience']

    def __str__(self):
        return "{}".format(self.full_name)


    class Airplane(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    tail_number = models.CharField(max_length=8, verbose_name="Номер самолета", unique=True)
    type = models.CharField(max_length=20, verbose_name="Тип")
    seats = models.IntegerField(verbose_name="Число мест")
    velocity = models.IntegerField(verbose_name="Скорость полёта (км/ч)")
    airline = models.CharField(max_length=30, verbose_name="Авиакомпания")
    under_maintenance = models.BooleanField(default=False, verbose_name="В ремонте")

    def __str__(self):
        return "{}".format(self.tail_number)


    class FlightAsScheduled(models.Model):
    number = models.IntegerField(unique=True, primary_key=True, verbose_name="Номер рейса")
    distance = models.IntegerField(verbose_name="Расстояние до пункта назначения в км")
    departure = models.CharField(max_length=25, verbose_name="Пункт вылета")
    arrival = models.CharField(max_length=25, verbose_name="Пункт назначения")
    transit = models.ForeignKey('Transit', verbose_name="Транзит", null=True, blank=True, on_delete=models.CASCADE)
    completed = models.IntegerField(verbose_name="Количество совершённых рейсов")

    def __str__(self):
        return "{}, {} -> {}".format(self.number, self.departure, self.arrival)


    class Transit(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    destination = models.CharField(max_length=25, verbose_name="Пункт пересадки")

    def __str__(self):
        return "{}".format(self.destination)


    class Flight(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    number = models.ForeignKey('FlightAsScheduled', verbose_name="Номер рейса", on_delete=models.CASCADE)
    plane_id = models.ForeignKey('Airplane', verbose_name="Самолёт", on_delete=models.CASCADE)
    crew = models.IntegerField(verbose_name="Экипаж на борту")
    tickets_sold = models.IntegerField(verbose_name="Количество проданных билетов")
    departure_date = models.DateField(verbose_name="Дата вылета")
    departure_time = models.TimeField(verbose_name="Время вылета")
    arrival_date = models.DateField(verbose_name="Дата прилета")
    arrival_time = models.TimeField(verbose_name="Время прилета")
    transit_arrival_date = models.DateField(verbose_name="Дата транзитной посадки", blank=True, null=True)
    transit_arrival_time = models.TimeField(verbose_name="Время транзитной посадки", blank=True, null=True)
    transit_departure_date = models.DateField(verbose_name="Дата вылета из транзита", blank=True, null=True)
    transit_departure_time = models.TimeField(verbose_name="Время вылета из транзита", blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.number, self.plane_id)


    class AirlineAdministration(models.Model):
    employee = models.ForeignKey('Employee', verbose_name="ФИО сотрудника", on_delete=models.CASCADE)
    job = models.CharField(max_length=30, verbose_name="Должность")
    clearance = models.BooleanField(default=True, verbose_name="Допуск")

## Views.py
    from rest_framework import generics

    from airport_admin.serializers import *


    class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    class EmployeeModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    class AirplaneListView(generics.ListAPIView):
    serializer_class = AirplaneSerializer

    def get_queryset(self):
        queryset = Airplane.objects.all()
        maintenance_param = self.request.query_params.get('under_maintenance')

        if maintenance_param:
            queryset = queryset.filter(under_maintenance=maintenance_param)

        return queryset


    class AirplaneCreateView(generics.CreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


    class AirplaneModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


    class ScheduleListView(generics.ListAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


    class ScheduleCreateView(generics.CreateAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


    class ScheduleModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightAsScheduled.objects.all()
    serializer_class = ScheduleSerializer


    class FlightListView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()
        number = self.request.query_params.get('number', None)

        if number:
            queryset = queryset.filter(number=number)

        return queryset


    class FlightCreateView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


    class FlightModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


    class AirlineAdministrationListView(generics.ListAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


    class AirlineAdministrationCreateView(generics.CreateAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


    class AirlineAdministrationModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AirlineAdministration.objects.all()
    serializer_class = AirlineAdministrationSerializer


    class TransitListView(generics.ListAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer


    class TransitCreateView(generics.CreateAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer


    class TransitModifyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transit.objects.all()
    serializer_class = TransitSerializer

##Serializers.py
    from rest_framework import serializers
    from .models import *


    class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
    model = Employee
    fields = ['passport', 'full_name', 'age', 'education', 'experience', 'in_crew']


    class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
    model = Airplane
    fields = '__all__'


    class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
    model = FlightAsScheduled
    fields = '__all__'


    class FlightSerializer(serializers.ModelSerializer):
    class Meta:
    model = Flight
    fields = '__all__'


    class AirlineAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
    model = AirlineAdministration
    fields = '__all__'


    class TransitSerializer(serializers.ModelSerializer):
    class Meta:
    model = Transit
    fields = '__all__'

##Urls.py
    from django.urls import path
    from .views import *

    urlpatterns = [
    path('employees/', EmployeeListView.as_view()),
    path('employees/create/', EmployeeCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeModifyView.as_view()),
    path('airplanes/', AirplaneListView.as_view()),
    path('airplanes/create/', AirplaneCreateView.as_view()),
    path('airplanes/<int:pk>/', AirplaneModifyView.as_view()),
    path('schedule/', ScheduleListView.as_view()),
    path('schedule/create/', ScheduleCreateView.as_view()),
    path('schedule/<int:pk>/', ScheduleModifyView.as_view()),
    path('flights/', FlightListView.as_view()),
    path('flights/create/', FlightCreateView.as_view()),
    path('flights/<int:pk>/', FlightModifyView.as_view()),
    path('airline_admin/', AirlineAdministrationListView.as_view()),
    path('airline_admin/create/', AirlineAdministrationCreateView.as_view()),
    path('airline_admin/<int:pk>/', AirlineAdministrationModifyView.as_view()),
    path('transit/', TransitListView.as_view()),
    path('transit/create/', TransitCreateView.as_view()),
    path('transit/<int:pk>/', TransitModifyView.as_view())
    ]

#Показать все расписания 
####GET /schedule/
####HTTP 200 OK
####Allow: GET, HEAD, OPTIONS
####Content-Type: application/json
####Vary: Accept

    [
    {
    "number": 12,
    "distance": 3500,
    "departure": "Владивосток",
    "arrival": "Санкт-Петербург",
    "completed": 4,
    "transit": 1
    },
    {
    "number": 206,
    "distance": 2000,
    "departure": "Санкт-Петербург",
    "arrival": "Казань",
    "completed": 2,
    "transit": null
    },
    {
    "number": 438746,
    "distance": 2000,
    "departure": "Москва",
    "arrival": "Казань",
    "completed": 4,
    "transit": 1
    }