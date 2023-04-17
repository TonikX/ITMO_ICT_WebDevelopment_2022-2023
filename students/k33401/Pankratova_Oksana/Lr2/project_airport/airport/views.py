from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import Ticket, Flight, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import CreationForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect


def main_page(request):
    return render(request, 'main.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = '/account/login/'
    template_name = 'account/signup.html'


class tickets(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'my_tickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        return Ticket.objects.filter(passenger_id_id=self.request.user.id)


def flight(request, pk):
    flight_obj = get_object_or_404(Flight, id=pk)
    comments = Comment.objects.filter(flight_id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.passenger = request.user
            form.flight = flight_obj
            form.save()
            return redirect('flight', pk)
    else:
        form = CommentForm()

    return render(request, 'flight.html', {'context': flight_obj, 'comments': comments, 'form': form})


class tickets_change(UpdateView):
    model = Ticket
    template_name = 'ticket_change.html'
    fields = ['food', 'clas']
    success_url = '/tickets/'


class tickets_delete(DeleteView):
    model = Ticket
    success_url = '/tickets/'
    template_name = 'ticket_delete.html'
