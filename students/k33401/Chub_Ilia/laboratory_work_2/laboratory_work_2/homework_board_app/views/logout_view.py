from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class LogoutBaseView(LoginRequiredMixin, LogoutView):
    next_page = 'login'
