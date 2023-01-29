from django.urls import path
from .views import WarriorAPIView, ProfessionCreateView, SkillAPIView, SkillCreateView, WarriorDetailedAPIView

app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),

    path('warriors-detailed/', WarriorDetailedAPIView.as_view()),
]
