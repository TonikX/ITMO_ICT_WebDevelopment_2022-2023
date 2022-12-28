from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'main.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')
    else:
        form = RegistrationForm()
    visual = {'form': form}
    return render(request, 'registration/signin.html', visual)


def user_login(request):
    global form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return HttpResponse('Неправильный логин или пароль!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')

def show_tours_not_auth(request):
    visual = {"tours": Tour.objects.all()}
    return render(request, 'tours_for_notauth.html', visual)


class CreateReservation(CreateView):
    form_class = CreateReservationForm
    model = Reservation
    template_name = 'reservation.html'
    context_object_name = 'reservation'
    success_url = '/profilereservations'

    def get_initial(self):
        initial = super(CreateReservation, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        initial['tour_id'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial


class UpdateReserveView(UpdateView):
    model = Reservation
    fields = ['start_date', 'end_date']
    template_name = 'upreservation.html'
    context_object_name = 'reservation'
    success_url = '/profilereservations'

    def get_initial(self):
        initial = super(UpdateReserveView, self).get_initial()
        initial = initial.copy()
        return initial


class DeleteReserveView(DeleteView):
    model = Reservation
    template_name = 'delreservation.html'
    context_object_name = 'reservation'
    success_url = '/profilereservations'


def reservedtourlist(request):
    visual = {"reservations": Reservation.objects.all()}
    return render(request, 'reservedtour.html', visual)


class listreservations(ListView):
    template_name = 'profilereservations.html'
    context_object_name = 'reservation_list'

    def get_queryset(self):
        self.user = self.request.user.pk
        return Reservation.objects.filter(username=self.user)


def commentlist(request):
    visual = {"comments": Feedback.objects.all()}
    return render(request, 'comments.html', visual)


def tourlist(request):
    visual = {"tours": Tour.objects.all()}
    for i in range(len(visual['tours'])):
        tour_id = visual['tours'][i]
        comments = Feedback.objects.filter(tour_id=tour_id)
        visual['tours'][i].comments = comments
    return render(request, 'tours.html', visual)


class CreateComment(CreateView):
    form_class = CreateCommentForm
    model = Feedback
    template_name = 'comment.html'
    context_object_name = 'comment'
    success_url = '/tours'

    def get_initial(self):
        initial = super(CreateComment, self).get_initial()
        initial = initial.copy()
        initial['username'] = self.request.user.pk
        initial['tour_id'] = get_object_or_404(Tour, pk=self.kwargs['pk'])
        return initial
