from django.shortcuts import render #метод, который запускаеи хтмл страницу и передает в нее параметры
from django.http import Http404 # метод обработки ситуации, когда нет необходимых записей в бд
from project_first_app.models import Owner # таблица из модели данных
# Create your views here.
def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': owner})
