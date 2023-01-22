from django.urls import resolve
from urllib.parse import urlparse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Count
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.views.generic import RedirectView
from operator import itemgetter

from .utils import get_city_by_iata_code
from . import models
from . import forms


class Home(TemplateView):
    template_name = 'home.html'


class Flights(LoginRequiredMixin, ListView):
    model = models.Flight
    template_name = 'flights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flights = self.model.objects.all()

        # Getting city names based on iata airport codes
        api_key = self.request.user.api_key
        api_url = self.request.user.api_url

        iata_codes = []
        for flight in flights:
            iata_codes.append(flight.source_airport_code)
            iata_codes.append(flight.destination_airport_code)

        cities_result = get_city_by_iata_code(
            api_key, api_url, iata_codes)
        iata_codes_dict, error = itemgetter(
            'iata_codes', 'error')(cities_result)

        context['error'] = error

        # Grouping by day
        context['dates'] = {}
        dates = flights.extra(
            select={'day': 'date( departure )'}
        ).values('day').annotate(available=Count('departure'))

        for date in dates:
            grouped_date = datetime.strptime(date['day'], '%Y-%m-%d').date()
            context['dates'][date['day']] = flights.filter(
                departure__contains=grouped_date)

            # Setting city names from dict
            for flight in context['dates'][date['day']]:
                for key, value in iata_codes_dict.items():
                    if flight.source_airport_code == key:
                        flight.source = value
                    if flight.destination_airport_code == key:
                        flight.destination = value

        return context


class SignUp(CreateView):
    model = models.User
    form_class = forms.UserSignUpForm
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse("home")

    # Auto login after signing up
    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class LogIn(LoginView):
    template_name = 'log_in.html'


class LogOut(RedirectView):
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogOut, self).get_redirect_url(*args, **kwargs)


class Profile(LoginRequiredMixin, TemplateView):
    model = models.User
    template_name = 'profile.html'

    login_url = 'log_in'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context.update({'user': self.request.user})
        flights = models.Flight.objects.filter(
            reservators__in=[self.request.user])
        context['flights'] = flights
        return context


@login_required
def toggle_reserve(request, pk):
    prev_url = urlparse(request.META.get('HTTP_REFERER')).path
    prev_url_name = resolve(prev_url).url_name

    model = models.Flight
    flight = model.objects.get(pk=pk)
    is_reserved = request.user in flight.reservators.filter(pk=request.user.pk)

    if not is_reserved:
        reservators_count = flight.reservators.count()
        max_reservations = flight.max_reservations

        if reservators_count >= max_reservations:
            messages.error(request, "All seats have already been reserved.")
            return redirect(reverse_lazy(prev_url_name))

        flight.reservators.add(request.user)
    else:
        flight.reservators.remove(request.user)

    return redirect(reverse_lazy(prev_url_name))
