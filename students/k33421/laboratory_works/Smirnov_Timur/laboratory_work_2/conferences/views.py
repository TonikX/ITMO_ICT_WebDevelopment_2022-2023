from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Theme, PlannedConference, RegisteredConference, Comment
from .forms import CommentForm, ConferenceRegisterForm


class CustomLoginView(LoginView):
    template_name = 'conferences/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('conferences')


class RegisterPage(FormView):
    template_name = 'conferences/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('conferences')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('conferences')
        return super(RegisterPage, self).get(*args, **kwargs)


class ConferencesList(ListView):
    model = PlannedConference
    template_name = 'conferences/conferences_list.html'
    context_object_name = 'conferences'


def conference_detail(request, pk):
    conference = PlannedConference.objects.get(pk=pk)
    registers = RegisteredConference.objects.filter(
        conference__pk=pk, results=True)
    comments = Comment.objects.filter(conference__pk=pk)
    initial = {'conference': conference, 'user': request.user}
    comment_form = CommentForm(initial=initial)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form. save()
        else:
            comment_form = c_form
    context = {'conference': conference,
               'comments': comments, 'comment_form': comment_form, 'registers': registers}
    return render(request, 'conferences/conference_detail.html', context)


class ThemesList(ListView):
    model = Theme
    template_name = 'conferences/themes_list.html'
    context_object_name = 'themes'


class ThemeDetail(DetailView):
    model = Theme
    context_object_name = 'theme'
    template_name = 'conferences/theme_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conferences"] = PlannedConference.objects.filter(
            themes__id=context['theme'].id)
        return context


@login_required
def conference_register_view(request, pk):
    conference = PlannedConference.objects.get(pk=pk)
    initial = {'conference': conference, 'user': request.user}
    form = ConferenceRegisterForm(initial=initial)
    if request.method == 'POST':
        c_form = ConferenceRegisterForm(request.POST)
        if c_form.is_valid():
            c_form. save()
            return redirect(f'/conference/{pk}')
        else:
            form = c_form
    context = {'conference': conference, 'form': form}
    return render(request, 'conferences/conference_register.html', context)


class RegisterList(LoginRequiredMixin, ListView):
    model = RegisteredConference
    template_name = 'conferences/registers.html'
    context_object_name = 'registers'


class DeleteRegisterView(LoginRequiredMixin, DeleteView):
    model = RegisteredConference
    context_object_name = 'register'
    success_url = reverse_lazy('my_registers')
