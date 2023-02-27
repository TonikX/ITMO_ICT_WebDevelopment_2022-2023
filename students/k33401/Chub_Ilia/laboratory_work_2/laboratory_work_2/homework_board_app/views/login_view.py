from . import *
from django.contrib.auth.views import LoginView


class LoginBaseView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_template.html'
