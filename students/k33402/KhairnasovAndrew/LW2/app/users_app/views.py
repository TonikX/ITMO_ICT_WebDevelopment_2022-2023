from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users_app.forms import RegisterForm, MyAuthenticationForm


class RegisterTemplateView(CreateView):
    form_class = RegisterForm
    success_url = '/login'
    template_name = 'register.html'


class MyLoginView(LoginView):
    template_name = "login.html"
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/hotels/"
