from django.shortcuts import render
from .models import User, Homework, TaskCompletion, CLASSES_LIST
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SolutionForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class StartPageView(TemplateView):
    def get(self, request):
        return render(request, 'board_app/start_page.html')


class NotificationView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'

    def get(self, request):
        context = {}
        context["edit_link"] = f"/accounts/{self.request.user.id}/update/"
        return render(request, 'board_app/account_created.html', context)


class StudentUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'

    model = User
    template_name = 'board_app/user_update.html'
    fields = ["surname", "name", "patronymic", "birthday", "group"]
    success_url = '/profile/'


class ProfilePageView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'

    def get(self, request):
        context = {}
        context["edit_link"] = f"/accounts/{self.request.user.id}/update/"
        context["user"] = self.request.user
        return render(request, 'board_app/profile_page.html', context)


class AllTasks(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'

    def get(self, request):
        user = self.request.user
        if (user.group, user.group) not in CLASSES_LIST:
            return redirect(f"/accounts/{request.user.id}/update/")

        context = {}
        context['user'] = user
        context['task_list'] = Homework.objects.filter(group=user.group)

        answers = TaskCompletion.objects.filter(student_id=user.id)
        context['answers'] = answers

        context['hw_ids'] = []
        for answer in answers:
            context['hw_ids'].append(answer.homework_id)

        return render(request, 'board_app/all_tasks.html', context)


@login_required
def solution_create(request):
    task_id = request.GET.get('task_id')
    task = Homework.objects.get(pk=task_id)
    context = {}
    context["user"] = request.user

    if request.method == 'POST':
        form = SolutionForm(task, request.user, task.subject, task.task_text, request.POST)

        if form.is_valid():
            form.save()
            return redirect('/profile/all_tasks/')

    else:
        form = SolutionForm(task, request.user, task.subject, task.task_text)
        context["form"] = form
        context["task"] = Homework.objects.get(pk=task_id)

    return render(request, 'board_app/solution.html', context)


@login_required
def subject_select(request):
    user = request.user
    if (user.group, user.group) not in CLASSES_LIST:
        return redirect(f"/accounts/{request.user.id}/update/")

    context = {}
    context['user'] = user
    hw_list = Homework.objects.filter(group=user.group)

    context['subjects'] = []
    for hw in hw_list:
        if hw.subject not in context['subjects']:
            context['subjects'].append(hw.subject)

    return render(request, 'board_app/subject_select.html', context)


@login_required
def class_marks(request):
    context = {}
    user = request.user
    context['user'] = user

    class_students = User.objects.filter(group=user.group)
    class_students = class_students.order_by('surname', 'name', 'patronymic')
    context['class_students'] = class_students

    subject = request.GET.get('subject')
    context['subject'] = subject

    context['marks'] = []
    context['average'] = []
    for student in class_students:
        tasks_done = TaskCompletion.objects.filter(student_id=student.id, subject=subject)
        marks = ''
        marks_sum = 0
        n = 0
        for index, task in enumerate(tasks_done):
            marks += task.mark
            if index != len(tasks_done) - 1:
                marks += ', '
            if task.mark in '2345':
                marks_sum += int(task.mark)
                n += 1
        context['marks'].append(marks)
        if n != 0:
            context['average'].append(round((marks_sum / n), 2))
        else:
            context['average'].append('')

    return render(request, 'board_app/class_marks.html', context)