from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseRedirect


def homepage(request):
    return render(request, 'main/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords dont match')
            return redirect('register')

    else:
        return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User doesnt exists')
            return redirect('login')
    else:
        return render(request, 'main/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


def conferences(request):
    con = Conference.objects.all()
    p = Paginator(con, 1)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'main/card.html', {'conferences': page})


def conf(request, pk):
    c = Conference.objects.get(id=pk)
    comments = Comment.objects.filter(conference=c)
    return render(request, 'main/conf.html', {'conference': c, 'comments': comments})


@login_required
def reg_to_conf(request, pk):
    obj = get_object_or_404(Conference, id=pk)
    user = request.user
    themes = obj.themes.split(',')
    if request.method == "POST":
        form = RegisterToConferenceForm(request.POST)
        if Registration.objects.filter(user=user, conference=obj).exists():
            messages.info(request, 'You already joined')
        else:
            if form['theme'].value() in themes:
                reg = form.save(commit=False)
                reg.user = user
                reg.conference = obj
                reg.save()
                return redirect('/conferences')
            else:
                messages.info(request, 'You must type a theme that exist')

    else:
        form = RegisterToConferenceForm()
    return render(request, 'main/reg_to_conf.html', {'form': form, 'conference': obj})


@login_required
def profile(request):
    user = request.user
    regs = Registration.objects.all().order_by('-create_date')
    return render(request, 'main/profile.html', {'registrations': regs, 'user': user})


@login_required
def delete(request, pk):
    obj = get_object_or_404(Registration, id=pk)
    obj.delete()
    return redirect('/profile')


@login_required
def edit(request, pk):
    obj = get_object_or_404(Registration, id=pk)
    user = request.user
    if request.method == "POST":
        form = RegisterToConferenceForm(request.POST or None, instance=obj)
        reg = form.save(commit=False)
        reg.save()
        return redirect('/conferences')
    else:
        form = RegisterToConferenceForm()
    return render(request, 'main/reg_to_conf.html', {'form': form, 'conference': obj})


@login_required
def add_comment(request, pk):
    obj = get_object_or_404(Conference, id=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form['text'].value():
            if form['rate'].value():
                if form.is_valid():
                    com = form.save(commit=False)
                    com.user = user
                    com.conference = obj
                    com.save()
                    return HttpResponseRedirect('/conferences')
            else:
                messages.info(request, 'You must rate the room!')
        else:
            messages.info(request, 'You should type something!')
    else:
        form = CommentForm()
    return render(request, 'main/comment.html', {'form': form})


@login_required
def make_table(request):
    table = Registration.objects.values('user__username', 'conference__title').order_by('conference__title')
    return render(request, 'main/table.html', {'table': table})


def search(request):
    searched = request.POST['searched']
    obj = Conference.objects.filter(title=searched)
    return render(request, 'main/includes/search.html', {'searched': searched, 'conferences': obj})