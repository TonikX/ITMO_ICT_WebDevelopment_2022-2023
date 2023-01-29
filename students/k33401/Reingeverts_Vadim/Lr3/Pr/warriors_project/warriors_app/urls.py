from django.urls import path
from .views import WarriorAPIView, ProfessionCreateView, SkillAPIView, SkillCreateView, WarriorAndProfessionAPIView, WarriorAndSkillAPIView, WarriorDetailsAPIView

app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),

    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),

    path('warriors-profession/', WarriorAndProfessionAPIView.as_view()),
    path('warriors-skill/', WarriorAndSkillAPIView.as_view()),
    path('warrior/<int:pk>', WarriorDetailsAPIView.as_view()),
]
