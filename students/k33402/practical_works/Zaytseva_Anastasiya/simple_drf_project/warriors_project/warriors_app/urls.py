from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
   path("warriors/<int:pk>/", WarriorAPIView.as_view()),
   path("warriors/<int:pk>/delete", DeleteWarriorAPIView.as_view()),
   path("warriors/<int:pk>/edit", EditWarriorAPIView.as_view()),
   path("warriors/", WarriorsAPIView.as_view()),
   path("warriors/with/profession", WarriorProfessionAPIView.as_view()),
   path("warriors/with/skill", WarriorSkillAPIView.as_view()),
   path("profession/create/", ProfessionCreateView.as_view()),
   path("skills/", SkillAPIView.as_view()),
   path("skill/create", SkillCreateView.as_view()),
]
