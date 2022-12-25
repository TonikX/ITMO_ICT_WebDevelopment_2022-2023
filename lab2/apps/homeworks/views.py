# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from apps.homeworks.models import Homework


class ListHomeworksView(TemplateView, LoginRequiredMixin):
    template_name = "homeworks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groups = list(self.request.user.groups_studying.all())
        context['homeworks'] = Homework.objects.filter(group__in=groups)
        return context
