from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view()),
   path('skills/', SkillAPIView.as_view()),
   path('skill/create/', SkillCreateView.as_view()),
   path('skills_of_warrior/create/', SkillOfWarriorCreateView.as_view()),
   path('warriors_professions/', WarriorProfessionView.as_view()),
   path('warriors_skills/', WarriorSkillView.as_view()),
   path('warriors/<int:pk>/', WarriorInfoAPIView.as_view()),
   path('warriors/<int:pk>/delete', WarriorDeleteView.as_view()),
   path('warriors/<int:pk>/edit', WarriorEditView.as_view()),
]