from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillAPIView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('warrior-profession/list', WarriorAndProfessionListAPIView.as_view()),
    path('warriors-skill/list', WarriorAndSkillListAPIView.as_view()),
    path('warrior/<int:pk>', WarriorGetAPIView.as_view()),
]