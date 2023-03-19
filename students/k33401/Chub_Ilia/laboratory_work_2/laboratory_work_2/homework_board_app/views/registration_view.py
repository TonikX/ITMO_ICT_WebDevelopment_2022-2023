from ..forms import RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class RegistrationView(SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Success"
    template_name = "registration_template.html"
