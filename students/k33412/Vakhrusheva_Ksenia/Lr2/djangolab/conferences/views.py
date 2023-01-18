from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def index_view(request):
	conferences = Conference.objects.all()
	return render(request, 'index.html', {'conferences': conferences})


def register_view(request):
	context = {}

	form = RegisterForm(request.POST or None)

	if form.is_valid():
		u = form.save(commit=False)
		u.set_password(request.POST.dict()['password'])
		form.save()
		return redirect('/login/')
	context['form'] = form
	return render(request, 'registration/register.html', context)


def conferences_view(request):
	conferences = Conference.objects.all()
	return render(request, 'conferences/list_view.html', {'conferences': conferences})


def conference_detail(request, pk):
	try:
		conference = Conference.objects.get(pk=pk)
		performances = Performance.objects.filter(conference=conference)
		comments = Comment.objects.filter(post=pk)
		context = {
			'conference': conference,
			'performances': performances,
			'comments': comments
		}

		form = CommentForm(request.POST or None)
		context['form'] = form

		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = Author.objects.get(pk=request.user.id)
			comment.post = conference
			comment.save()
	except Conference.DoesNotExist:
		raise Http404("Conference does not exist")
	return render(request, 'conferences/detail.html', context)


def conference_register(request, pk):
	context = {}
	if not request.user.is_authenticated:
		return redirect('/login/')
	form = ConferenceRegisterForm(request.POST or None)

	if form.is_valid():
		performance = form.save(commit=False)
		performance.author = Author.objects.get(pk=request.user.id)
		performance.conference = Conference.objects.get(pk=pk)
		performance.save()
		return redirect(f'/conferences/{pk}')
	context['form'] = form
	return render(request, 'conferences/register_performance.html', context)


def performance_view(request):
	if not request.user.is_authenticated:
		return redirect('/login/')

	conference = request.GET.get('conference', None)
	if conference:
		performances = Performance.objects.filter(author=request.user.id, conference=conference)
	else:
		performances = Performance.objects.filter(author=request.user.id)
	return render(request, 'performances/list_view.html', {'performances': performances})


def performance_edit(request, pk):
	context = {}
	if not request.user.is_authenticated:
		return redirect('/login/')

	instance = get_object_or_404(Performance, id=pk, author=request.user.id)
	form = ConferenceRegisterForm(request.POST or None, instance=instance)

	if form.is_valid():
		form.save()
		return redirect('/performances/')
	context['form'] = form
	context['pk'] = pk
	return render(request, 'performances/edit_performance.html', context)


def performance_delete(request, pk):
	if not request.user.is_authenticated:
		return redirect('/login/')

	instance = get_object_or_404(Performance, id=pk, author=request.user.id)
	print(instance)
	instance.delete()
	return redirect('/performances/')
