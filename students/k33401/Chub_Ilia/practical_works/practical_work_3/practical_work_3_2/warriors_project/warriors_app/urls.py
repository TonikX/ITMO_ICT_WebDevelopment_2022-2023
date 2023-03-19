from django.urls import path
from .views import *


urlpatterns = [
    path('professions/create', ProfessionCreateView.as_view()),
    path('skills/create', SkillsCreateView.as_view()),
    path('skills/all', SkillsAPIView.as_view()),
    path('all/with_skills', WarriorsWithSkillsView.as_view()),
    path('all/with_professions', WarriorsWithProfessionsView.as_view()),
    path('all', WarriorAPIView.as_view()),
    path('<int:pk>', WarriorDetailView.as_view())
]
