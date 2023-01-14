from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True)


class Ownership(models.Model):
    car_owner_id = models.ForeignKey(
        'CarOwner', on_delete=models.CASCADE, null=True, blank=True)
    car_id = models.ForeignKey(
        'Car', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                end_date__gt=models.F('start_date')), name='start_end_date_check', violation_error_message='Start date must be earlier than end date.'),
        ]


class CarOwner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField(max_length=30, null=True, blank=True)


class DriverLicense(models.Model):
    LICENSE_TYPES = (
        ('A', 'Motorcycles'),
        ('B', 'Cars'),
        ('C', 'Trucks'),
        ('D', 'Buses'),
        ('M', 'Motorbikes'),
    )
    car_owner_id = models.ForeignKey('CarOwner', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10, choices=LICENSE_TYPES,
                                    default='B')
    issue_date = models.DateTimeField()
