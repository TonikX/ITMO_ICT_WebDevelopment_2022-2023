from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate

from .forms import *


def conf_list(request):
    confs = Conference.objects.all()
    return render(request, 'TheConference/index.html', context={'confs': confs})


def conf_registration(request, name):
    conf = get_object_or_404(Conference, name__iexact=name)
    return render(request, 'TheConference/registration.html', context={'conf': conf})


def user_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = form.save()
            # user = authenticate(username=username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'TheConference/registration/user_registration.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'TheConference/registration/login.html')


def account(request):
    user = Participant.objects.all()
    return render(request, 'TheConference/account.html', context={'user': user})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'TheConference/tags_list.html', context={'tags': tags})


def tags_detail(request, title):
    tag = get_object_or_404(Tag, title__iexact=title)
    return render(request, 'TheConference/tags_detail.html', context={'tag': tag})
