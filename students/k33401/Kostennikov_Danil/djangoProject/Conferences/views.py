from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import *

from .forms import RegistrUser, LoginUser, ConferenceApply, CreateComment
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


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

def applies(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email, password=password)
        if not user:
            return False
        return redirect(f"/applies/{email}")
    except:
        return render(request, "applies.html")

def user_applies(request, email):
    user = User.objects.get(email=email)
    user_conf = User_confirence.objects.filter(user_id=user)
    return render(request, 'user_applies.html', context={"user_conf": user_conf})

def delete_apply(request, email,id):
    try:
        User_confirence.objects.get(id=id).delete()
        return redirect(f"/applies/{email}")
    except:
        return redirect(f"/applies/{email}")

def create_comment(request,id):
    form = CreateComment(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.filter(email=email,password=password).first()
        if not user:
            message = "Wrong email or password, or user is not registered"
            return render(request, 'create_comment.html', context={"form": form, "message": message})

        conference = Сonference.objects.get(id=id)
        comment = form.cleaned_data['comment']
        rank = form.cleaned_data['rank']

        Comment.objects.create(user_id=user,conference_id=conference, comment=comment,rank=rank)
        return redirect(f"/conference/{id}")

    return render(request, 'create_comment.html', context={"form": form})
