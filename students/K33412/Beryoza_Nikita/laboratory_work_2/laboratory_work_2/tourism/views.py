from django.shortcuts import render, redirect
from django.http import Http404 
from .forms import SignupForm, ReserveForm, CommentForm
from .models import Tourist, Tour, Reservation, Comment


def view_table(request):
    ind = {}
    ind['tours_by_country'] = {i: Tour.objects.filter(country=i) for i in list(dict.fromkeys([x.country for x in Tour.objects.all()]))}
    return render(request, 'view_table.html',  ind)


def sign_up(request):
    ind = {}

    form = SignupForm(request.POST or None)

    if form.is_valid():
        x = form.save(commit=False)
        password = request.POST.dict().get('password')
        x.set_password(password or 'password')
        form.save()
        return redirect('/login/')
    ind['form'] = form
    return render(request, 'signup.html', ind)


def view_tours(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    ind = {}
    ind['tours'] = Tour.objects.all().order_by('country')
    return render(request, 'view_tours.html', ind)


def view_tour(request, pk):
    ind = {}
    try:
        ind['tour'] = Tour.objects.get(pk=pk)
        ind['comments'] = Comment.objects.filter(tour=pk)
        form = CommentForm(request.POST or None)
        ind['form'] = form

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Tourist.objects.get(pk=request.user.id)
            comment.tour = ind['tour']
            comment.save()
    except Tour.DoesNotExist:
        raise Http404("Такой тур не найден")
    return render(request, 'view_tour.html', ind)


def reserve_tour(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login/')
    form = ReserveForm(request.POST or None)
    reservation = form.save(commit=False)
    reservation.tour = Tour.objects.get(pk=pk)
    reservation.tourist = Tourist.objects.get(pk=request.user.id)
    reservation.save()
    return redirect(f'/reservations/')



def view_reservations(request):
    ind = {}
    if not request.user.is_authenticated:
        return redirect('/login/')
    ind['reservations'] = Reservation.objects.filter(tourist=request.user.id)
    return render(request, 'view_reservations.html', ind)


def cancel_reservation(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    reservation = Reservation.objects.get(pk=pk, tourist=request.user.id)
    reservation.delete()
    return redirect('/reservations/')



    

    


