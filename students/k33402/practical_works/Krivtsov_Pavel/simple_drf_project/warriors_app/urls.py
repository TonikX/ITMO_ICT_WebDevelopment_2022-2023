from django.urls import path
from . import views


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', views.WarriorAPIView.as_view()),
   path('warriors/profession_info/', views.WarriorProfessionAPIView.as_view()),
   path('warriors/skills_info/', views.WarriorSkillsAPIView.as_view()),
   path('warriors/all_info/<int:pk>', views.WarriorFullInfoApiView.as_view()),
   path('warriors/<int:pk>/delete', views.WarriorDeleteApiView.as_view()),
   path('warriors/<int:pk>/update', views.WarriorUpdateApiView.as_view()),
   path('warriors/create/', views.WarriorCreateAPIView.as_view()),
   path('professions/', views.ProfessionAPIView.as_view()),
   path('profession/create/', views.ProfessionCreateView.as_view()),
   path('profession/generic_create/', views.ProfessionCreateAPIView.as_view()),
   path('skills/', views.SkillAPIView.as_view()),
   path('skills/create/', views.SkillCreateView.as_view()),
]
