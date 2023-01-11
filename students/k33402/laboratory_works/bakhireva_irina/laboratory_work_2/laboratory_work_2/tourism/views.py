from django.shortcuts import render, redirect
from django.http import Http404 
from .forms import SignupForm, ReserveForm, CommentForm
from .models import Tourist, Tour, Reservation, Comment


def view_table(request):
    ctx = {}
    ctx['tours_by_country'] = {c: Tour.objects.filter(country=c) for c in list(dict.fromkeys([x.country for x in Tour.objects.all()]))}
    return render(request, 'view_table.html',  ctx)


def sign_up(request):
    ctx = {}

    form = SignupForm(request.POST or None)

    if form.is_valid():
        u = form.save(commit=False)
        password = request.POST.dict().get('password')
        u.set_password(password or 'password')
        form.save()
        return redirect('/login/')
    ctx['form'] = form
    return render(request, 'signup.html', ctx)


def view_tours(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    ctx = {}
    ctx['tours'] = Tour.objects.all().order_by('country')
    return render(request, 'view_tours.html', ctx)


def view_tour(request, pk):
    ctx = {}
    try:
        ctx['tour'] = Tour.objects.get(pk=pk)
        ctx['comments'] = Comment.objects.filter(tour=pk)
        form = CommentForm(request.POST or None)
        ctx['form'] = form

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Tourist.objects.get(pk=request.user.id)
            comment.tour = ctx['tour']
            comment.save()
    except Tour.DoesNotExist:
        raise Http404("Такой тур не найден")
    return render(request, 'view_tour.html', ctx)


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
    ctx = {}
    if not request.user.is_authenticated:
        return redirect('/login/')
    ctx['reservations'] = Reservation.objects.filter(tourist=request.user.id)
    return render(request, 'view_reservations.html', ctx)


def cancel_reservation(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    reservation = Reservation.objects.get(pk=pk, tourist=request.user.id)
    reservation.delete()
    return redirect('/reservations/')



    

    


