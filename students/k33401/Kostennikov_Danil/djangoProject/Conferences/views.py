from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import *

from .forms import RegistrUser, LoginUser, ConferenceApply
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def main_page(request):
    n = ["Foo", "Bar"]
    return render(request, 'main_page.html', context={'names': n})

class Reg_user(CreateView):
    model = User
    fields = [
        'email',
        'first_name',
        'last_name',
        'password'
    ]
    template_name = "reg_user.html"
    success_url = reverse_lazy('get_all_conferences')

def conference_apply(request, id):
    form = ConferenceApply(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email,password=password).first()
        if not user:
            message = "Wrong email or password, or user is not registered"
            return render(request, 'conference_apply.html', context={"form": form, "message": message})

        conference = Сonference.objects.get(id=id)
        user_conf = User_confirence.objects.filter(user_id=user,conference_id=conference).exists()
        if user_conf:
            message = "You have alreade applied"
            return render(request, 'conference_apply.html', context={"form": form, "message": message})
        User_confirence.objects.create(user_id=user, conference_id=conference)
        message = "Success"
        return render(request, 'conference_apply.html', context={"form": form, "message": message})
    return render(request, 'conference_apply.html', context={"form": form})

def get_conferences(request):
    conferences = Сonference.objects.all()
    return render(request, 'conferences.html', context={'conferences': conferences})


def get_conference_by_id(request, id):
    conference = Сonference.objects.get(id=id)
    users_conf = User_confirence.objects.filter(conference_id=id)
    coments = Comment.objects.filter(conference_id=id)
    return render(request, 'conference.html', context={'conference': conference, 'users_conf': users_conf,
                                                       'coments': coments})



