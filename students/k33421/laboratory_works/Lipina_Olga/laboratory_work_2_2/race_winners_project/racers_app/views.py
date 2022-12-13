from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.db import IntegrityError


from .forms import MakeComment
from .models import *

# Create your views here.

def main_page(request):
    return render(request, 'main.html')




def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST.get("first_name", 'NaN')
        team_name = request.POST.get("team_name", 'NaN')
        fathername = request.POST.get("fathername", 'NaN')
        experience = request.POST.get("experience", 'NaN')
        last_name = request.POST.get("last_name", 'NaN')

        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register_django.html", {
                "message": "passwords do not match"
            })

        try:
            if experience=='':
                experience=0
            student = Racer.objects.create_user(username, email, password, fathername=fathername,
                                                team_name=team_name,
                                                experience=experience)
            student.first_name = first_name
            student.last_name = last_name
            student.save()
            # homeworks = Homework.objects.all()
            # for homework in homeworks:
            #     assignment = Assignment(student=student, homework=homework)
            #     assignment.save()
        except IntegrityError:
            return render(request, "register_django.html", {
                "message": "username already taken"
            })
        login(request, student)
        return redirect(reverse("races"))
    else:
        return render(request, "register_django.html")



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
    return render(request, 'login_django.html', locals())

# @login_required
# def log_out(request):
#     logout(request)
#     return redirect(reverse('logout'))
#



class RegisterUser(CreateView):
    model = Racer
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
    model = Racer
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

def reg_race_list_vies(request):
    context = {
        'reg_races': RegistrationRace.objects.filter(num_user_reg=request.user)
    }
    print(request.user)
    print('--', context)
    return render(request, 'reg_race_list.html', context)


class RegRaceCreate(CreateView):
  model = RegistrationRace
  template_name = 'reg_race_form.html'
  fields = ['num_race_reg']
  success_url = '/reg_race/list/'
  def form_valid(self, form):
    form.instance.num_user_reg = self.request.user
    return super().form_valid(form)

class RegRaceDelete(DeleteView):
    model = RegistrationRace
    template_name = 'reg_race_delete.html'
    success_url = '/reg_race/list/'

class RegRaceUpdate(UpdateView):
    model = RegistrationRace
    fields = ['num_race_reg']
    template_name = 'reg_race_update.html'
    success_url = '/reg_race/list/'

@login_required
def make_comment(request):
    data = {}
    form = MakeComment(request.POST or None)
    user_racer = None
    if request.user.is_authenticated:
        user_racer = request.user
        # request.POST['username'] = username
    else:
        return None
    if form.is_valid():
        bet = form.save(commit=False)  # the bet isn't saved just yet
        bet.username = user_racer  # you add the user here
        bet.save()
    data['form'] = form
    return render(request, 'comment_create.html', data)

def all_comments(request):
    list_comments = {"object_list": Comment.objects.all()}
    return render(request, 'comments_list.html', list_comments)