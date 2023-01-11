from django.urls import path

from .views import *

app_name = "warriors_app"

urlpatterns = [
	path('warriors/', WarriorAPIView.as_view()),
	path('profession/create', ProfessionCreateView.as_view()),
	path('skills/', SkillAPIView.as_view()),
	path('skill/create', SkillCreateView.as_view()),
	path('warriors/profession', WarriorWithProfessionView.as_view()),
	path('warriors/skills', WarriorWithSkillView.as_view()),
	path('warrior/<pk>', FullWarriorAPIView.as_view()),
	path('warrior/delete/<pk>', DeleteWarriorView.as_view()),
	path('warrior/edit/<pk>', EditWarriorView.as_view()),
]
