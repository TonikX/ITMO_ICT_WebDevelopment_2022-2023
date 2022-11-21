from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from datetime import date

from .forms import *
from hotel_first_app.models import Registration


class ReserveDeleteView(DeleteView):
    model = Registration
    template_name = 'delete_reserve.html'
    success_url = '/hotels/hotels/'


class UpdateReserveView(UpdateView):
    form_class = UpdateReserveForm
    template_name = 'update_reserve.html'
    context_object_name = 'reg'

    def get_queryset(self):
        self.success_url = f"/account/{self.kwargs['id_user']}"
        return Registration.objects.filter(pk=self.kwargs['pk'])


class AccountUserView(UpdateView):
    form_class = AccountForm
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super(AccountUserView, self).get_context_data(**kwargs)
        cur_date = date.today()
        month_ago_date = cur_date.replace(month=(cur_date.month - 1))
        context['month_registrations'] = Registration.objects.filter(check_out__gte=month_ago_date)
        context['taken_registrations'] = Registration.objects.filter(status_reg="T")
        context['booked_registrations'] = Registration.objects.filter(status_reg="B")
        context['guest_registrations'] = Registration.objects.filter(id_guest=self.kwargs['pk'])
        context['guests'] = User.objects.filter(is_superuser=False)
        return context

    def get_queryset(self):
        self.success_url = f"/account/{self.kwargs['pk']}"
        return User.objects.filter(pk=self.kwargs['pk'])


def error(request):
    return render(request, 'error.html')


class RegView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'index.html'
    success_url = 'hotels'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        context = {'username': ""}
        if form.is_valid():
            form.save()
            context['username'] = form.cleaned_data.get('username')
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('hotels')
        return render(request, 'error.html')


class LogInView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('hotels')


class LogOutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')
