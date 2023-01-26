from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('warriors/<int:pk>', WarriorRetrieveUpdateDestroyAPIView.as_view()),
    path('profession/create/', ProfessionCreateAPIView.as_view()),
    path('warriors/profession',WarriorAndProfessionAPIView.as_view()),
    path('warriors/skill',WarriorAndSkillsAPIView.as_view()),
]