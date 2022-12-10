from django.urls import path
from .views import *

app_name = "warriors_app"

urlpatterns = [
    path('warriors/', WarriorListAPIView.as_view()),
    path('warriors/<int:pk>/', WarriorAPIView.as_view()),
    path('warriors/<int:pk>/update/', WarriorAPIUpdate.as_view()),
    path('warriors/<int:pk>/delete/', WarriorAPIDelete.as_view()),
    path('jobs', JobsListAPIView.as_view()),
    path('job/create/', JobCreateAPIView.as_view()),
    path('skills/', SkillListAPIView.as_view()),
    path('skill/create/', SkillCreateAPIView.as_view()),
]
