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
    types = (
        ("Mono", "Monobreed exhibition"),
        ("Poly", "Polybreed exhibition")
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    dateof_begin = models.DateTimeField(null=False, blank=False)
    dateof_end = models.DateTimeField(null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=250, null=False, blank=False)
    typeof_show = models.CharField(max_length=250, choices=types)
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