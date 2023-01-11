

from rest_framework import permissions
from drf_yasg.views import get_schema_view

from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    # path('warriors/', WarriorAPIView.as_view()),
    path('warriors/', WarriorListAPIView.as_view()),  # list of warriors

    path('warriors/create/', WarriorCreateAPIView.as_view()),  # create warrior

    # list warriors with skills and professions
    path('warriors/<int:pk>/', WarriorRetrieveAPIView.as_view()),

    # update / destroy warrior by id
    path('warriors/edit/<int:pk>/', WarriorRetrieveUpdateDestroyAPIView.as_view()),

    path('warriors/show_professions', WarriorProfessionAPIView.as_view()),  # list warriors with professions
    path('warriors/show_skills', WarriorSkillAPIView.as_view()),  # list warriors with skills

    path('professions/', ProfessionAPIView.as_view()),  # list of professions

    # path('profession/create/', ProfessionCreateView.as_view()),
    path('profession/create/', ProfessionCreateAPIView.as_view()),  # create profession

    path('skills/', SkillAPIView.as_view()),  # list of skills
    path('skill/create/', SkillCreateView.as_view()),  # create skill
]