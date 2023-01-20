from django.http import Http404
from django.shortcuts import render 
from .models import Owner

def detail(request, owner_id):
    try: 
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p}) 