from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/', WarriorAPIView.as_view()),
    path('professions/', ProfessionAPIView.as_view()),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),

    path('warriors_professions/', WarriorsProfessionsListAPIView.as_view()),
    path('warriors_skills/', SkillAPIView.as_view()),
    path('warrior/<int:pk>', WarriorRetrieveAPIView.as_view()),
    path('delete_warrior/<int:pk>', WarriorAPIView.as_view()),
    path('edit_warrior/<int:pk>', WarriorAPIView.as_view()),
    ]