from django.urls import path, include
from django.views.generic import TemplateView

from .views import *
from . import views

urlpatterns = [
    path('conferences/', get_conferences, name='get_all_conferences'),
    path('conference/<int:id>/', get_conference_by_id, name='get_conference_by_id'),
    path("registration/", views.RegisterTemplateView.as_view(), name="register"),
    path("conference_apply/<int:id>/", views.conference_apply, name="conference_apply"),
    path("applies", views.user_applies, name='applies'),
    path("delete_apply/<int:id>", views.delete_apply, name='delete_apply'),
    path("create_comment/<int:id>", views.create_comment, name='create_comment'),
    path("mylogin/", MyLogin.as_view(), name='mylogin'),
    path('accounts/', include('django.contrib.auth.urls')),
]