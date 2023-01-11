from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users_app.forms import RegisterForm, MyAuthenticationForm

"""
шаблонная вьюшка, которая будет регистрировать юзера
"""


class RegisterTemplateView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


"""
шаблонная вьюшка, которая будет логинить нас в системе
"""


class MyLoginView(LoginView):
    template_name = "login.html"
    form_class = MyAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/conferences"
