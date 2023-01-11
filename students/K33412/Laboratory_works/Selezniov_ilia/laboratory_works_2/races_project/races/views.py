from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory


@unauthenticated_user
def regPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='driver')
            user.groups.add(group)
            Driver.objects.create(user=user)

            messages.success(request, 'Account was created')
            return redirect('driver_cr')

    context = {'form': form}
    return render(request, 'reg_user.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/races')
        else:
            messages.info(request, 'Username or password is not correct')

    context = {}
    return render(request, 'login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['driver'])
def home(request):
    regs = request.user.driver.registration_set.all()
    driver = Driver.objects.get(id=request.user.driver.id)
    # cars = request.user.driver.car_set.all()
    cars = Car.objects.filter(driver=Driver.objects.get(id=request.user.driver.id))

    return render(request, 'home.html', {'regs': regs, 'cars': cars, 'driver': driver})


@login_required(login_url='login')
def drivers(request, pk_test):
    drivers = []
    cars = []

    registrations = Registration.objects.filter(race=pk_test).order_by('place')
    for reg in registrations:
        drivers.append(reg.driver)
        cars.append(reg.car)
    print(drivers)

    return render(request, 'drivers.html', {'drivers': drivers, 'cars': cars, 'regs': registrations})


@login_required(login_url='login')
def races(request):
    context = Race.objects.all()
    return render(request, 'races.html', {'races': context})


@login_required(login_url='login')
def createReg(request):
    driver = Driver.objects.get(id=request.user.driver.id)
    car = Car.objects.get(driver=driver)

    # if Registration.objects.get(driver=driver, race=race):
    # 	messages.error(request, 'You are already regestered to this race')
    # 	return redirect('/home')

    if car.car_model == None:
        messages.error(request, 'You need a car to register')
        return redirect('/home')

    form = RegForm(initial={'driver': driver, 'car': car})
    if request.method == "POST":
        print(request.POST)
        form = RegForm(request.POST)
        race_test = Race.objects.get(id=request.POST.get('race'))
        if Registration.objects.filter(driver=driver, race=race_test):
            messages.error(request, 'You are already regestered to this race')
            return redirect('/home')
        if form.is_valid():
            reg = form.save()
            return redirect('/home')
            messages.success(request, 'You were registered')

    context = {'form': form}
    return render(request, 'reg_form.html', context)


@login_required(login_url='login')
def raceReg(request, pk):
    driver = Driver.objects.get(id=request.user.driver.id)
    race = Race.objects.get(id=pk)
    if Registration.objects.filter(driver=driver, race=race):
        messages.error(request, 'You are already regestered to this race')
    else:
        car = Car.objects.get(driver=driver)
        if car.car_model != None:
            Registration.objects.create(driver=driver, race=race, car=car)
            messages.success(request, 'You were registered')
        else:
            messages.error(request, 'You need a car to register')

    return redirect('/races')


@login_required(login_url='login')
def changeReg(request, pk):
    reg = Registration.objects.get(id=pk)
    form = RegForm(instance=reg)
    if request.method == "POST":
        form = RegForm(request.POST, instance=reg)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context = {'form': form}
    return render(request, 'reg_form.html', context)


def regDriver(request):
    driver = Driver.objects.get(name=None)
    form = CreateDriverForm(instance=driver)
    if request.method == "POST":
        form = CreateDriverForm(request.POST, instance=driver)
        if form.is_valid():
            driver = form.save()
            Car.objects.create(driver=driver)
            messages.success(request, 'Driver was created')
            return redirect('login')

    context = {'form': form}
    return render(request, 'reg_driver.html', context)


@login_required(login_url='login')
def deleteReg(request, pk):
    reg = Registration.objects.get(id=pk)
    context = {'reg': reg}
    if request.method == "POST":
        reg.delete()
        return redirect('/home')

    return render(request, 'del_reg.html', context)


@login_required(login_url='login')
def createCar(request):
    driver = Driver.objects.get(id=request.user.driver.id)
    car = Car.objects.get(driver=driver)
    form = CarForm(instance=car)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('/home')

    context = {'form': form}

    return render(request, 'carForm.html', context)


@login_required(login_url='login')
def changeCar(request, pk):
    car = Car.objects.get(id=pk)
    form = CarForm(instance=car)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form': form}
    return render(request, 'carForm.html', context)


@login_required(login_url='login')
def writeComment(request, pk):
    race = Race.objects.get(id=pk)
    driver = Driver.objects.get(id=request.user.driver.id)
    form = CommentForm(initial={'race': race, 'driver': driver})

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You left a comment for admin. Wait for an answer')
            return redirect('/races')

    context = {'form': form}
    return render(request, 'comment_form.html', context)


@login_required(login_url='login')
def createRace(request):
    form = RaceForm()
    if request.method == "POST":
        form = RaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Race was created')
            return redirect('/races')

    context = {'form': form}
    return render(request, 'race_form.html', context)


@login_required(login_url='login')
def changeRace(request, pk):
    race = Race.objects.get(id=pk)
    form = RaceForm(instance=race)

    if request.method == "POST":
        form = RaceForm(request.POST, instance=race)
        if form.is_valid():
            form.save()
            return redirect('/races')

    context = {'form': form}
    return render(request, 'race_form.html', context)


@login_required(login_url='login')
def results(request, pk):
    raceFormSet = inlineformset_factory(Race, Registration, fields=('driver', 'place'), extra=0)
    race = Race.objects.get(id=pk)
    regs = race.registration_set.count()
    formset = raceFormSet(instance=race)
    if request.method == 'POST':
        formset = raceFormSet(request.POST, instance=race)
        if formset.is_valid():
            formset.save()
            return redirect('/races')

    context = {'formset': formset, 'regs': regs}
    return render(request, 'race_res.html', context)


@login_required(login_url='login')
def comments(request, pk):
    race = Race.objects.get(id=pk)
    comments = race.comment_set.all()
    context = {'comments': comments}

    return render(request, 'comments.html', context)


@login_required(login_url='login')
def delRace(request, pk):
    race = Race.objects.get(id=pk)
    context = {'race': race}
    if request.method == "POST":
        race.delete()
        return redirect('/races')

    return render(request, 'del_race.html', context)
