from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import *
from .forms import RegistrUser, CreateComment, MyAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.


class Reg_user(CreateView):
    model = User
    fields = [
        'username',
        'first_name',
        'last_name',
        'password'
    ]
    template_name = "reg_user.html"
    success_url = reverse_lazy('get_all_conferences')


class RegisterTemplateView(CreateView):
    form_class = RegistrUser
    template_name = "reg_user.html"
    success_url = reverse_lazy('get_all_conferences')

class MyLogin(LoginView):
    template_name = "mylogin.html"
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('get_all_conferences')




def get_conferences(request):
    conferences = Сonference.objects.all()
    return render(request, 'conferences.html', context={'conferences': conferences})


def get_conference_by_id(request, id):
    conference = Сonference.objects.get(id=id)
    users_conf = User_confirence.objects.filter(conference_id=id)
    coments = Comment.objects.filter(conference_id=id)
    return render(request, 'conference.html', context={'conference': conference, 'users_conf': users_conf,
                                                       'coments': coments})

def conference_apply(request, id):
    message = ""
    try:
        username = request.user.username
        #password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if not user or not username:
            message = "Wrong username or password, or user is not registered"
            return False
           # return render(request, 'conference_apply.html', context={"form": form, "message": message})

        conference = Сonference.objects.get(id=id)
        user_conf = User_confirence.objects.filter(user_id=user,conference_id=conference).exists()
        if user_conf:
            message = "You have alreade applied"
            #return render(request, 'conference_apply.html', context={"form": form, "message": message})
            return False
        User_confirence.objects.create(user_id=user, conference_id=conference)
        message = "Success"
        return redirect(f"/applies")
        #return render(request, 'conference_apply.html', context={"form": form, "message": message})
    except:
        return render(request, "applies.html")
    #return render(request, 'conference_apply.html', context={"form": form})

def user_applies(request):
    username = request.user.username
    user = User.objects.get(username=username)
    user_conf = User_confirence.objects.filter(user_id=user)
    return render(request, 'user_applies.html', context={"user_conf": user_conf})

def delete_apply(request,id):
    try:
        User_confirence.objects.get(id=id).delete()
        return redirect(f"/applies")
    except:
        return redirect(f"/applies")

def create_comment(request,id):
    username = request.user.username
    user = User.objects.get(username=username)

    if not user or not username:
        message = "Wrong email or password, or user is not registered"
        return redirect(f"/mylogin")
    form = CreateComment(request.POST)

    if form.is_valid():
        conference = Сonference.objects.get(id=id)
        comment = form.cleaned_data['comment']
        rank = form.cleaned_data['rank']

        Comment.objects.create(user_id=user,conference_id=conference, comment=comment,rank=rank)
        return redirect(f"/conference/{id}")


    return render(request, 'create_comment.html', context={"form": form})



