from django.db import models
from django.contrib.auth.models import AbstractUser

class Organizer(AbstractUser):
    tel = models.CharField(verbose_name='Телефон', max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username

class Participant(models.Model):
    name = models.CharField(max_length=100)
    breed_types = (
        ('h', 'haski'),
        ('t', 'terrier'),
        ('b', 'bulldog'),
    )
    breed = models.CharField(max_length=1, choices=breed_types)
    age = models.IntegerField()
    family = models.CharField(max_length=1000)
    owner_data = models.CharField(max_length=1000)
    club = models.ForeignKey('Club', on_delete=models.CASCADE,
                             null=True, blank=True
                             )

    def __str__(self):
        return self.name


class Show(models.Model):
    year = models.IntegerField(primary_key=True)
    show_types = (
        ('mono', 'mono-breed'),
        ('poly', 'poly-breed')
    )
    type = models.CharField(max_length=4, choices=show_types)
    participants = models.ManyToManyField('Participant',
                                          related_name='show_participants'
                                         )

    def __str__(self):
        return str(self.year)


class Participation(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    medal_types = (
        ('g', 'gold'),
        ('s', 'silver'),
        ('b', 'bronze'),
    )
    medal = models.CharField(max_length=1, choices=medal_types, null=True)
    rings = models.ManyToManyField('Ring', null=True, blank=True)
    vaccinated = models.DateField()
    dismissed = models.BooleanField()
    final_grade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.participant}'


class Expert(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Club(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('Participant',
                                     related_name='club_members'
                                     )

    def __str__(self):
        return self.name


class Ring(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    experts = models.ManyToManyField('Expert',
                                     # through='Grade'
                                     related_name='ring_experts',
                                     null=True,
                                     blank=True
                                     )
    breed_types = (
        ('h', 'haski'),
        ('t', 'terrier'),
        ('b', 'bulldog'),
    )
    breed = models.CharField(max_length=1, choices=breed_types)

    def __str__(self):
        return f'{self.show} {self.breed}'

