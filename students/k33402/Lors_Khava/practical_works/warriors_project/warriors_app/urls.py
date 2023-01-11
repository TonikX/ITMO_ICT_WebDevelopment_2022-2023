from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view()), 

    path('warriors/create/', WarriorCreateAPIView.as_view()), 

    path('warriors/<int:pk>/', WarriorRetrieveAPIView.as_view()), # list warriors with skills and professions

    path('warriors/edit/<int:pk>/', WarriorRetrieveUpdateDestroyAPIView.as_view()), # update / destroy warrior by id

    path('warriors/show_professions', WarriorProfessionAPIView.as_view()),  # list warriors with professions
    path('warriors/show_skills', WarriorSkillAPIView.as_view()),  # list warriors with skills

    path('professions/', ProfessionAPIView.as_view()),  # list of professions

    path('profession/create/', ProfessionCreateAPIView.as_view()),  

    path('skills/', SkillAPIView.as_view()), 
    path('skill/create/', SkillCreateView.as_view()) 
]