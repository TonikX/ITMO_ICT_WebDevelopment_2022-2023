# Create your views here.
from django.views.generic import TemplateView

from apps.homeworks.models import Homework


class HomeworksView(TemplateView):
    template_name = "homeworks/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # groups = self.request.user.groups.all()
        context['homeworks'] = Homework.objects.all()
        print(context['homeworks'])

        return context
