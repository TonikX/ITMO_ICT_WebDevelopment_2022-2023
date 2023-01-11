from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from backend.profiles.models import Profile
from backend.app.models import Exhibition, Competition, Expert, ExpertCompetition, CompParticipation, Dog, Result, DogRegistration, Dismissed, DogOwner, ClubParticipation
from backend.app.forms import ExhibitionForm, SetExpertForm, DelExpertForm, CompetitionForm, DogToCompForm, DelDogFromCompForm, DogRegForm, Query2Form, Query3Form



class AllExhibition(ListView):
    """Выводим все выставки"""
    model = Exhibition
    queryset = Exhibition.objects.all()
    context_object_name = 'exhibition'
    template_name = 'app/exhibition.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ExhibitionForm()
        return context


class ViewAllExhibition(LoginRequiredMixin, AllExhibition):
    """Вывод выставок пользователя"""
    model = Exhibition
    template_name = 'app/exhibition.html'
    context_object_name = 'exhibition'

    def get_queryset(self):
        qs = Exhibition.objects.all()
        return qs


def exhibition_info(request):
    """Let it be"""
    context = {}
    conf = Exhibition.objects.all()
    org = Profile.objects.all()
    context["exhibition"] = conf
    context["orgs"] = Profile.objects.all()

    return render(request, "exhibition.html", context)


def exhibition_add(request):
    context = {}
    conf = Exhibition.objects.all()
    context["exhibition"] = conf

    form = ExhibitionForm(request.POST, request.FILES)
    context['form'] = form
    if form.is_valid():
        object = form.save(commit=False)
        pk = request.POST.get("pk")

        object.user = request.user
        object.save()
        return redirect('/exhibition_info/')
    return render(request, "exhibition_add.html", context)


def exhibition_my(request):
    """Let it be"""
    context = {}
    conf = Exhibition.objects.filter(user=request.user)
    context["exhibition"] = conf
    context["orgs"] = Profile.objects.filter(id=request.user.id)

    return render(request, "exhibition.html", context)

from django.db.models import F


def one_exhibition_info(request, pk):
    """Let it be"""
    context = {}
    conf = Exhibition.objects.get(id=pk)
    comp = Competition.objects.all()
    res = Result.objects.all()
    res = Result.objects.annotate(result=F('score1') + F('score2')+F('score3')).order_by('-result')
    #print(queryset)

    context["ex"] = conf
    context["orgs"] = Profile.objects.filter(id=request.user.id)
    context["competitions"] = comp
    context["results"] = res
    context["count"] = CompParticipation.objects.filter(competition__in=Competition.objects.filter(exhibition=conf)).count()
    context["breeds"] = CompParticipation.objects.filter(competition__in=Competition.objects.filter(exhibition=conf))

    return render(request, "one_exhibition_info.html", context)


def experts_output(request):
    """Let it be"""
    context = {}
    conf = Expert.objects.all()
    context["experts"] = conf
    return render(request, "experts_output.html", context)


def set_experts(request):
    context = {}
    conf = Exhibition.objects.filter(user=request.user)
    context["exhibition"] = conf
    context["button"] = "эксперта"
    form = SetExpertForm(request.user.id, request.POST)
    form2 = DelExpertForm(request.user.id, request.POST)
    context['form'] = form
    context['form2'] = form2

    if form.is_valid():
        data = form.cleaned_data.get("competition")
        object = form.save(commit=False)
        object.save()
        return redirect('/set_experts/')

    if form2.is_valid():
        print(2)
        competition = form2.cleaned_data.get("competition")
        expert = form2.cleaned_data.get("expert")
        u = ExpertCompetition.objects.get(competition=competition, expert=expert).delete()
        return redirect('/set_experts/')
    return render(request, "set_experts.html", context)


def competition_add(request):
    context = {}
    form = CompetitionForm(request.user.id, request.POST)
    context['button'] = "Добавить соревнование"
    context['form'] = form
    if form.is_valid():
        comps = Competition.objects.filter(exhibition=Exhibition.objects.get(title=form.cleaned_data.get("exhibition"))).values_list('ring', flat=True)
        ex = Exhibition.objects.get(title=form.cleaned_data.get("exhibition"))
        ex_id = ex.id
        if form.cleaned_data.get("ring") in comps:
             context["message"] = "На это соревнование уже назначен данный ринг"
             return render(request, "competition_add.html", context)
        if form.cleaned_data.get("date") < ex.date_start or form.cleaned_data.get("date") > ex.date_finish:
            context["message"] = "Выберите подходящие данной выставке даты"
            context["date_start"] = ex.date_start
            context["date_finish"] = ex.date_finish
            return render(request, "competition_add.html", context)
        object = form.save(commit=False)
        object.save()
        return redirect('/one_exhibition_info/'+str(ex_id))
    return render(request, "competition_add.html", context)


def dog_to_comp(request):
    context = {}
    context["button"] = "собаку"
    form = DogToCompForm(request.user.id, request.POST)
    form2 = DelDogFromCompForm(request.user.id, request.POST)
    context['form'] = form
    context['form2'] = form2

    if request.POST.get('f1') == 'f1':
        if form.is_valid():
            name = form.cleaned_data.get("dog")
            comp = form.cleaned_data.get("competition")
            part = CompParticipation.objects.filter(dog=name, competition=comp)
            if part:
                context["message"] = "Выбранная собака уже записана на указанное соревнование"
                return render(request, "set_experts.html", context)
            object = form.save(commit=False)
            object.save()
            return redirect('/dog_to_comp/')
    if request.POST.get('f2') == 'f2':
        if form2.is_valid():
            name = form2.cleaned_data.get("dog")
            comp = form2.cleaned_data.get("competition")
            part = CompParticipation.objects.filter(dog=name, competition=comp)
            if not part:
                context["message"] = "Выбранная собака не была записана на указанное соревнование"
                return render(request, "set_experts.html", context)
            u = CompParticipation.objects.get(competition=comp, dog=name).delete()
            p = Dismissed.objects.create(dog=name, competition = comp)
            return redirect('/dog_to_comp/')
    return render(request, "set_experts.html", context)


def dog_reg(request):
    context = {}
    form = DogRegForm(request.user.id, request.POST)
    context['button'] = "Зарегистрировать собаку"
    context['form'] = form
    if form.is_valid():
        ex = form.cleaned_data.get("exhibition")
        dog = form.cleaned_data.get("dog")
        reg = DogRegistration.objects.filter(exhibition=ex, dog=dog)
        if reg:
            context["message"] = "Выбранная собака уже была зарегистрирована на эту выставку"
            return render(request, "competition_add.html", context)
        object = form.save(commit=False)
        object.save()
        return redirect('/dog_reg/')
    return render(request, "competition_add.html", context)


def query(request, query_number):
    context = {}
    if query_number == 1:
        if request.POST.get('f1') == 'f1':
            dog_name = request.POST.get("dog")
            owner_name = request.POST.get("owner").split(" ")
            if DogOwner.objects.filter(name=owner_name[0], surname=owner_name[1], dog__in=Dog.objects.filter(name=dog_name)):
                answer = Competition.objects.filter(id__in=CompParticipation.objects.filter(dog__in=Dog.objects.filter(name=dog_name)).values_list("competition"))
                context["answer"] = owner_name[0] + " " + owner_name[1] + " c собакой " + dog_name + " выступает на ринге №"
                context["ring"] = answer[0]
                return render(request, "query1.html", context)
            context["message"] = "Такого хозяина нет в базе данных или у указанного хозяина нет указанной собаки"

        return render(request, "query1.html", context)
    if query_number == 2:
        form = Query2Form(request.POST)
        context["form"] = form
        if form.is_valid():
            club = form.cleaned_data.get("club")
            print(club.id)
            temp = ClubParticipation.objects.filter(club=club)
            context["dogs"] = temp

        return render(request, "query2.html", context)
    if query_number == 3:
        form = Query3Form(request.POST)
        context["form"] = form
        if form.is_valid():
            # competition = form.cleaned_data.get("competition")
            exhibition = form.cleaned_data.get("exhibition")
            context["count"] = Dismissed.objects.filter(competition__in=Competition.objects.filter(exhibition=exhibition)).count()
            context["dogs"] = Dismissed.objects.filter(competition__in=Competition.objects.filter(exhibition=exhibition))

        return render(request, "query3.html", context)
    if query_number == 4:
        if request.POST.get('f1') == 'f1':
            breed = request.POST.get("breed")
            exp = ExpertCompetition.objects.all() # Все назначенные эксперты
            comp_dogs = CompParticipation.objects.all()
            context["experts"] = []
            for i in comp_dogs:
                if i.dog.breed == breed:
                    for j in exp:
                        if i.competition == j.competition:
                            context["experts"].append(str(j.expert.surname) + " " + str(j.expert.name))

        dogs = Dog.objects.all()
        context["dogs"] = dogs
        return render(request, "query4.html", context)
    if query_number == 5:
        if request.POST.get('f1') == 'f1':
            breed = request.POST.get("breed")
            ex = request.POST.get("exhibition")
            comp_dog = CompParticipation.objects.filter(competition__in=Competition.objects.filter(exhibition__in=Exhibition.objects.filter(title=ex)))
            count = 0
            context["dogs_name"] = []
            for i in comp_dog:
                if i.dog.breed == breed:
                    context["dogs_name"].append(i.dog.name)
                    count += 1
            context["count"] = count
        dogs = Dog.objects.all()
        context["dogs"] = dogs
        context["exs"] = Exhibition.objects.all()
        return render(request, "query5.html", context)