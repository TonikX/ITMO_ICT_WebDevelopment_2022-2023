from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostComment
from .models import Conference, Comment
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "index.html")


class ConferenceView(generic.ListView):
    model = Conference
    context_object_name = "conferences"
    queryset = Conference.objects.all()
    template_name = "conferences.html"


class ConferenceDetailView(FormMixin, generic.DetailView):
    model = Conference
    template_name = "conference-detail.html"
    form_class = PostComment

    def get_context_data(self, **kwargs):
        context = super(ConferenceDetailView, self).get_context_data(**kwargs)
        context["form"] = PostComment(
            initial={"name": self.object, "author": self.request.user}
        )
        context["comments"] = Comment.objects.filter(name=self.get_object()).all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(
            reverse("conference-detail", args=(self.object.pk,))
        )