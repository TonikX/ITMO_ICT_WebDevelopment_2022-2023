from django.views.generic import ListView
from ..models import EducationalJournalModel, StudentModel


class EducationalJournalModel(ListView):
    model = EducationalJournalModel
    template_name = "all_educational_journal_template.html"

    def get_queryset(self):
        queryset = self.queryset

        try:
            student = StudentModel.objects.get(user__username=self.request.user.username)
            queryset = self.model.objects.filter(submit_homework_task_uuid__student_id=student.id)
        except:
            pass

        return queryset
