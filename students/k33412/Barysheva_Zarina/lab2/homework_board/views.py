from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import DoneTaskForm, UserForm, AssignmentForm

from homework_board.models import *

@login_required()
def get_report_card(request):
        tasks = Assignment.objects.all()
        students = User.objects.filter(is_teacher=0)
        report_card = {}

        for student in students:
            student_marks_dict = {}
            for task in tasks:
                try:
                    student_task = DoneTask.objects.get(assignment_id=task.pk, student_id=student.pk)
                    student_mark = student_task.mark
                except DoneTask.DoesNotExist:
                    student_mark = 0
                student_marks_dict[task.pk] = student_mark
            report_card[str(student.surname) + ' ' + str(student.name) + ' (' + str(student.pk) + ')'] = student_marks_dict
        return render(request, 'report_card.html', {'report_card': report_card, 'tasks': tasks})

@login_required()
def get_all_tasks(request):
     check = request.user.is_teacher
     tasks_list = Assignment.objects.all()
     return render(request, 'assignments_list.html', {'tasks_list': tasks_list, 'check': check})

@login_required()
def send_new_donetask(request, task_id):
    if request.method == 'POST':
        form = DoneTaskForm(request.POST)
        if form.is_valid():
            new_done_task = form.save(commit=False)
            new_done_task.student_id = request.user
            new_done_task.assignment_id = Assignment.objects.get(pk=task_id)
            new_done_task.save()
        return HttpResponseRedirect('/report_card/')
    else:
        form = DoneTaskForm()

    return render(request, 'done_task.html', {'form': form, 'task_id': task_id})

            
def create_new_user(request):          
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
        return HttpResponseRedirect('/report_card/')
    else:
        form = UserForm()

    return render(request, 'reg_student.html', {'form': form})

@login_required()
def create_new_task(request): 
    check = request.user.is_teacher
    if check:         
        if request.method == 'POST':
            form = AssignmentForm(request.POST)
            if form.is_valid():
                new_assignment = form.save(commit=False)
                new_assignment.teacher_id = request.user
                new_assignment.save()
            return HttpResponseRedirect('/assignments/')
        else:
            form = AssignmentForm()
    else:
        return HttpResponseRedirect('/report_card/')
    return render(request, 'create_assignment.html', {'form': form})


@login_required()
def exit(request):
    logout(request)

@login_required()
def get_task(request, task_id):
     task = Assignment.objects.get(pk=task_id)
     return render(request, 'assignment.html', {'task': task})