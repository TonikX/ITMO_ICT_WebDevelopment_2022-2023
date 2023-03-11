from django.urls import path

from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    # path('warriors/', WarriorAPIView.as_view()),
    path('warriors/', WarriorListAPIView.as_view()),
    path('warriors/<int:pk>/', WarriorObjectAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    path('skill/', SkillAPIView.as_view()),
    path('skill/create/', SkillAPIView.as_view()),
]
