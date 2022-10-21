from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import Http404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import *

from .forms import  RegistrUser
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def main_page(request):
    n = ["Foo", "Bar"]
    return render(request, 'main_page.html', context={'names': n})



def registr_user(request):
    data = {}
    form = RegistrUser(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError(('This email already registerd'))
        else:
            form.save()
        messages.success(request, "Registration successful.")
       # return redirect("")
   # data['form'] = form
    return render (request, 'reg_user.html', context={"register_form":form})

def Create_User(request):
    return True


def get_conferences(request):
    conferences = Сonference.objects.all()
    return render(request, 'conferences.html', context={'conferences': conferences})


def get_conference_by_id(request, id):
    conference = Сonference.objects.get(id=id)
    users_conf = User_confirence.objects.filter(conference_id=id)
    coments = Comment.objects.filter(conference_id=id)
    return render(request, 'conference.html', context={'conference': conference, 'users_conf': users_conf,
                                                       'coments': coments})


