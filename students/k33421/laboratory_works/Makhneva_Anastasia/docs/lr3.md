# Лабораторная работа №3
## Основные файлы
`models.py`
```python
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
                                          # through='Participation',
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
```
`serializers.py`
```python
from rest_framework import serializers
from .models import *

class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        fields = "__all__"

class ParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = "__all__"


class RingParticipationSerializer(serializers.ModelSerializer):
    '''На каком ринге выступает заданный хозяин со своей собакой?'''

    class Meta:
        model = Participation
        fields = ["rings"]


class ParticipantBreedsSerializer(serializers.ModelSerializer):
    '''Количество участников по каждой породе?'''
    class Meta:
        model = Participant
        fields = ["breed"]


class ClubBreedsSerializer(serializers.ModelSerializer):
    '''Какими породами представлен заданный клуб?'''
    members = ParticipantBreedsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ring
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):
    '''Сколько собак были отстранены от участия в выставке?'''
    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ['dismissed_count']

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    '''Какие эксперты обслуживают породу?'''
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Ring
        fields = ["breed", "experts"]
```
`views.py`
```python
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from django.db.models.aggregates import Count, Sum


class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()

class ParticipationAPIList(generics.ListCreateAPIView):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()

class ParticipantAPIList(generics.ListCreateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()


class RingParticipationAPIView(generics.RetrieveAPIView):
    serializer_class = RingParticipationSerializer
    queryset = Participation.objects.all()


class ClubBreedsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClubBreedsSerializer
    queryset = Club.objects.all()


class DismissedCountAPIView(generics.RetrieveAPIView):
    serializer_class = DismissedCountSerializer
    queryset = Participation.objects.all()

# leave name
class BreedExpertsAPIView(generics.ListAPIView):
    serializer_class = BreedExpertsSerializer
    queryset = Ring.objects.all()


class BreedCountAPIView(APIView):

    def get(self, request):
        # breed_count = Participant.objects.filter(breed=breed).count()
        breed_count = Participant.objects \
            .values('breed').annotate(count=Count('breed'))
        content = {'breed_count': breed_count}
        return Response(content)


class BreedCountAPIView(APIView):

    def get(self, request):
        breed_count = Ring.objects \
            .values('breed').annotate(count=Count('breed'))
        content = {'breed_count': breed_count}
        return Response(content)


class ReportAPIView(APIView):

    def get(self, request, year):
        participants = Show.objects.get(year=year).participants
        participant_count = participants.count()
        breed_count = participants.values('breed').annotate(count=Count('breed'))
        best_grades = Participation.objects.filter(rings__show__year=year)\
            .values('participant')\
            .annotate(ex_sum=Sum('final_grade'))\
            .order_by()
        medals = Participation.objects.values('rings__breed')\
            .annotate(medals_count=Count('medal'))
        content = {'participant_count': participant_count,
                   'breeds': breed_count,
                   'best_grades': best_grades,
                   'medals': medals}
        return Response(content)
```
`urls.py`
```python
from django.urls import path
from .views import *


app_name = "dogsapp"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participation/', ParticipationAPIList.as_view()),
    path('participants/', ParticipantAPIList.as_view()),

    path('participant_ring/<int:pk>', RingParticipationAPIView.as_view()),
    path('club_breeds/<int:pk>', ClubBreedsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('breed_experts/', BreedExpertsAPIView.as_view()),
    path('breeds_count/', BreedCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]
```
## Данные обо всех участиях
Выводит информацию о каждой записи об участии собаки в выставке.

URL: `/participation/`

Method: `GET`

Auth required : YES

Permissions required : None

Data constraints : {}
```python
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 13,
        "medal": "s",
        "vaccinated": "2022-01-03",
        "dismissed": false,
        "final_grade": 11,
        "participant": 17,
        "rings": [
            2
        ]
    },
    {
        "id": 14,
        "medal": "s",
        "vaccinated": "2021-04-03",
        "dismissed": false,
        "final_grade": 11,
        "participant": 15,
        "rings": [
            3
        ]
    },
    {
        "id": 15,
        "medal": "b",
        "vaccinated": "2021-03-03",
        "dismissed": true,
        "final_grade": 0,
        "participant": 16,
        "rings": [
            1
        ]
    }
]
```
