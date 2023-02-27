from django.views.generic import FormView
from ..forms import SubmitHomeworkTaskForm
from ..models import SubmitHomeworkTaskModel, HomeworkModel
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import StudentModel

class SubmitHomeworkTaskView(LoginRequiredMixin, FormView):
    form_class = SubmitHomeworkTaskForm
    template_name = 'submit_homework_task_template.html'
    success_url = 'homework_tasks/all'

    def form_valid(self, form):
        user = self.request.user
        student_model = StudentModel.objects.get(user=user)
        uuid = form.cleaned_data['homework_uuid']
        answer = form.cleaned_data['answer']
        homework_model = HomeworkModel.objects.get(uuid=uuid)
        submitHomeworkTaskModel = SubmitHomeworkTaskModel(
            homework_uuid=homework_model,
            answer=answer,
            student_id=student_model
        )

        submitHomeworkTaskModel.save()

        return super(SubmitHomeworkTaskView, self).form_valid(form)
