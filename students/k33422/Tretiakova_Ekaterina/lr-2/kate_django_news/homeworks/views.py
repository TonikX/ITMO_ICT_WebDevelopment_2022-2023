from django.http import HttpResponse, HttpResponseRedirect

from homeworks.models import Subject, Homework, User, Grade


def index(request):
    homeworks_text = ''
    homeworks = Homework.objects.all()
    for homework in homeworks:
        homeworks_text += 'Домашняя работа #{0} :  {1}'.format(homework.id, homework.task_description)
    return HttpResponse(homeworks_text)


def create_homework(request):
    if request.method == "POST":
        homework = Homework()
        homework.task_description = request.POST.get("task_description")
        homework.date_start = request.POST.get("date_start")
        homework.date_end = request.POST.get("date_end")
        homework.is_work_submitted = request.POST.get("is_work_submitted")
        homework.save()
    return HttpResponseRedirect("/")


def create_user(request):
    if request.method == "POST":
        user = User()
        user.user_name = request.POST.get("user_name")
        user.save()
    return HttpResponseRedirect("/")


def create_grade(request, homework_id):
    if request.method == "POST":
        grade = Grade()
        grade.grade = request.POST.get("grade")
        grade.homework = Homework.objects.all().get(homework_id)
        grade.save()
    return HttpResponseRedirect("/")


def create_subject(request, user_id):
    if request.method == "POST":
        subject = Subject()
        subject.subject_name = request.POST.get("subject_name")
        subject.user = User.objects.all().get(user_id)
        subject.save()
    return HttpResponseRedirect("/")
