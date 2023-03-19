import datetime
from django.db import models


class ReaderModel(models.Model):
    def get_next_primary_key(self) -> int:
        return ReaderModel.objects.aggregate(models.Max('ticket'))['ticket'] + 1

    educations = (
        ('p', 'primary'),
        ('s', 'secondary'),
        ('h', 'higher'),
    )

    ticket = models.IntegerField(primary_key=True, default=get_next_primary_key)
    name = models.CharField(max_length=100)
    passport_number = models.IntegerField()
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=1, choices=educations)
    is_has_academic_degree = models.BooleanField()
    registration_date = models.DateField(default=datetime.date.today)
