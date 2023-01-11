# Лабораторная работа №3

## Задание
Реализовать сайт, используя фреймворк Django 3 и СУБД PostgreSQL *, в
соответствии с вариантом задания лабораторной работы.



##Основные файлы:
`models.py`
```python
from django.db import models
from django.contrib.auth.models import AbstractUser


class Organizer(AbstractUser):
    tel = models.CharField(verbose_name='phone number', max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel']

    def __str__(self):
        return self.username


class Participant(models.Model):
    name = models.CharField(max_length=100)
    fandom_types = (
        ('n', 'naruto'),
        ('h', 'harry potter'),
        ('s', 'supernatural'),
        ('d', 'doctor who')
    )
    fandom = models.CharField(max_length=1, choices=fandom_types)
    age = models.IntegerField()
    character = models.CharField(max_length=1000)
    club = models.ForeignKey('Club', on_delete=models.CASCADE,
                             null=True, blank=True
                             )

    def __str__(self):
        return self.name


class Show(models.Model):
    year = models.IntegerField(primary_key=True)
    show_types = (
        ('mono', 'mono-fandom'),
        ('poly', 'poly-fandom')
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
    stage = models.ManyToManyField('Stage', null=True, blank=True)
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


class Stage(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    experts = models.ManyToManyField('Expert',
                                     # through='Grade'
                                     related_name='stage_experts',
                                     null=True,
                                     blank=True
                                     )
    fandom_types = (
        ('n', 'naruto'),
        ('h', 'harry potter'),
        ('s', 'supernatural'),
        ('d', 'doctor who')
    )
    fandom = models.CharField(max_length=1, choices=fandom_types)

    def __str__(self):
        return f'{self.show} {self.fandom}'


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


class StageParticipationAPIView(generics.RetrieveAPIView):
    serializer_class = StageParticipationSerializer
    queryset = Participation.objects.all()


class ClubFandomsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClubFandomsSerializer
    queryset = Club.objects.all()


class DismissedCountAPIView(generics.RetrieveAPIView):
    serializer_class = DismissedCountSerializer
    queryset = Participation.objects.all()


class FandomExpertsAPIView(generics.ListAPIView):
    serializer_class = FandomExpertsSerializer
    queryset = Stage.objects.all()


class FandomCountAPIView(APIView):

    def get(self, request):
        fandom_count = Participant.objects \
            .values('fandom').annotate(count=Count('fandom'))
        content = {'fandom_count': fandom_count}
        return Response(content)


class FandomCountAPIView(APIView):

    def get(self, request):
        fandom_count = Stage.objects \
            .values('fandom').annotate(count=Count('fandom'))
        content = {'fandom_count': fandom_count}
        return Response(content)


class ReportAPIView(APIView):

    def get(self, request, year):
        participants = Show.objects.get(year=year).participants
        participant_count = participants.count()
        fandom_count = participants.values('fandom').annotate(count=Count('fandom'))
        best_grades = Participation.objects.filter(stage__show__year=year)\
            .values('participant')\
            .annotate(ex_sum=Sum('final_grade'))\
            .order_by()
        medals = Participation.objects.values('stage__fandom')\
            .annotate(medals_count=Count('medal'))
        content = {'participant_count': participant_count,
                   'fandoms': fandom_count,
                   'best_grades': best_grades,
                   'medals': medals}
        return Response(content)

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


class StageParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = ["stage"]


class ParticipantFandomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ["fandom"]


class ClubFandomsSerializer(serializers.ModelSerializer):
    members = ParticipantFandomsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):
    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ['dismissed_count']

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class FandomExpertsSerializer(serializers.ModelSerializer):
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Stage
        fields = ["fandom", "experts"]

```

`urls.py`
```python
from django.urls import path
from .views import *


app_name = "lab3_app"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participation/', ParticipationAPIList.as_view()),
    path('participants/', ParticipantAPIList.as_view()),

    path('participant_stage/<int:pk>', StageParticipationAPIView.as_view()),
    path('club_fandoms/<int:pk>', ClubFandomsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('fandom_experts/', FandomExpertsAPIView.as_view()),
    path('fandoms_count/', FandomCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]

```

# Показать все участия

Выводит информацию о каждой записи об участии

**URL** : `/participation/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Warriors": [
    {
        "id": 1,
        "medal": "g",
        "dismissed": false,
        "final_grade": 100,
        "participant": 1,
        "stage": [
            1
        ]
    },
    {
        "id": 2,
        "medal": "b",
        "dismissed": false,
        "final_grade": 61,
        "participant": 2,
        "stage": [
            2
        ]
    },
    {
        "id": 3,
        "medal": "g",
        "dismissed": false,
        "final_grade": 23,
        "participant": 1,
        "stage": [
            1
        ]
    }
    ]
}
```