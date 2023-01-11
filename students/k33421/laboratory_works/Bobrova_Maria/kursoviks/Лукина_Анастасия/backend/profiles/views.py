from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Profile
from .forms import ProfileForm
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class ProfileView(LoginRequiredMixin, DetailView):
    """Вывод профиля пользователя"""
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля"""
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('view_profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Профиль был обновлён')
        return super().form_valid(form)


class PublicUserInfo(LoginRequiredMixin, DetailView):
    """Публичный профиль пользователя"""
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/public_user_info.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Profile, id=pk)
        return obj

    def get_queryset(self):
        profile = self.get_object()
        user = User.objects.get(id=profile.id)
        qs = user.twits.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context

