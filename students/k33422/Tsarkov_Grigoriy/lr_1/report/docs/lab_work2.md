# Лабораторная работа №2

## Задание
Реализовать сайт, используя фреймворк Django 3 и СУБД PostgreSQL *, в
соответствии с вариантом задания лабораторной работы.

Интерфейс описывает названия конференций, список тематик, место проведения,
период проведения, описание конференций, описание место проведения, условия участия.
Необходимо реализовать следующий функционал:

* Регистрация новых пользователей.

* Просмотр конференций и регистрацию авторов для выступлений

* Пользователь должен иметь возможность редактирования и удаления своих
регистраций.

* Написание отзывов к конференциям. При добавлении комментариев,
должны сохраняться даты конференции, текст комментария, рейтинг (1-10),
информация о комментаторе.

* Администратор должен иметь возможность указания результатов
выступления (рекомендован к публикации или нет) средствами Django-
admin.

* В клиентской части должна формироваться таблица, отображающая всех
участников по конференциям.

##Основные файлы:
`models.py`
```python
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings 


class Conference(models.Model):
    name = models.CharField("conference", max_length=50)
    topic = models.CharField("topic", blank=True, choices=[
        ("business", "business"),
        ("design", "design"),
        ("physics", "physics"),
    ], max_length=10)
    location = models.CharField("location", max_length=100)
    start_date = models.DateField("start date")
    end_date = models.DateField("end date")
    description = models.CharField("conference description", max_length=200)
    location_description = models.CharField("location description", max_length=200)
    terms = models.CharField("participation terms", max_length=1000)
    speaker = models.ManyToManyField(User, related_name="speaker")
    recommend = models.CharField("recommend", choices=[
        ("yes", "yes"),
        ("no", "no"),
    ], max_length=3)


    class Meta:
        verbose_name = "conference"
        verbose_name_plural = "conferences"

    def __str__(self):
        return f"{self.topic}: {self.name}"

    def written_by(self):
        return ", ".join([str(p) for p in self.speaker.all()])


class Comment(models.Model):
    name = models.ForeignKey(Conference, on_delete=models.CASCADE, verbose_name="conference")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="comment author")
    text = models.CharField("comment", max_length=100)
    rating = models.CharField("rating", choices =[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),

    ], max_length=2)


    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.author}: {self.text}"

```

`views.py`

```python
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
```

`forms.py`
```python
from django.forms import ModelForm, Textarea, HiddenInput
from .models import Comment


class PostComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text", "author", "rating"]

        labels = {
            "text": "Write your comment here",
        }

        widgets = {
            "conference": HiddenInput(),
            "text": Textarea(attrs={"cols": 70, "rows": 10}),
            "author": HiddenInput(),
        }
```

`urls.py`
```python
from django.urls import path

from .views import index, ConferenceView, ConferenceDetailView

urlpatterns = [
    path("", index, name="index"),
    path("conferences/", ConferenceView.as_view(), name="conferences"),
    path(
        "conferences/<slug:pk>/",
        ConferenceDetailView.as_view(),
        name="conference-detail",
    ),
]
```

