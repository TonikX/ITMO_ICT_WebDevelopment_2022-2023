from django.db import models
from django.contrib.auth.models import AbstractUser


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
    airport_start = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='airp1')
    airport_fin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='airp2')
    sold_tickets = models.IntegerField()
    transit_code = models.ForeignKey('Transit', on_delete=models.CASCADE, blank=True, null=True)
    plane_number = models.ForeignKey('Airplane', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.flight_number, self.datetime_start, self.datetime_fin, self.distance, self.airport_start, self.airport_fin, self.sold_tickets, self.transit_code, self.plane_number)


class Airport(models.Model):
    airport_name = models.CharField(max_length=3, primary_key=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {}".format(self.airport_name, self.country, self.city)


class Airplane(models.Model):
    # TYPE_PLANE = (('TRANSPORT', 't'), ('PASSENGER', 'p'))
    STATUS = (('OPERATIONAL', 'operational'), ('REPAIR', 'repair'), ('RETIRED', 'retired'))
    BRAND = (('AIRBUS', 'Airbus S.A.S.'), ('BOEING', 'Boeing'), ('SUPERJET', 'Superjet'))
    COMPANY = (('S7', 'S7'), ('POBEDA', 'Победа'), ('AEROFLOT', 'Аэрофлот'), ('NORDSTAR', 'Nordstar'))
    plane_number = models.CharField(max_length=20, primary_key=True)
    # type = models.CharField(max_length=10, choices=TYPE_PLANE)
    brand = models.CharField(max_length=20, choices=BRAND)
    speed = models.IntegerField(blank=True)
    status = models.CharField(max_length=11, choices=STATUS)
    seats = models.IntegerField()
    company = models.CharField(max_length=20, choices=COMPANY)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.plane_number, self.brand, self.speed, self.status, self.seats, self.company)


class Crew(models.Model):
    crew_number = models.CharField(max_length=10, primary_key=True)
    flight_number = models.ForeignKey('Flight', on_delete=models.CASCADE, blank=True, null=True)
    worker_id = models.ForeignKey('Worker', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.crew_number, self.flight_number, self.worker_id)


class Worker(models.Model):
    OCCUP = (('COMMANDER', 'commander'), ('RELIEF PILOT', 'Relief pilot'), ('NAVIGATOR', 'navigator'), ('ATTENDANT', 'attendant'))
    COMPANY = (('S7', 'S7'), ('POBEDA', 'Победа'), ('AEROFLOT', 'Аэрофлот'), ('NORDSTAR', 'Nordstar'))
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
        return "{} {} {} {} {} {} {} {} {} {}".format(self.worker_id, self.name, self.age, self.education, self.work_exp, self.passport, self.occupation, self.access, self.employer, self.status)


class Transit(models.Model):
    transit_code = models.CharField(max_length=10, primary_key=True)
    datetime_start_tr = models.DateTimeField()
    datetime_fin_tr = models.DateTimeField()
    change_airport = models.ForeignKey('Airport', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}{}".format(self.transit_code, self.datetime_start_tr, self.datetime_fin_tr, self.change_airport)