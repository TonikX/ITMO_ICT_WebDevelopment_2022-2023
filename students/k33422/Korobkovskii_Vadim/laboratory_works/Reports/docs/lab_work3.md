# Лабораторная работа №3

## Задание
`Необходимо:`


  1. Реализовать модель базы данных средствами DjangoORM согласно выбранному варианту.

  2. Реализовать логику работы API средствами Django REST Framework, используя методы сериализации.
 
  3. Подключить регистрацию, авторизацию по токенам и вывод информации о текущем пользователе средствами Djoser

  4. Выполнить практическую работу №3.1

## Выбранный вариант

Создать программную систему, предназначенную для организаторов ежегодных
выставок собак. Выставки могут быть моно- и полипородные. Она должна обеспечивать
хранение сведений о собаках - участниках выставок и экспертах. Участие может быть индивидуальным или от клуба. У выставки могут быть спонсоры, которые могут
спонсировать разные выставки.
Для каждой собаки в БД должны храниться сведения, о том, к какому клубу она
относится, кличка, порода и возраст, классность, сведения о родословной (номер
документа, клички родителей), дата последней прививки, фамилия, имя, отчество и
паспортные данные хозяина. Перед соревнованиями собаки должны пройти обязательный
медосмотр.
Т.к. участие является платным, то хозяин обязан после регистрации до
прохождения медосмотра должен оплатить счет и предоставить его организаторам.
Собака допускается до соревнований, если она успешно прошла медосмотр.
Сведения об эксперте должны включать фамилию и имя, номер ринга, который он
обслуживает, клуб, название клуба, в котором он состоит. Каждый ринг могут
обслуживать несколько экспертов. Каждая порода собак выступает на своем ринге, но на
одном и том же ринге в разное время могут выступать разные породы.
Каждая собака должна выполнить 3 упражнения, за каждое из которых она
получает баллы от каждого эксперта. Итогом выставки является определение медалистов
по каждой породе по итоговому рейтингу.
Организатор выставки должен иметь возможность добавить в базу нового
участника или нового эксперта, снять эксперта с судейства, заменив его другим,
отстранить собаку от участия в выставке.


`Организатору выставки могут потребоваться следующие сведения:`
:

  1. На каком ринге выступает заданный хозяин со своей собакой?

  2. Какими породами представлен заданный клуб?
 
  3. Сколько собак были отстранены от участия в выставке?

  4. Какие эксперты обслуживают породу?

  5. Количество участников по каждой породе?

Необходимо предусмотреть возможность выдачи отчета о результатах заданной
выставки (сколько всего участников, какие породы, сколько медалей по каждой породе).

## Реализация 

* `Файл с моделями (базами данных) models.py`
``` python
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Organizer(AbstractUser):
    org_surname = models.CharField("Фамилия/Surname", max_length=30, null=False, blank=False)
    org_name = models.CharField("Имя/Name", max_length=30, null=False, blank=False)
    org_patronymic = models.CharField("Отчество/Patronymic", max_length=30, null=True, blank=True)
    org_phone_number = models.CharField("Номер телефона/Phone number", max_length=20, null=True, blank=True)
    org_passport = models.CharField("Серия и номер пасспорта/Passport number", max_length=20, null=False, blank=False)
    org_email = models.EmailField("Электронная почта/Email address", unique=True)
    REQUIRED_FIELDS = ["org_surname", "org_name", "org_patronymic", "org_phone_number", "org_passport", "org_email"]

    def __str__(self):
        return f"{self.org_surname} {self.org_name} {self.org_patronymic}"


class Owner(models.Model):
    owner_surname = models.CharField("Фамилия хозяина/Owner's surname", max_length=30, null=False, blank=False)
    owner_name = models.CharField("Имя хозяина/Owner's name", max_length=30, null=False, blank=False)
    owner_patronymic = models.CharField("Отчество хозяина/Owner's patronymic", max_length=30, null=True, blank=True)
    owner_passport = models.CharField("Серия и номер пасспорта хозяина/Owner's passport number", unique=True, max_length=30, null=False, blank=False)
    owner_phone_number = models.CharField("Номер телефона/Phone number", max_length=20, unique=True, null=False, blank=False)
    owner_email = models.CharField("Почта/E-mail", max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Хозяин/Owner {self.owner_surname} {self.owner_name} (ID {self.id})"


class Club(models.Model):
    name = models.CharField("Название клуба/Club name", max_length=100, null=False, blank=False)
    club_phone_number = models.CharField("Номер телефона/Phone number", unique=True, max_length=20, null=False, blank=False)
    club_email = models.CharField("Почта/E-mail", max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Клуб/Club {self.name}"


class Dog(models.Model):
    breeds = (
        ('Корги/Corgi', 'Корги/Corgi'),
        ('Немецкая овчарка/German shepherd', 'Немецкая овчарка/German shepherd'),
        ('Бигль/Beagle', 'Бигль/Beagle'),
        ('Пудель/Poodle', 'Пудель/Poodle'),
        ('Ретривер/Retriever', 'Ретривер/Retriever'),
        ('Самоед/Samoyed', 'Самоед/Samoyed'),
        ('Доберман/Doberman', 'Доберман/Doberman')
    )
    class_types = (
        ("Show", "Собаки класса show/Dogs of show class"),
        ("Breed", "Собаки класса breed/Dogs of breed class"),
        ("Pet", "Собаки класса pet/Dogs of pet class")
    )
    dog_name = models.CharField("Кличка/Name", max_length=100, null=False, blank=True)
    breed = models.CharField("Порода/Breed", max_length=100, choices=breeds)
    full_age = models.IntegerField("Полный возраст в годах/Full age in years", null=False, blank=False, validators=[MinValueValidator(0)])
    month_age = models.IntegerField("Полный возраст в месяцах/Full age in months", null=False, blank=False, validators=[MinValueValidator(0)])
    dog_class = models.CharField("Класс/Class", max_length=250, choices=class_types)
    document = models.CharField("Номер документа о родословной/Number of the pedigree document", unique=True, max_length=20, null=False, blank=False)
    dad_name = models.CharField("Кличка отца/Dad's name", max_length=100, null=False, blank=True)
    mom_name = models.CharField("Кличка матери/Mom's name", max_length=100, null=False, blank=True)
    last_vaccination = models.DateField("Дата последней прививки/Last vaccination date", null=False, blank=False)
    dog_info = models.TextField("Информация о собаке/Info about dog", max_length=2000, null=False, blank=True)
    dog_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="dog_owner", related_query_name="dog_owner", verbose_name="Владелец/Owner")
    dog_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="dog_club", related_query_name="dog_club", verbose_name="Клуб/Club")

    def __str__(self):
        return f"{self.breed} {self.dog_name} (ID {self.id})"


class Show(models.Model):
    show_types = (
        ("Моно/Mono", "Однопородная выставка/Monobreed exhibition"),
        ("Поли/Poly", "Всепородная выставка/Polybreed exhibition")
    )
    name = models.CharField("Название выставки/Exhibition name", max_length=100, null=False, blank=False)
    begin_date = models.DateTimeField("Начало выставки/Show start", null=False, blank=False)
    end_date = models.DateTimeField("Окончание выставки/Show end", null=False, blank=False)
    city = models.CharField("Город проведения выставки/City of the show", max_length=50, null=False, blank=False)
    address = models.CharField("Адресс/Address", max_length=250, null=False, blank=False)
    show_type = models.CharField("Тип выставки/Exhibition type", max_length=250, choices=show_types)
    host = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name="host", related_query_name="org", verbose_name="Организатор/Organizer")

    def __str__(self):
        return f"Выставка/Exhibition '{self.name}', {self.begin_date}"
        #.strftime('%Y')


class DogParticipation(models.Model):
    status_choices = (
        ("Участвовал/Participated", "Участвовал/Participated"),
        ("Снят/Suspended", "Снят/Suspended"),
        ("Не допущен/Not allowed", "Не допущен/Not allowed"),
        ("Неявка/Absence", "Неявка/Absence")
    )
    bill_choices = (
        ("Оплачен/Paid", "Оплачен/Paid"),
        ("Не оплачен/Not paid", "Не оплачен/Not paid")
    )
    checkup_choices = (
        ("Пройден/Passed", "Медосмотр успешно пройден/Medical examination was successfully passed"),
        ("Не пройден/Not passed", "Медосмотр не был пройден/Medical examination was not passed")
    )
    medals = (
        ("Золото/Gold", "Золото за первое место/Gold for first place"),
        ("Серебро/Silver", "Серебро за второе место/Silver for second place"),
        ("Бронза/Bronze", "Бронза за третье место/Bronze for third place"),
        ("Медаль от зрителей/Audience award", "Медаль как приз зрительских симпатий/Medal as audience sympathy prize")
    )
    show_dog_number = models.IntegerField("Номер собаки на выставке/Dog's number on show", null=False, blank=False)
    dog_status = models.CharField("Статус собаки/Dog's status", max_length=100, choices=status_choices)
    reg_dog_date = models.DateField("Дата регистрации собаки/Dog registration date", null=False, blank=False)
    bill = models.CharField("Счёт/Bill", max_length=100, choices=bill_choices)
    checkup = models.CharField("Медосмотр/Checkup", max_length=100, choices=checkup_choices)
    checkup_date = models.DateField("Дата прохождения медосмотра/Checkup date", null=True, blank=True)
    participant_dog = models.ForeignKey(Dog, on_delete=models.CASCADE, related_name="dog_reg_participation", related_query_name="dog_reg", verbose_name="Участник-собака/Participant-dog")
    show_dog = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_reg_dog_participation", related_query_name="show_dog_reg", verbose_name="Выставка/Exhibition")
    show_medal = models.CharField("Медаль/Medal", max_length=250, choices=medals, null=True, blank=False)

    class Meta:
        unique_together = ("show_dog", "participant_dog")

    def __str__(self):
        return f"{self.show_dog}, {self.participant_dog}"


class Expert(models.Model):
    expert_surname = models.CharField("Фамилия эксперта/Expert's surname", max_length=30, null=False, blank=False)
    expert_name = models.CharField("Имя эксперта/Expert's name", max_length=30, null=False, blank=False)
    expert_patronymic = models.CharField("Отчество эксперта/Expert's patronymic", max_length=30, null=True, blank=True)
    expert_passport = models.CharField("Серия и номер пасспорта эксперта/Expert's passport number", max_length=30, null=False, blank=False)
    expert_phone_number = models.CharField("Номер телефона/Phone number", max_length=20, null=False, blank=False)
    expert_email = models.CharField("Почта/E-mail", max_length=50, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="expert_club", related_query_name="exp_club", verbose_name="Клуб/Club")

    def __str__(self):
        return f"Эксперт/Expert {self.expert_surname} {self.expert_name} {self.expert_patronymic} (ID {self.id})"


class ExpertParticipation(models.Model):
    status_choices = (
        ("Участвовал/Participated", "Участвовал/Participated"),
        ("Снят/Suspended", "Снят/Suspended"),
        ("Не допущен/Not allowed", "Не допущен/Not allowed"),
        ("Неявка/Absence", "Неявка/Absence")
    )
    show_exp_number = models.IntegerField("Номер эксперта на выставке/Expert's number on show")
    exp_status = models.CharField("Статус эксперта/Expert's status", max_length=250, choices=status_choices)
    reg_exp_date = models.DateField("Дата регистрации эксперта/Expert registration date")
    participant_exp = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name="exp_reg_participation", related_query_name="exp_reg", verbose_name="Участник-эксперт/Participant-expert")
    show_exp = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_exp_reg_participation", related_query_name="show_exp_reg", verbose_name="Выставка/Exhibition")

    class Meta:
        unique_together = ("show_exp", "participant_exp")
        unique_together = ("show_exp_number", "show_exp")

    def __str__(self):
        return f"{self.participant_exp}, {self.show_exp}"


class Sponsor(models.Model):
    sponsor_name = models.CharField("Имя спонсора/Sponsor name", max_length=200, null=False, blank=False)
    sponsor_phone_number = models.CharField("Номер телефона/Phone number", max_length=20, null=False, blank=False)
    sponsor_email = models.CharField("Почта/E-mail", max_length=50, null=True, blank=True)


class Sponsorship(models.Model):
    contract_number = models.IntegerField("Номер контракта/Contract number", null=False, blank=False, unique=True)
    sign_date = models.DateField("Дата подписания контракта/Contract sign date", null=False, blank=False)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="sponsor", related_query_name="sponsor", verbose_name="Спонсор/Sponsor")
    sponsor_show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="sponsor_show", related_query_name="sponsor_show", verbose_name="Выставка/Exhibition")


class ShowSchedule(models.Model):
    breeds = (
        ('Корги/Corgi', 'Корги/Corgi'),
        ('Немецкая овчарка/German shepherd', 'Немецкая овчарка/German shepherd'),
        ('Бигль/Beagle', 'Бигль/Beagle'),
        ('Пудель/Poodle', 'Пудель/Poodle'),
        ('Ретривер/Retriever', 'Ретривер/Retriever'),
        ('Самоед/Samoyed', 'Самоед/Samoyed'),
        ('Доберман/Doberman', 'Доберман/Doberman')
    )
    class_types = (
        ("Baby", "Собаки от 4 до 6 месяцев/Dogs from 4 to 6 months old"),
        ("Puppy", "Собаки от 6 до 9 месяцев/Dogs from 6 to 9 months old"),
        ("Junior", "Собаки от 9 до 18 месяцев/Dogs from 9 to 18 months old"),
        ("Intermediate", "Собаки от 15 до 24 месяцев/Dogs from 15 to 24 months old"),
        ("Open", "Собаки от 15 месяцев/Dogs from 15 months old"),
        ("Work", "Собаки от 15 месяцев с дипломом/Dogs from 15 months with diploma old"),
        ("Champions", "Собаки от 15 месяцев при наличии сертификата Чемпиона страны-члена FCI/Dogs from 15 months old with FCI Member country Champion certificate"),
        ("Veteran", "Собаки от 8 лет/Dogs from 8 years old")
    )
    show_breed = models.CharField("Порода/Breed", choices=breeds, max_length=50, null=False, blank=False)
    show_time = models.DateTimeField("Дата и время выступления/Date and time of performance", null=False, blank=False)
    ring_number = models.IntegerField("Номер ринга/Ring number", null=False, blank=False)
    show_class = models.CharField("Выставочный класс/Show class", max_length=200, choices=class_types, null=False, blank=False)
    show_schedule = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="show_schedule", related_query_name="show_schedule", verbose_name="Выставка/Exhibition")

    def __str__(self):
        return f"{self.show_schedule}, {self.show_breed}, ринг/ring №{self.ring_number}"


class Grading(models.Model):
    schedule_grade = models.ForeignKey(ShowSchedule, on_delete=models.CASCADE, related_name="schedule_grade", related_query_name="schedule_grade", verbose_name="Расписание/Schedulle")
    dog_grade = models.ForeignKey(DogParticipation, on_delete=models.CASCADE, related_name="dog_grade", related_query_name="dog_grade", verbose_name="Собака/Dog")
    expert_grade = models.ForeignKey(ExpertParticipation, on_delete=models.CASCADE, related_name="expert_grade", related_query_name="expert_grade", verbose_name="Эскперт/Expert")
    grade1 = models.IntegerField("Оценка за упражнение №1/Grade for exercise №1", null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    grade2 = models.IntegerField("Оценка за упражнение №2/Grade for exercise №2", null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    grade3 = models.IntegerField("Оценка за упражнение №3/Grade for exercise №3", null=False, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    sum = models.IntegerField("Сумма оценок/Grades summary", blank=True)

    def save(self, *args, **kwargs):
        if self.grade1 is not None and self.grade2 is not None and self.grade3 is not None:
            self.sum = self.grade1 + self.grade2 + self.grade3
        if self.grade1 is None and self.grade2 is not None and self.grade3 is not None:
            self.sum = self.grade2 + self.grade3
        if self.grade1 is not None and self.grade2 is not None and self.grade3 is None:
            self.sum = self.grade1 + self.grade3
        if self.grade1 is not None and self.grade2 is not None and self.grade3 is None:
            self.sum = self.grade1 + self.grade2
        if self.grade1 is None and self.grade2 is None and self.grade3 is not None:
            self.sum = self.grade3
        if self.grade1 is None and self.grade2 is not None and self.grade3 is None:
            self.sum = self.grade2
        if self.grade1 is not None and self.grade2 is None and self.grade3 is None:
            self.sum = self.grade1
        if self.grade1 is None and self.grade2 is None and self.grade3 is None:
            self.sum = 0
        super(Grading, self).save(*args, **kwargs)
```
* `Файл с представлениями views.py` 
``` python
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
    queryset = Grading.objects.filter(~Q(dog_grade__dog_status="Не допущен/Not allowed"))


#class DogRingAPIView(generics.RetrieveAPIView):
#    serializer_class = DogRingSerializer
#    queryset = ShowSchedule.objects.all()


class DogRingAPIView(APIView):
    def get(self, request, id):
        rings = Grading.objects.filter(dog_grade__participant_dog__dog_owner__id=id).values(
            "schedule_grade__show_schedule__name", "schedule_grade__show_schedule__begin_date",
            "dog_grade__participant_dog__dog_name", "dog_grade__participant_dog__breed", "schedule_grade__ring_number")
        content = {"rings": rings}
        return Response(content)

#class ClubBreedAPIView(generics.RetrieveAPIView):
    #serializer_class = ClubBreedSerializer
    #queryset = Club.objects.all()


class ClubBreedAPIView(APIView):
    def get(self, request, id):
        breeds = Dog.objects.filter(dog_club__id=id).values("breed").annotate(count=Count("breed"))
        content = {"breeds": breeds}
        return Response(content)



#class DogNotAllowedOrSuspendedCountAPIView(generics.RetrieveAPIView):
    #serializer_class = DogNotAllowedOrSuspendedCountSerializer
    #queryset = Show.objects.all()
    #def get(self, request, show, year):


class DogNotAllowedOrSuspendedCountAPIView(APIView):
    def get(self, request, id):
        participants = DogParticipation.objects.filter(show_dog__id=id).filter(Q(dog_status="Не допущен/Not allowed") | Q(dog_status="Снят/Suspended"))
        counter = participants.count()
        dogs = participants.values("show_dog__name", "show_dog__begin_date", "participant_dog__breed", "participant_dog__dog_name")
        content = {"counter": counter, "dogs": dogs}
        return Response(content)




class BreedExpertsAPIView(APIView):
    #serializer_class = BreedExpertsSerializer
    #queryset = Grading.objects.all()
    def get(self, request):
        breeds = Grading.objects.values("dog_grade__participant_dog__breed", "expert_grade__participant_exp__expert_surname",
                                        "expert_grade__participant_exp__expert_name", "expert_grade__participant_exp__expert_patronymic").distinct().order_by("dog_grade__participant_dog__breed")
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
        year = show.begin_date.year
        participants = DogParticipation.objects.filter(show_dog__id=id)
        counter = participants.count()
        breed_counter = participants.values("participant_dog__breed").annotate(count=Count("participant_dog__breed"))
        best_grades = Grading.objects.filter(schedule_grade__show_schedule__id=id).values(
                                             "dog_grade__participant_dog__dog_name", "dog_grade__participant_dog__breed",
                                             "dog_grade__id", "grade1", "grade2", "grade3", "sum").order_by("dog_grade__participant_dog__breed", "sum")
        medals = DogParticipation.objects.filter(show_dog__id=id).values(
                                             "participant_dog__dog_name", "participant_dog__breed",
                                             "show_medal").annotate(medals_count=Count("show_medal")).order_by(
                                             "participant_dog__breed", "dog_grade__sum")
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
* `Файл с сериализаторами serializers.py`
``` python
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
        fields = ["id", "dog_name", "breed", "full_age", "month_age", "document", "dad_name", "mom_name",
                  "last_vaccination", "dog_info", "dog_owner", "dog_club"]


class DogRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ["dog_name", "breed", "full_age", "month_age", "dog_class", "document", "dad_name", "mom_name",
                  "last_vaccination", "dog_info", "dog_owner", "dog_club"]


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
        fields = ["id", "show_dog_number", "dog_status", "reg_dog_date", "bill", "checkup", "checkup_date",
                  "participant_dog", "show_dog", "show_medal"]


class DogParticipationRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogParticipation
        fields = ["id", "show_dog_number", "dog_status", "reg_dog_date", "bill", "checkup", "checkup_date",
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
    dog_grade = DogParticipationSerializer
    expert_grade = ExpertParticipationSerializer
    schedule_grade = ShowScheduleSerializer

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
        fields = ["begin_date", "miss_count"]

    def get_count(self, obj):
        return obj.show_dog_reg.filter(Q(dog_status="Снят/Suspended") | Q(dog_status="Не допущен/Not allowed")).count()


class BreedExpertsSerializer(serializers.ModelSerializer):
    show_schedule = ShowScheduleSerializer(many=True)
    experts_reg = ExpertParticipationSerializer(many=True)
    experts = ExpertSerializer(many=True)

    class Meta:
        model = Grading
        fields = ["__all__"]
```
* `Файл со ссылками urls.py`
``` python
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *

app_name = "dogs_app"

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v2",
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vkorobkovskiy@gmail.com"),
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
