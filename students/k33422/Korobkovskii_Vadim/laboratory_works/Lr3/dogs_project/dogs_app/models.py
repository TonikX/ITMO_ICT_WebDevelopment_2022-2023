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

    def __str__(self):
        return f"{self.sponsor_name}"


class Sponsorship(models.Model):
    contract_number = models.IntegerField("Номер контракта/Contract number", null=False, blank=False, unique=True)
    sign_date = models.DateField("Дата подписания контракта/Contract sign date", null=False, blank=False)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="sponsor", related_query_name="sponsor", verbose_name="Спонсор/Sponsor")
    sponsor_show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="sponsor_show", related_query_name="sponsor_show", verbose_name="Выставка/Exhibition")

    def __str__(self):
        return f"{self.sponsor} for {self.sponsor_show}"


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


