from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth import login, authenticate

from .forms import *


def conf_list(request):
    confs = Conference.objects.all()
    return render(request, 'TheConference/index.html', context={'confs': confs})


def conf_registration(request, name):
    try:
        conf = get_object_or_404(Conference, name__iexact=name)
        perfs = Performance.objects.filter(conference=conf)
        comments = Comment.objects.filter(post=conf)
        context = {
            'conf': conf,
            'perfs': perfs,
            'comments': comments
        }

        form = CommentForm(request.POST or None)
        context['form'] = form

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Participant.objects.get(pk=request.user.id)
            comment.post = conf
            comment.save()

    except Conference.DoesNotExist:
        raise Http404("Conference does not exist")
    return render(request, 'TheConference/registration.html', context)


def registration(request, name):
    conf = get_object_or_404(Conference, name__iexact=name)
    context = {'conf': conf}
    if not request.user.is_authenticated:
        return redirect('/login')
    form = ConferenceRegisterForm(request.POST or None)

    if form.is_valid():
        performance = form.save(commit=False)
        performance.author = Participant.objects.get(id=request.user.id)
        performance.conference = Conference.objects.get(name=name)
        performance.save()
        return redirect(f'/conf/{name}')
    context['form'] = form
    return render(request, 'TheConference/conf_registration.html', context)


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
    perfs = Performance.objects.filter(author=request.user)
    return render(request, 'TheConference/account.html', context={'perfs': perfs})


def performance_edit(request, pk):
    context = {}
    instance = get_object_or_404(Performance, id=pk, author=request.user.id)
    form = ConferenceRegisterForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('/account')
    context['form'] = form
    context['pk'] = pk
    return render(request, 'TheConference/edit_performance.html', context)


def performance_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')

    instance = get_object_or_404(Performance, id=pk, author=request.user.id)
    print(instance)
    instance.delete()
    return redirect('/account')


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'TheConference/tags_list.html', context={'tags': tags})


def tags_detail(request, title):
    tag = get_object_or_404(Tag, title__iexact=title)
    return render(request, 'TheConference/tags_detail.html', context={'tag': tag})
