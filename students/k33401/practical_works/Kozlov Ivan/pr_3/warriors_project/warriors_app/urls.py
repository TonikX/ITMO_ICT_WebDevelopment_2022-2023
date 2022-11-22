from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skills/', SkillsAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warrios_with_skills_and_profession/', WarriorListView.as_view()),
    path('get_warrios_by_id/<int:pk>/', WarriorView.as_view()),
    path('del_warrios_by_id/<int:pk>/', DelWarriorView.as_view()),
    path('update_warrios_by_id/<int:pk>/', UpdateWarriors.as_view()),
]
