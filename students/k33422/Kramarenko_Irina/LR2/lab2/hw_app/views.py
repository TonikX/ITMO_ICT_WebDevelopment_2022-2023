from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .forms import UploadHW, RegUser
from .models import TeacherHomework, StudentHomework


def reg_user(request):
    data = {}
    form = RegUser(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'reg_user.html', data)


def upload_hw(request):
    data = {}
    form = UploadHW(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, 'upload_hw.html', data)


class PrintHWs(ListView):
    model = TeacherHomework
    template_name = "list_hws.html"

    # def get_queryset(self):
    #     self.study_class = get_object_or_404(Student, name=self.kwargs['study_class'])
    #     return TeacherHomework.objects.filter(study_class=self.study_class)


class PrintGrades(ListView):
    model = StudentHomework
    template_name = "list_grades.html"