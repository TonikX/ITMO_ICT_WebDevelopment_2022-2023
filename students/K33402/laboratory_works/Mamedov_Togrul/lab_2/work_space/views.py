from django.shortcuts import render, redirect

from work_space.forms import CreateTaskForm, AnswerTaskForm
from work_space.models import CreateTask, AnswerTask
from django.contrib.auth import get_user_model

User = get_user_model()


def staf_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_staff:
            return func(request, *args, **kwargs)
        return redirect('auth:signup')

    return check_user


@staf_only
def TaskCreate(request):
    if request.method == 'POST':
        form = CreateTaskForm(
            request.POST
        )
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = request.user
            instance.save()
            return redirect('work:task_list')
    else:
        form = CreateTaskForm()
    context = {
        'form': form,
    }
    return render(request, 'work_space/task_create.html', context=context)


def TaskList(request):
    tasks = CreateTask.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'work_space/task_list.html', context=context)


def AnswerCreate(request, pk):
    task = CreateTask.objects.get(pk=pk)
    if request.method == 'POST':
        form = AnswerTaskForm(
            request.POST
        )
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student = request.user
            instance.save()
            return redirect('work:task_list')
    else:
        form = AnswerTaskForm()
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'work_space/task_answer.html', context=context)


def AnswerList(request):
    answers = AnswerTask.objects.all()
    context = {
        'answers': answers,
    }
    return render(request, 'work_space/answer_list.html', context=context)


def AssessmentList(request):
    users = Users.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'work_space/assessment_list.html', context=context)
