# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from apps.homeworks.models import Homework
from apps.submissions.forms import SubmissionCreationForm
from apps.submissions.models import Submission


class ListSubmissionsView(TemplateView, LoginRequiredMixin):
    template_name = "submissions/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        is_student = self.request.user.groups_studying.exists()
        is_teacher = self.request.user.groups_teaching.exists()
        context['is_teacher'] = is_teacher
        context['is_student'] = is_student

        submissions_teacher = None
        submissions_student = None
        if is_teacher:
            groups_teaching = self.request.user.groups_teaching.all()
            submissions_teacher = Submission.objects.filter(
                homework__group__in=groups_teaching
            )
        if is_student:
            submissions_student = Submission.objects.filter(
                student=self.request.user
            )
        context['submissions_teacher'] = submissions_teacher
        context['submissions_student'] = submissions_student
        return context


def send_submission(request, hw_id, *args, **kwargs):
    homework = get_object_or_404(Homework, pk=hw_id)
    if request.method == 'POST':
        form = SubmissionCreationForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.homework = homework
            submission.student = request.user
            submission.save()
            return redirect('submissions')
    else:
        form = SubmissionCreationForm()
    return render(request, 'submissions/create.html', {'form': form, 'homework': homework})
