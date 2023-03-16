from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from .forms import MakeComment
from .models import *


def home_page(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST.get("first_name", 'NaN')
        team = request.POST.get("team", 'NaN')
        patronymic = request.POST.get("patronymic", 'NaN')
        experience_years = request.POST.get("experience_years", 'NaN')
        last_name = request.POST.get("last_name", 'NaN')

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "reg_django.html", {
                "message": "passwords do not match"
            })

        try:
            if experience_years=='':
                experience_years=0
            racer = UserRacer.objects.create_user(username, email, password, patronymic=patronymic,
                                                team=team,
                                                experience_years=experience_years)
            racer.first_name = first_name
            racer.last_name = last_name
            racer.save()
        except IntegrityError:
            return render(request, "reg_django.html", {
                "message": "username is taken"
            })
        login(request, racer)
        return redirect(reverse("races"))
    else:
        return render(request, "reg_django.html")


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('races'))
        else:
            error_text = 'invalid credentials'
    return render(request, 'login.html', locals())


class RegList(ListView):
    model = Registration
    template_name = 'reg_list.html'


class UserList(ListView):
    model = UserRacer
    template_name = 'user_list.html'


class RaceList(ListView):
    model = Race
    template_name = 'race_list.html'


def get_race(request, id_race: int):
    try:
        race = Race.objects.get(pk=id_race)
    except Race.DoesNotExist:
        raise Http404("Race does not exist.")
    return render(request, 'race.html', {'race': race})


class RegRaceCreate(CreateView):
  model = Registration
  template_name = 'reg_form.html'
  fields = ['num_race_reg', 'num_user_reg']
  success_url = '/reg_list/'


class RegRaceDelete(DeleteView):
    model = Registration
    template_name = 'reg_delete.html'
    success_url = '/reg_list/'


class RegRaceUpdate(UpdateView):
    model = Registration
    fields = ['num_race_reg', 'num_user_reg']
    template_name = 'reg_update.html'
    success_url = '/reg_list/'


def comment(request):
    data = {}
    form = MakeComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'comment.html', data)


def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'comments_list.html', list_comments)