#  Web-программирование 3 Лабараторная работа 4 задание
## Галиновский Роман К33402 2022-2023

Создать программную систему, предназначенную для организаторов ежегодных
выставок собак. Выставки могут быть моно- и полипородные. Она должна обеспечивать
хранение сведений о собаках - участниках выставок и экспертах. Участие может быть

10
индивидуальным или от клуба. У выставки могут быть спонсоры, которые могут
спонсировать разные выставки.
Должна храниться следующая информация:
1. Для каждой собаки в БД должны храниться сведения, о том, к какому клубу она
относится, кличка, порода и возраст, классность, сведения о родословной (номер
документа, клички родителей), дата последней прививки, фамилия, имя, отчество и
паспортные данные хозяина. Перед соревнованиями собаки должны пройти обязательный
медосмотр.
2. Хозяин обязан после регистрации до
прохождения медосмотра должен оплатить счет и предоставить его организаторам.
Собака допускается до соревнований, если она успешно прошла медосмотр.
3. Сведения об эксперте должны включать фамилию и имя, номер ринга, который он
обслуживает, клуб, название клуба, в котором он состоит. Каждый ринг могут
обслуживать несколько экспертов. Каждая порода собак выступает на своем ринге, но на
одном и том же ринге в разное время могут выступать разные породы.
4. Каждая собака должна выполнить 3 упражнения, за каждое из которых она
получает баллы от каждого эксперта. Итогом выставки является определение медалистов
по каждой породе по итоговому рейтингу.
5. Организатор выставки должен иметь возможность добавить в базу нового
участника или нового эксперта, снять эксперта с судейства, заменив его другим,
отстранить собаку от участия в выставке.

Организатору выставки могут потребоваться следующие сведения:
- На каком ринге выступает заданный хозяин со своей собакой?
- Какими породами представлен заданный клуб?
- Сколько собак были отстранены от участия в выставке?
- Какие эксперты обслуживают породу?
- Количество участников по каждой породе?
  
<i>Необходимо предусмотреть возможность выдачи **отчета о результатах заданной
выставки** (сколько всего участников, какие породы, сколько медалей по каждой породе).</i>

## Реализовать модели
Модель базы данных была реализована средствами Django ORM:
`models.py`
```python
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Organizer(AbstractUser):
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    patronymic = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    passport = models.CharField(max_length=20, null=False, blank=False)
    mail = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["surname", "name", "patronymic", "phone_number", "passport", "email"]

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.patronymic)

class Club(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(unique=True, max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return "Club name {}".format(self.name)

class Owner(models.Model):
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    patronymic = models.CharField(max_length=30, null=True, blank=True)
    passport = models.CharField(unique=True, max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return "Owner {} {} // ID {}".format(self.surname, self.name, self.id)

class Dog(models.Model):
    breeds = (
        ('Achihuahua', 'Achihuahua'),
        ('Apchihuahua', 'Apchihuahua'),
        ('Pudel', 'Pudel'),
        ('Sobaka', 'Sobaka'),
        ('Dobel', 'Dobel'),
        ('Ovcharka', 'Ovcharka'),
        ('Doberman', 'Doberman')
    )
    typeof_class = (
        ("Show", "Dogs of show class"),
        ("Breed", "Dogs of breed class"),
        ("Pet", "Dogs of pet class")
    )
    name = models.CharField(max_length=100, null=False, blank=True)
    breed = models.CharField( max_length=100, choices=breeds)
    full_age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    month_age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    classof_dog = models.CharField(max_length=250, choices=typeof_class)
    document = models.CharField(unique=True, max_length=20, null=False, blank=False)
    last_vaccination = models.DateField(null=False, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="owner", related_query_name="owner", verbose_name="Owner")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="club", related_query_name="club", verbose_name="Club")

    def __str__(self):
        return "{} {} // ID {}".format(self.breed, self.name, self.id)


class Show(models.Model):
    typeof_show = (
        ("Mono", "Monobreed exhibition"),
        ("Poly", "Polybreed exhibition")
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    dateof_begin = models.DateTimeField(null=False, blank=False)
    dateof_end = models.DateTimeField(null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    typeof_show = models.CharField(max_length=250, choices=typeof_show)
    host = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name="host", related_query_name="org", verbose_name="Organizer")

    def __str__(self):
        return "Show {}, begins: {}".format(self.name, self.dateof_begin)

class DogParticipation(models.Model):
    status_choices = (
        ("Participated", "Participated"),
        ("Suspended", "Suspended"),
        ("Not allowed", "Not allowed"),
        ("Absence", "Absence")
    )
    bill_choices = (
        ("Paid", "Paid"),
        ("Not paid", "Not paid")
    )
    checkup_choices = (
        ("Passed", "Medical examination was successfully passed"),
        ("Not passed", "Medical examination was not passed")
    )
    medals = (
        ("Gold", "Gold for first place"),
        ("Silver", "Silver for second place"),
        ("Bronze", "Bronze for third place"),
        ("Audience award", "Medal as audience sympathy prize")
    )
    show_dog_number = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=100, choices=status_choices)
    dateof_reg_dog = models.DateField(null=False, blank=False)
    bill = models.CharField(max_length=100, choices=bill_choices)
    checkup = models.CharField(max_length=100, choices=checkup_choices)
    dateof_checkup = models.DateField(null=True, blank=True)
    participant_dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="dog_reg_participation", related_query_name="dog_reg", verbose_name="Participant-dog")
    show_dog = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_reg_dog_participation", related_query_name="show_dog_reg", verbose_name="Exhibition")
    show_medal = models.CharField(max_length=250, choices=medals, null=True, blank=False)

    class Meta:
        unique_together = ("show_dog", "participant_dog")

    def __str__(self):
        return "{}, {}".format(self.show_dog, self.participant_dog)


class Expert(models.Model):
    surname = models.CharField(max_length=30, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    patronymic = models.CharField(max_length=30, null=True, blank=True)
    passport = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="expert_club", related_query_name="exp_club", verbose_name="Club")

    def __str__(self):
        return "Expert name is {} {} {}//ID {}".format(self.surname, self.name, self.patronymic, self.id)


class ExpertParticipation(models.Model):
    status_choices = (
        ("Participated", "Participated"),
        ("Suspended", "Suspended"),
        ("Not allowed", "Not allowed"),
        ("Absence", "Absence")
    )
    number = models.IntegerField()
    status = models.CharField(max_length=250, choices=status_choices)
    dateof_reg_exp = models.DateField()
    participant_exp = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name="exp_reg_participation", related_query_name="exp_reg", verbose_name="Participant-expert")
    show_exp = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_exp_reg_participation", related_query_name="show_exp_reg", verbose_name="Exhibition")

    class Meta:
        unique_together = ("show_exp", "participant_exp")
        unique_together = ("number", "show_exp")

    def __str__(self):
        return "{}, {}".format(self.participant_exp, self.show_exp)


class Sponsor(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Sponsorship(models.Model):
    contract_number = models.IntegerField(null=False, blank=False, unique=True)
    dateof_sign = models.DateField(null=False, blank=False)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="sponsor", related_query_name="sponsor", verbose_name="Sponsor")
    sponsor_show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="sponsor_show", related_query_name="sponsor_show", verbose_name="Exhibition")

    def __str__(self):
        return "{} - {}".format(self.sponsor, self.sponsor_show)


class ShowSchedule(models.Model):
    breeds = (
        ('Achihuahua', 'Achihuahua'),
        ('Apchihuahua', 'Apchihuahua'),
        ('Pudel', 'Pudel'),
        ('Sobaka', 'Sobaka'),
        ('Dobel', 'Dobel'),
        ('Ovcharka', 'Ovcharka'),
        ('Doberman', 'Doberman')
    )
    class_types = (
        ("Puppy", "1-9 m.o"),
        ("Junior", "9-24 m.o"),
        ("Open", "15+ m.o"),
        ("Work", "15+ m.o with certificate"),
        ("Champions", "15+ m.o with champion certificate"),
        ("Veteran", "8+ y.o")
    )
    breedof_show = models.CharField(choices=breeds, max_length=50, null=False, blank=False)
    timeof_show = models.DateTimeField(null=False, blank=False)
    numberof_ring = models.IntegerField(null=False, blank=False)
    show_class = models.CharField(max_length=200, choices=class_types, null=False, blank=False)
    show_schedule = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_schedule", related_query_name="show_schedule", verbose_name="Exhibition")

    def __str__(self):
        return "{}, {}, ring {}".format(self.show_schedule, self.breedof_show, self.numberof_ring)


class Grading(models.Model):
    schedule = models.ForeignKey(ShowSchedule, on_delete=models.CASCADE, related_name="schedule", related_query_name="schedule", verbose_name="Schedulle")
    dog = models.ForeignKey(DogParticipation, on_delete=models.CASCADE, related_name="dog", related_query_name="dog", verbose_name="Dog")
    expert = models.ForeignKey(ExpertParticipation, on_delete=models.CASCADE, related_name="expert", related_query_name="expert", verbose_name="Expert")
    first = models.IntegerField(null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    second = models.IntegerField(null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    third = models.IntegerField(null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    sum = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        if self.first is not None and self.second is not None and self.third is not None:
            self.sum = self.first + self.second + self.third
        if self.first is None and self.second is not None and self.third is not None:
            self.sum = self.second + self.third
        if self.first is not None and self.second is not None and self.third is None:
            self.sum = self.first + self.third
        if self.first is not None and self.second is not None and self.third is None:
            self.sum = self.first + self.second
        if self.first is None and self.second is None and self.third is not None:
            self.sum = self.third
        if self.first is None and self.second is not None and self.third is None:
            self.sum = self.second
        if self.first is not None and self.second is None and self.third is None:
            self.sum = self.first
        if self.first is None and self.second is None and self.third is None:
            self.sum = 0
        super(Grading, self).save(*args, **kwargs)
```
## Реализовать API средствами Django REST Framework

`serializers.py`
``` python
serializers.py
from rest_framework import serializers
from django.db.models import Q
from .models import *


class OrganizerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organizer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    dog_owner = OwnerSerializer()
    dog_club = ClubSerializer()

    class Meta:
        model = Dog
        fields = ["id", "dog_name", "breed", "full_age", "month_age","classof_dog", "document",
                  "last_vaccination", "owner", "club"]


class DogRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ["name", "breed", "full_age", "month_age", "classof_dog", "document",
                  "last_vaccination", "owner", "club"]


class ShowSerializer(serializers.ModelSerializer):
    host = OrganizerSerializer

    class Meta:
        model = Show
        fields = "__all__"


class DogParticipationSerializer(serializers.ModelSerializer):
    participant_dog = DogSerializer()
    show_dog = ShowSerializer()

    class Meta:
        model = DogParticipation
        fields = ["id", "show_dog_number", "status", "dateof_reg_dog", "bill", "checkup", "dateof_checkup",
                  "participant_dog", "show_dog", "show_medal"]


class DogParticipationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogParticipation
        fields = ["id", "show_dog_number", "status", "dateof_reg_dog", "bill", "checkup", "dateof_checkup",
                  "participant_dog", "show_dog", "show_medal"]


class ExpertSerializer(serializers.ModelSerializer):
    club = ClubSerializer

    class Meta:
        model = Expert
        fields = "__all__"


class ExpertParticipationSerializer(serializers.ModelSerializer):
    participant_exp = ExpertSerializer
    show_exp = ShowSerializer

    class Meta:
        model = ExpertParticipation
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = "__all__"


class SponsorshipSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer
    sponsor_show = ShowSerializer

    class Meta:
        model = Sponsorship
        fields = "__all__"


class ShowScheduleSerializer(serializers.ModelSerializer):
    show_schedule = ShowSerializer

    class Meta:
        model = ShowSchedule
        fields = "__all__"


class GradingSerializer(serializers.ModelSerializer):
    dog = DogParticipationSerializer
    expert = ExpertParticipationSerializer
    schedule = ShowScheduleSerializer

    class Meta:
        model = Grading
        fields = "__all__"


class DogRingSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(many=True)
    dog = DogSerializer(many=True)
    show = ShowSerializer(many=True)
    dog_reg = DogParticipationSerializer(many=True)

    class Meta:
        model = ShowSchedule
        fields = ["__all__"]


class DogBreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ["breed"]


class ClubBreedSerializer(serializers.ModelSerializer):
    members = DogBreedSerializer(many=True)

    class Meta:
        model = Club
        fields = ["name", "members"]


class DogNotAllowedOrSuspendedCountSerializer(serializers.ModelSerializer):
    miss_count = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ["dateof_begin", "miss_count"]

    def get_count(self, obj):
        return obj.show_dog_reg.filter(Q(status="Suspended") | Q(status="Not allowed")).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    show_schedule = ShowScheduleSerializer(many=True)
    experts_reg = ExpertParticipationSerializer(many=True)
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Grading
        fields = ["__all__"]
```
`views.py`
```python
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from django.db.models.aggregates import *


class OwnerListAPIView(generics.ListAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class OwnerCreateAPIView(generics.CreateAPIView):
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()


class ClubListAPIView(generics.ListAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class ClubCreateAPIView(generics.CreateAPIView):
    serializer_class = ClubSerializer
    queryset = Club.objects.all()


class DogListAPIView(generics.ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DogRetrieveSerializer
    queryset = Dog.objects.all()


class DogCreateAPIView(generics.CreateAPIView):
    serializer_class = DogRetrieveSerializer
    queryset = Dog.objects.all()


class ShowListAPIView(generics.ListAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class ShowAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class ShowCreateAPIView(generics.CreateAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class DogParticipationListAPIView(generics.ListAPIView):
    serializer_class = DogParticipationSerializer
    queryset = DogParticipation.objects.all()


class DogParticipationAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DogParticipationRetrieveSerializer
    queryset = DogParticipation.objects.all()


class DogParticipantCreateAPIView(generics.CreateAPIView):
    serializer_class = DogParticipationRetrieveSerializer
    queryset = DogParticipation.objects.all()


class ExpertListAPIView(generics.ListAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertCreateAPIView(generics.CreateAPIView):
    serializer_class = ExpertSerializer
    queryset = Expert.objects.all()


class ExpertParticipationListAPIView(generics.ListAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class ExpertParticipationAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class ExpertParticipationCreateAPIView(generics.CreateAPIView):
    serializer_class = ExpertParticipationSerializer
    queryset = ExpertParticipation.objects.all()


class SponsorListAPIView(generics.ListAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorCreateAPIView(generics.CreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()


class SponsorshipListAPIView(generics.ListAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class SponsorshipAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class SponsorshipCreateAPIView(generics.CreateAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.all()


class ShowScheduleListAPIView(generics.ListAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class ShowScheduleAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class ShowScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = ShowScheduleSerializer
    queryset = ShowSchedule.objects.all()


class GradingListAPIView(generics.ListAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.all()


class GradingAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.all()


class GradingCreateAPIView(generics.CreateAPIView):
    serializer_class = GradingSerializer
    queryset = Grading.objects.filter(~Q(dog__status="Not allowed"))

class DogRingAPIView(APIView):
    def get(self, request, id):
        rings = Grading.objects.filter(dog__participant_dog__dog_owner__id=id).values(
            "schedule__show_schedule__name", "schedule__show_schedule__begin_date",
            "dog__participant_dog__dog_name", "dog__participant_dog__breed", "schedule__ring_number")
        content = {"rings": rings}
        return Response(content)

class ClubBreedAPIView(APIView):
    def get(self, request, id):
        breeds = Dog.objects.filter(dog_club__id=id).values("breed").annotate(count=Count("breed"))
        content = {"breeds": breeds}
        return Response(content)

class DogNotAllowedOrSuspendedCountAPIView(APIView):
    def get(self, request, id):
        participants = DogParticipation.objects.filter(show_dog__id=id).filter(Q(status="Not allowed") | Q(status="Suspended"))
        counter = participants.count()
        dogs = participants.values("show_dog__name", "show_dog__begin_date", "participant_dog__breed", "participant_dog__dog_name")
        content = {"counter": counter, "dogs": dogs}
        return Response(content)




class BreedExpertsAPIView(APIView):
    def get(self, request):
        breeds = Grading.objects.values("dog__participant_dog__breed", "expert__participant_exp__expert_surname",
                                        "expert__participant_exp__expert_name", "expert__participant_exp__expert_patronymic").distinct().order_by("dog__participant_dog__breed")
        content = {"breeds": breeds}
        return Response(content)


class BreedCountAPIView(APIView):
    def get(self, request):
        breed_counter = Dog.objects.values("breed").annotate(count=Count("breed"))
        content = {"breed_counter": breed_counter}
        return Response(content)


class ReportAPIView(APIView):
    def get(self, request, id):
        show = Show.objects.get(id=id)
        show_title = show.name
        year = show.dateof_begin.year
        participants = DogParticipation.objects.filter(show_dog__id=id)
        counter = participants.count()
        breed_counter = participants.values("participant_dog__breed").annotate(count=Count("participant_dog__breed"))
        best_grades = Grading.objects.filter(schedule__show_schedule__id=id).values(
                                             "dog__participant_dog__dog_name", "dog__participant_dog__breed",
                                             "dog__id", "first", "second", "third", "sum").order_by("dog__participant_dog__breed", "sum")
        medals = DogParticipation.objects.filter(show_dog__id=id).values(
                                             "participant_dog__dog_name", "participant_dog__breed",
                                             "show_medal").annotate(medals_count=Count("show_medal")).order_by(
                                             "participant_dog__breed", "dog__sum")
        content = {
            "show_title": show_title,
            "year": year,
            "participants_number": counter,
            "breeds": breed_counter,
            "best_grades": best_grades,
            "medals": medals
        }
        return Response(content)
```
`urls.py`
```python
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *

app_name = "pet_app"

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v2",
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="roman.galinovski@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path("owner/", OwnerListAPIView.as_view()),
    path("owner/<int:pk>/", OwnerAPIView.as_view()),
    path("owner/create/", OwnerCreateAPIView.as_view()),
    path("club/", ClubListAPIView.as_view()),
    path("club/<int:pk>/", ClubAPIView.as_view()),
    path("club/create/", ClubCreateAPIView.as_view()),
    path("dog/", DogListAPIView.as_view()),
    path("dog/<int:pk>/", DogAPIView.as_view()),
    path("dog/create/", DogCreateAPIView.as_view()),
    path("show/", ShowListAPIView.as_view()),
    path("show/<int:pk>/", ShowAPIView.as_view()),
    path("show/create/", ShowCreateAPIView.as_view()),
    path("dog_reg/", DogParticipationListAPIView.as_view()),
    path("dog_reg/<int:pk>/", DogParticipationAPIView.as_view()),
    path("dog_reg/create/", DogParticipantCreateAPIView.as_view()),
    path("expert/", ExpertListAPIView.as_view()),
    path("expert/<int:pk>/", ExpertAPIView.as_view()),
    path("expert/create/", ExpertCreateAPIView.as_view()),
    path("expert_reg/", ExpertParticipationListAPIView.as_view()),
    path("expert_reg/<int:pk>/", ExpertParticipationAPIView.as_view()),
    path("expert_reg/create/", ExpertParticipationCreateAPIView.as_view()),
    path("sponsor/", SponsorListAPIView.as_view()),
    path("sponsor/<int:pk>/", SponsorAPIView.as_view()),
    path("sponsor/create/", SponsorCreateAPIView.as_view()),
    path("sponsorship/", SponsorshipListAPIView.as_view()),
    path("sponsorship/<int:pk>/", SponsorshipAPIView.as_view()),
    path("sponsorship/create/", SponsorshipCreateAPIView.as_view()),
    path("schedule/", ShowScheduleListAPIView.as_view()),
    path("schedule/<int:pk>/", ShowScheduleAPIView.as_view()),
    path("schedule/create/", ShowScheduleCreateAPIView.as_view()),
    path("grading/", GradingListAPIView.as_view()),
    path("grading/<int:pk>/", GradingAPIView.as_view()),
    path("grading/create", GradingCreateAPIView.as_view()),
    path("dog_ring/<int:id>/", DogRingAPIView.as_view()),
    path("club_breeds/<int:id>/", ClubBreedAPIView.as_view()),
    path("miss_count/<int:id>/", DogNotAllowedOrSuspendedCountAPIView.as_view()),
    path("breed_experts/", BreedExpertsAPIView.as_view()),
    path("breeds_count/", BreedCountAPIView.as_view()),
    path("report/<int:id>/", ReportAPIView.as_view()),
    path("doc/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("doc/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
```
## Подключение регистрации / авторизации по токенам / вывода информации о текущем пользователе средствами Djoser
`settings.py`
``` python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'pet_app',
    'djoser',
    'django_extensions',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
]
```
`urls.py`
```python
urlpatterns = [
    path("owner/", OwnerListAPIView.as_view()),
    path("owner/<int:pk>/", OwnerAPIView.as_view()),
    path("owner/create/", OwnerCreateAPIView.as_view()),
    path("club/", ClubListAPIView.as_view()),
    path("club/<int:pk>/", ClubAPIView.as_view()),
    path("club/create/", ClubCreateAPIView.as_view()),
    path("dog/", DogListAPIView.as_view()),
    path("dog/<int:pk>/", DogAPIView.as_view()),
    path("dog/create/", DogCreateAPIView.as_view()),
    path("show/", ShowListAPIView.as_view()),
    path("show/<int:pk>/", ShowAPIView.as_view()),
    path("show/create/", ShowCreateAPIView.as_view()),
    path("dog_reg/", DogParticipationListAPIView.as_view()),
    path("dog_reg/<int:pk>/", DogParticipationAPIView.as_view()),
    path("dog_reg/create/", DogParticipantCreateAPIView.as_view()),
    path("expert/", ExpertListAPIView.as_view()),
    path("expert/<int:pk>/", ExpertAPIView.as_view()),
    path("expert/create/", ExpertCreateAPIView.as_view()),
    path("expert_reg/", ExpertParticipationListAPIView.as_view()),
    path("expert_reg/<int:pk>/", ExpertParticipationAPIView.as_view()),
    path("expert_reg/create/", ExpertParticipationCreateAPIView.as_view()),
    path("sponsor/", SponsorListAPIView.as_view()),
    path("sponsor/<int:pk>/", SponsorAPIView.as_view()),
    path("sponsor/create/", SponsorCreateAPIView.as_view()),
    path("sponsorship/", SponsorshipListAPIView.as_view()),
    path("sponsorship/<int:pk>/", SponsorshipAPIView.as_view()),
    path("sponsorship/create/", SponsorshipCreateAPIView.as_view()),
    path("schedule/", ShowScheduleListAPIView.as_view()),
    path("schedule/<int:pk>/", ShowScheduleAPIView.as_view()),
    path("schedule/create/", ShowScheduleCreateAPIView.as_view()),
    path("grading/", GradingListAPIView.as_view()),
    path("grading/<int:pk>/", GradingAPIView.as_view()),
    path("grading/create", GradingCreateAPIView.as_view()),
    path("dog_ring/<int:id>/", DogRingAPIView.as_view()),
    path("club_breeds/<int:id>/", ClubBreedAPIView.as_view()),
    path("miss_count/<int:id>/", DogNotAllowedOrSuspendedCountAPIView.as_view()),
    path("breed_experts/", BreedExpertsAPIView.as_view()),
    path("breeds_count/", BreedCountAPIView.as_view()),
    path("report/<int:id>/", ReportAPIView.as_view()),
    path("doc/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("doc/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
```
