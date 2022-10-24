from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from .forms import MakeComment
from .models import *

# Create your views here.

def main_page(request):
    return render(request, 'main.html')

class RegisterUser(CreateView):
    model = UserRacer
    fields = ['username',
              'first_name', 'last_name', 'fathername',
              'team_name',
              'user_descr',
              'car_descr',
              'experience',
              'type_user']
    success_url = '/user_list/'
    template_name = "user_register.html"

class UserList(ListView):
    # list view
    model = UserRacer
    template_name = 'user_list.html'

class RaceList(ListView):
    # list view
    model = Race
    template_name = 'race_list.html'

def get_race(request, id_race: int):
    # https:..race/1/
    try:
        race = Race.objects.get(pk=id_race)
    except Race.DoesNotExist:
        raise Http404("Race does not exist.")
    return render(request, 'race.html', {'race': race})


class RegRaceList(ListView):
    # list view
    model = RegistrationRace
    template_name = 'reg_race_list.html'

class RegRaceCreate(CreateView):
  model = RegistrationRace
  template_name = 'reg_race_form.html'
  fields = ['num_race_reg', 'num_user_reg']
  success_url = '/reg_race/list/'

class RegRaceDelete(DeleteView):
    model = RegistrationRace
    template_name = 'reg_race_delete.html'
    success_url = '/reg_race/list/'

class RegRaceUpdate(UpdateView):
    model = RegistrationRace
    fields = ['num_race_reg', 'num_user_reg']
    template_name = 'reg_race_update.html'
    success_url = '/reg_race/list/'

def make_comment(request):
    data = {}
    form = MakeComment(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'comment_create.html', data)

def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'comments_list.html', list_comments)