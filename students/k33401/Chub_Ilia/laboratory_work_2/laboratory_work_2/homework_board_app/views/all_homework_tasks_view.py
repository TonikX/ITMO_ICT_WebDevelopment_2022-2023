from . import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import HomeworkModel, StudentModel


class AllHomeworkTasksView(LoginRequiredMixin, ListView):
    model = HomeworkModel
    template_name = "all_homework_tasks_template.html"

    def get_queryset(self):
        queryset = self.queryset

        try:
            student = StudentModel.objects.get(user__username=self.request.user.username)
            queryset = self.model.objects.filter(academic_discipline__students_uuids=student.id)
        except:
            pass

        return queryset
