from django.db import models


class ReaderModel(models.Model):
    educations = (
        ('p', 'primary'),
        ('s', 'secondary'),
        ('h', 'higher'),
    )

    id = models.UUIDField(primary_key=True)
    ticket = models.IntegerField()
    name = models.CharField(max_length=100)
    passport_number = models.IntegerField()
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=1, choices=educations)
    is_has_academic_degree = models.BooleanField()
    registration_date = models.DateField()
    books_instances = models.ManyToManyField(
        'BookInstanceModel',
        through='ReaderBookModel',
        related_name='reader_book_instance'
    )
