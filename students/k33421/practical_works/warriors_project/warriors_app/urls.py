from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillsAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
]
