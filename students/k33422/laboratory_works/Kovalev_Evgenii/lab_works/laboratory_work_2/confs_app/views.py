from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView, CreateView, DeleteView, DetailView

from django.shortcuts import render, redirect

from .models import *
from .forms import *


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):

        print(request.POST)
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            print('valid')
            user = form.get_user()
            login(request, user)
            return redirect('conflist_route')
        else:
            print('not valid')
            messages.error(request, 'Указаны неверные данные')

        return redirect('login_route')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('conflist_route')
        else:
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_route')


class SignupView(FormView):
    form_class = UserRegisterForm
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, 'Успешная регистрация')
            return redirect('login_route')
        else:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request, 'Пользователь с таким именем уже зарегистрирован')
            else:
                messages.error(request, 'Ошибка регистрации')

        return redirect('signup_route')


class ConferenceView(LoginRequiredMixin, ListView):
    model = Conference
    template_name = 'conference_list.html'
    context_object_name = 'conferences'

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset


@login_required
def join_or_leave_conf_view(request, conf_pk, user_pk):
    conf = Conference.objects.get(pk=conf_pk)
    user = User.objects.get(pk=user_pk)

    if user in conf.members.all():
        conf.members.remove(user)
    else:
        conf.members.add(user)

    return redirect('conflist_route')


@login_required
def user_confs_view(request, username):
    all_confs = Conference.objects.all()
    user_confs = []

    for conf in all_confs:
        if request.user in conf.members.all():
            user_confs.append(conf)

    return render(request, 'user_confs.html', {'user_confs': user_confs})


class DetailConfView(LoginRequiredMixin, DetailView):
    model = Conference
    template_name = 'detail_conference.html'
    context_object_name = 'conf'
    pk_url_kwarg = 'conf_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conf_pk = self.kwargs['conf_pk']
        comments = Comment.objects.filter(conference__pk=conf_pk).order_by('-created')
        context['comments'] = comments
        return context


@login_required
def comment_view(request, conf_pk):
    user_obj = User.objects.get(pk=request.user.pk)
    conference = Conference.objects.get(pk=conf_pk)

    comment_text = request.POST['comment_text']

    if str(comment_text).isspace():
        messages.error(request, 'Комментарий не может быть пустым')
    else:
        comment_obj = Comment.objects.create(
            author=user_obj,
            conference=conference,
            rating=0,
            text=comment_text
        )

    return redirect('detail_conf_route', conf_pk=conf_pk)


@login_required
def remove_comment_view(request, conf_pk, comment_pk):
    comment_obj = Comment.objects.get(pk=comment_pk).delete()
    return redirect('detail_conf_route', conf_pk=conf_pk)


@login_required
def conf_members_view(request, conf_pk):
    conference = Conference.objects.get(pk=conf_pk)
    members = conference.members.all()
    context = {
        'members': members,
        'conf': conference
    }
    return render(request, 'conf_members.html', context)
