from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('warriors/profession/', WarriorProfessionListAPIView.as_view()),
   path('warriors/skill/', WarriorSkillListAPIView.as_view()),
   path('warrior/create/', WarriorCreateAPIView.as_view()),
   path('warrior/<int:pk>/', WarriorRetrieveAPIView.as_view()),
   path('warrior/update/<int:pk>/', WarriorUpdateAPIView.as_view()),
   path('warrior/delete/<int:pk>/', WarriorDeleteAPIView.as_view()),
   path('profession/generic_create/', ProfessionCreateView.as_view()),
   path('profession/create/', ProfessionCreateAPIView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skill/create/', SkillCreateAPIView.as_view()),
]