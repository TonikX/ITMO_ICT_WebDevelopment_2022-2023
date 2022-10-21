from django.shortcuts import render
from django.http import Http404
from .models import *


# Create your views here.

def main_page(request):
    n = ["Foo", "Bar"]
    return render(request, 'main_page.html', context={'names': n})


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
