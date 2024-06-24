from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .form import *
from .models import *

def hellow(request):
    return render(request, "welcome.html")

@csrf_exempt
def user_login(request):


    if request.method == 'POST':
        if request.POST.get('username') == None:
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('http://127.0.0.1:8000/home/'+str(user.id))

            else:
                return render(request, 'login.html', {'error_msg': "Incorrect username or password"})
    else:
        return render(request, 'login.html')


def user_register(request):

    registered = False
    if request.method == 'POST':
        create_user_form = User_form(data=request.POST)
        if create_user_form.is_valid():
            user = create_user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('http://127.0.0.1:8000/home/'+str(user.id))
        else:
            print(create_user_form.errors)
    else:
        create_user_form = User_form()

    return render(request, 'register.html', {'create_user_form': create_user_form, 'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def list_air_travel(request, user_id):
    id = user_id
    air_travel = Air_travel.objects.order_by('-date')[:5]
    return render(request, 'home.html', {'list': air_travel, 'user': id})

@login_required
def list_passenger(request, travel_id):
    air_travel = get_object_or_404(Air_travel, pk=travel_id)
    list_user = []

    passengers = list(Passenger.objects.filter(Air_travel=travel_id).all())
    print(passengers)
    for i in passengers:
        passenger_in_travel = User.objects.get(id=i.passenger.id)
        list_user.append(passenger_in_travel)
    print(list_user)
    return render(request, 'passenger.html', {'list': list_user,'travel': air_travel})

@login_required
def list_my_air_travel(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    list_travels = []

    passengers = list(Passenger.objects.filter(passenger=user.id).all())
    print(passengers)
    for i in passengers:
        my_travel = Air_travel.objects.get(id=i.Air_travel.id)
        list_travels.append(my_travel)
    print(list_travels)
    return render(request, 'travels.html', {'list': list_travels, 'user': user})

@login_required
def create_passenger(request,travel_id,user_id):
    user = get_object_or_404(User, pk=user_id)
    air_travel = get_object_or_404(Air_travel, pk=travel_id)
    new_passenger = Passenger()
    new_passenger.passenger = user
    new_passenger.Air_travel = air_travel
    new_passenger.save()

    return HttpResponseRedirect('http://127.0.0.1:8000/passenger/'+str(air_travel.id))

@login_required
def list_comment(request, travel_id, user_id):
    id = user_id
    air_travel = get_object_or_404(Air_travel, pk=travel_id)
    comment = Comment.objects.filter(air_travel=travel_id).all()
    return render(request, 'reviews.html', {'list': comment, 'user': id, 'travel_name':air_travel})

@login_required
def edit_passenger(request,travel_id,user_id):
    user = get_object_or_404(User, pk=user_id)
    air_travel = get_object_or_404(Air_travel, pk=travel_id)
    
    passenger = Passenger.objects.filter(Air_travel=travel_id,passenger = user.id).first()
    passenger.delete()

    return HttpResponseRedirect('http://127.0.0.1:8000/my_travels/'+str(user.id))

@login_required
def create_comment(request,user_id,travel_id):
    user = get_object_or_404(User, pk=user_id)
    air_travel = get_object_or_404(Air_travel, pk=travel_id)
    new_comment = Comment()
    new_comment.text = request.POST.get('text')
    new_comment.air_travel = air_travel
    new_comment.rating = request.POST.get('rating')
    new_comment.creator = user
    new_comment.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/comment/'+str(user.id)+'/'+str(air_travel.id))
