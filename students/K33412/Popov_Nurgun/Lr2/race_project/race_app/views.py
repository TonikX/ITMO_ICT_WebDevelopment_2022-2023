from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from .forms import *
from race_app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.http import HttpResponse


def reg_page(request):
    if request.user.is_authenticated:
        return redirect('/races')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already used!')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    messages.success(request, 'Account was created')
                    return redirect('/login')
            else:
                messages.info(request, 'Passwords do not match')
                return redirect('/register')
        return render(request, 'registration.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/races')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/races')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect('/login')
        else:
            return render(request, 'login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required
def races(request):
    races = Race.objects.all()
    return render(request, 'races.html', {'races': races,})


@login_required(login_url='login')
def writeComment(request, pk):
    try:
        race = Race.objects.get(id=pk)
        racer = Racer.objects.get(id=request.user.racer.id)
        form = CommentForm(initial={'race': race, 'racer': racer})
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You left a comment for admin.')
                return redirect('/races')
        context = {'form': form}
        return render(request, 'comment.html', context)
    except Exception:
        messages.error(request, 'You must be a driver to leave a comment. Please, contact the admin.')
    return redirect('/races')


@login_required
def raceReg(request, pk):
    try:
        racer = Racer.objects.get(id=request.user.racer.id)
        race = Race.objects.get(id=pk)
        if Registration.objects.filter(racer=racer, race=race):
            messages.error(request, 'You have already been registered')
        else:
            if Car.objects.filter(racer=racer):
                car = Car.objects.get(racer=racer)
                Registration.objects.create(racer=racer, race=race, car=car)
                messages.success(request, 'You were registered')
            else:
                messages.error(request, 'You need a car to register')
    except Exception:
        messages.error(request, 'You must be a driver to register. Please, contact the admin.')
    return redirect('/races')


@login_required
def deleteReg(request, pk):
    try:
        racer = Racer.objects.get(id=request.user.racer.id)
        race = Race.objects.get(id=pk)
        reg = Registration.objects.get(racer=racer, race=race)
        if Registration.objects.filter(racer=racer, race=race):
            reg.delete()
            messages.success(request, 'Your registration was deleted')
        else:
            messages.error(request, 'You are not registered to the race')
    except Exception:
        messages.error(request, 'You must be a driver to register. Please, contact the admin.')
    return redirect('/races')


@login_required
def changeRace(request, pk):
    race = Race.objects.get(id=pk)
    form = RaceForm(instance=race)
    if request.method == "POST":
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect('/races')
    context = {'form': form}
    return render(request, 'race_edit.html', context)

@login_required
def changeReg(request, pk):
    try:
        race = Race.objects.get(id=pk)
        racer = Racer.objects.get(id=request.user.racer.id)
        reg = Registration.objects.get(race=race, racer=racer)
        form = RegForm(instance=reg)
        if request.method == "POST":
            form = RegForm(request.POST, instance=reg)
            if form.is_valid():
                form.save()
                return redirect('/races')
            else:
                return HttpResponse(form.errors)
        context = {'form': form}
        return render(request, 'race_form.html', context)
    except Exception:
        messages.error(request, 'You are either not registered or not a driver.')
    return redirect('/races')


@login_required
def results(request, pk):
    raceFormSet = inlineformset_factory(Race, Registration, fields=('racer', 'place'), extra=0)
    race = Race.objects.get(id=pk)
    regs = race.registration_set.count()
    registrations = race.registration_set.all()
    formset = raceFormSet(instance=race)
    if request.method == 'POST':
        formset = raceFormSet(request.POST, instance=race)
        if formset.is_valid():
            formset.save()
            return redirect('/races')
    context = {'formset': formset, 'regs': regs, 'registrations': registrations}
    return render(request, 'race_res.html', context)