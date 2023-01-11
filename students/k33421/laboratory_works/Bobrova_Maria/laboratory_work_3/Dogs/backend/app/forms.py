from django import forms

from backend.app.models import Show, Ring, Expert, Participant, Participation, Club
from django.contrib.auth.models import User
from django.db.models import Q


class ShowForm(forms.ModelForm):
    """"Форма добавления выставки"""

    TYPES = (
        ('T1', 'Монопородная выставка'),
        ('T2', 'Полипородная выставка'),
    )

    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={"class": "form-control"}))
    city = forms.CharField(label="Город", widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Адрес", widget=forms.TextInput(attrs={"class": "form-control"}))
    show_type = forms.ChoiceField(choices=TYPES, label="Тип", widget=forms.Select(attrs={"class": "form-control"}))
    date_start = forms.CharField(label="Дата начала", widget=forms.widgets.DateInput(attrs={'type': 'date', "class": "form-control"}))
    date_finish = forms.CharField(label="Дата конца", widget=forms.widgets.DateInput(attrs={'type': 'date', "class": "form-control"}))
    image = forms.ImageField(label="Изображение")


    class Meta:
        model = Show
        fields = ("title", "city", "address", "show_type", "date_start", "date_finish","image")


class SetExpertForm(forms.ModelForm):
    """"Форма добавления эксперта на соревнование"""

    class Meta:
        model = Expert
        fields = "__all__"

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['ring'].queryset = Ring.objects.filter(exhibition__in=Show.objects.filter(
            user__in=User.objects.filter(id=id_user)
        ))
        #self.fields['expert'].queryset = Expert.objects.filter(~Q(id__in=ExpertCompetition.objects.all().values('expert')))
        self.fields['expert'].queryset = Expert.objects.filter(
            ~Q(id__in=Expert.objects.filter(competition__in=Ring.objects.filter(exhibition__in=Show.objects.filter(
            user__in=User.objects.filter(id=id_user)))).values('expert')))

        self.fields['expert'].widget.attrs.update({'class': 'form-control'})
        self.fields['ring'].widget.attrs.update({'class': 'form-control'})


class DelExpertForm(forms.ModelForm):
    """"Форма снятия эксперта с соревнования"""

    class Meta:
        model = Expert
        fields = "__all__"

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['ring'].queryset = Ring.objects.filter(exhibition__in=Show.objects.filter(
            user__in=User.objects.filter(id=id_user)), id__in=Expert.objects.all().values('ring'))

        self.fields['expert'].queryset = Expert.objects.filter(id__in=Expert.objects.filter(competition__in=Ring.objects.filter(exhibition__in=Show.objects.filter(
            user__in=User.objects.filter(id=id_user)))).values('expert'))

        self.fields['expert'].widget.attrs.update({'class': 'form-control'})
        self.fields['ring'].widget.attrs.update({'class': 'form-control'})


class RingForm(forms.ModelForm):
    """"Форма добавления соревнования"""
    ring = forms.IntegerField(label="Номер ринга")
    ex1 = forms.CharField(label="Упражнение №1")
    ex2 = forms.CharField(label="Упражнение №2")
    ex3 = forms.CharField(label="Упражнение №3")
    date = forms.DateField(label="Дата", widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Ring
        fields = "__all__"

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['show'].queryset = Show.objects.filter(user__in=User.objects.filter(id=id_user))
        self.fields['ring'].widget.attrs.update({'class': 'form-control'})
        self.fields['ex1'].widget.attrs.update({'class': 'form-control'})
        self.fields['ex2'].widget.attrs.update({'class': 'form-control'})
        self.fields['ex3'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['show'].widget.attrs.update({'class': 'form-control'})


class DogToCompForm(forms.ModelForm):
    """"Форма назначения собак на соревнования"""

    class Meta:
        model = Participation
        fields = ("ring", "participant")

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['ring'].queryset = Ring.objects.filter(exhibition__in=Show.objects.filter(user=User.objects.get(id=id_user)))
        #self.fields['dog'].queryset = Participant.objects.filter(
        #    id__in=DogRegistration.objects.filter(exhibition__in=Exhibition.objects.filter(user=User.objects.get(id=id_user))).values_list("dog"))

        self.fields['ring'].widget.attrs.update({'class': 'form-control'})
        self.fields['participant'].widget.attrs.update({'class': 'form-control'})


class DelDogFromCompForm(forms.ModelForm):
    """"Форма снятия собак с соревнования"""

    class Meta:
        model = Participation
        fields = "__all__"

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields["ring"].queryset = Ring.objects.filter(exhibition__in=Show.objects.filter(user=User.objects.get(id=id_user)),
                                                                       id__in = Participation.objects.all().values('ring'))
        self.fields['participant'].queryset = Participant.objects.filter(id__in=Participation.objects.all().values('participant'))

        self.fields['ring'].widget.attrs.update({'class': 'form-control'})
        self.fields['participant'].widget.attrs.update({'class': 'form-control'})


'''class DogRegForm(forms.ModelForm):
    """"Форма регистрации на выставку"""

    class Meta:
        model = DogRegistration
        fields = "__all__"

    def __init__(self, id_user, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['exhibition'].queryset = Exhibition.objects.filter(user__in=User.objects.filter(id=id_user))

        self.fields['exhibition'].widget.attrs.update({'class': 'form-control'})
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})
        self.fields['dog'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_paid'].widget.attrs.update({'class': 'form-control'})'''


'''class Query2Form(forms.ModelForm):
    """"Форма запроса 2"""

    class Meta:
        model = ClubParticipation
        fields = ('club',)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['club'].widget.attrs.update({'class': 'form-control'})'''


'''class Query3Form(forms.ModelForm):
    """"Форма запроса 3"""

    class Meta:
        #model = Dismissed
        model = Competition
        fields = ('exhibition',)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['exhibition'].widget.attrs.update({'class': 'form-control'})'''