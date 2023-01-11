# Лабораторная работа №2

## Описание работы
Вариант про выставку собак. 

Запрос, которые надо реализовать:
- На каком ринге выступает собака
- Какими породами представлен заданный клуб
- Сколько собак были отсранены от участия в выставке
- Какие эксперты обслуживают породу
- Количество участников по каждой породе

- Реализовать модель базы данных средствами DjangoORM (согласовать с преподавателем на консультации).
- При необходимости, студент может согласовать модель базы данных с преподавателем и только потом приступить к описанию модели средствами Django ORM. 
- Реализовать логику работу API средствами Django REST Framework (используя методы сериализации).

Далее представлена реализация основных файлов работы

## Файлы

* `models.py`
Создание сущностей и их отношений
```python
from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def str(self):
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

    def str(self):
        return str(self.year)


class Participation(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    medal_types = (
        ('g', 'gold'),
        ('s', 'silver'),
        ('b', 'bronze'),
    )
    medal = models.CharField(max_length=1, choices=medal_types, null=True, blank=True)
    rings = models.ManyToManyField('Ring', null=True, blank=True)
    vaccinated = models.DateField()
    dismissed = models.BooleanField()
    final_grade = models.IntegerField(blank=True, null=True)

    def str(self):
        return f'{self.participant}'


class Expert(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

    def str(self):
        return f'{self.name} {self.last_name}'


class Club(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('Participant',
                                     related_name='club_members'
                                     )

    def str(self):
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

    def str(self):
        return f'{self.show} {self.breed}'
```

* `views.py`
Создание действий
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


class RingParticipationRetrieveAPIView(generics.RetrieveAPIView):
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
        # breed_count = Participant.objects.filter(breed=breed).count()
        breed_count = Ring.objects \
            .values('breed').annotate(count=Count('breed'))
        content = {'breed_count': breed_count}
        return Response(content)

# class BreedCountAPIView(generics.ListAPIView):
#     serializer_class = ParticipantSerializer
#     lookup_url_kwarg = "breed"
#
#     def get_queryset(self):
#         breed = self.kwargs.get(self.lookup_url_kwarg)
#         participants = Participant.objects.filter(breed=breed)
#         print(participants)
#         return participants


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

* `serializers.py`
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

    class Meta:
        model = Participation
        fields = ["rings"]


class ParticipantBreedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = ["breed"]


class ClubBreedsSerializer(serializers.ModelSerializer):
    members = ParticipantBreedsSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class RingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ring
        fields = "__all__"


class DismissedCountSerializer(serializers.ModelSerializer):

    dismissed_count = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        fields = ["dismissed_count"]

    def get_dismissed_count(self, obj):
        return Participation.objects.filter(dismissed=True).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Ring
        fields = ["breed", "experts"]
```

* `urls.py`
Создание ссылок
```python
from django.urls import path
from .views import *


app_name = "dogsapp"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participation/', ParticipationAPIList.as_view()),
    path('participants/', ParticipantAPIList.as_view()),

    path('participant_ring/<int:pk>', RingParticipationRetrieveAPIView.as_view()),
    path('club_breeds/<int:pk>', ClubBreedsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('breed_experts/', BreedExpertsAPIView.as_view()),
    path('breeds_count/', BreedCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]
```

