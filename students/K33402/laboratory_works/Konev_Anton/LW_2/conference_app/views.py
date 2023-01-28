from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.generic import TemplateView

from conference_app.forms import *
from conference_app.models import *


class ConferencesList(TemplateView):
    template_name = "conferences.html"

    """
    
    Добавляем в контекст данные для отображения
    
    """

    def get_context_data(self, **kwargs):
        return super().get_context_data(conferences=Conference.objects.all(), **kwargs)


class ConferenceView(TemplateView):
    template_name = "conference.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(conference=Conference.objects.get(id=kwargs["id"]),
                                        regestrations=ConfRegistration.objects.filter(conference_id=kwargs["id"]),
                                        comments=ConfComment.objects.filter(conference_id=kwargs['id']),
                                        reg_form=RegForm(prefix="reg"),
                                        comment_form=AddComment(prefix="com"),
                                        **kwargs)

    """
    
    Принимаем форм запросы и пытаемся распарсить форм дату
    
    """

    def post(self, request: HttpRequest, **kwargs):
        user: Optional[AbstractUser] = request.user
        form_data = RegForm(request.POST, prefix="reg")
        if form_data.is_valid():
            if user is not None and user.is_authenticated:
                res = ConfRegistration(user_id=user.pk, conference_id=kwargs["id"], text=form_data.cleaned_data["text"])
                res.save()
            return redirect("/registrations/")
        form_data = AddComment(request.POST, prefix="com")
        if not form_data.is_valid():
            raise ValidationError("")
        if user is not None and user.is_authenticated:
            res = ConfComment(user_id=user.pk, conference_id=kwargs["id"],  text=form_data.cleaned_data["comment"],
                              rate=form_data.cleaned_data["rate"])
            res.save()
        return redirect(f"/conferences/{kwargs['id']}")


class RegistrationsView(TemplateView):
    template_name = "registrations.html"

    def get_context_data(self, **kwargs):
        user: Optional[AbstractUser] = self.request.user
        return super().get_context_data(regestrations=ConfRegistration.objects.filter(user_id=user.id),
                                        **kwargs)


class RegistrationView(TemplateView):
    template_name = "registration.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(regestration=ConfRegistration.objects.get(id=kwargs['id']),
                                        del_form=DeleteRegForm(prefix='del'),
                                        ch_form=ChangeRegForm(prefix='ch'),
                                        **kwargs)

    def post(self, request: HttpRequest, **kwargs):
        user: Optional[AbstractUser] = request.user
        form_data = DeleteRegForm(request.POST, prefix="del")
        if form_data.is_valid():
            if user is not None and user.is_authenticated and form_data['is_delete']:
                res = ConfRegistration.objects.get(user_id=user.pk, id=kwargs['id'])
                res.delete()
            return redirect("/registrations/")
        form_data = ChangeRegForm(request.POST, prefix="ch")
        if not form_data.is_valid():
            raise ValidationError("")
        if user is not None and user.is_authenticated:
            res = ConfRegistration.objects.get(user_id=user.pk, id=kwargs['id'])
            res.text = form_data.cleaned_data['new_text']
            res.save()
        return redirect(f"/registration/{kwargs['id']}")
