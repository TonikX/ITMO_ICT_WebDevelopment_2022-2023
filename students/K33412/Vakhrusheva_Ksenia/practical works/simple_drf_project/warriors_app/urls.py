from django.urls import path

from warriors_app.views import WarriorAPIView, ProfessionCreateView, SkillAPIView, SkillCreateView, \
	WarriorProfessionView, WarriorSkillView, SingleWarriorView, UpdateWarriorView, DeleteWarriorView

app_name = "warriors_app"

urlpatterns = [
	path('warrior/<int:pk>', SingleWarriorView.as_view()),
	path('warrior/<int:pk>/delete', DeleteWarriorView.as_view()),
	path('warrior/<int:pk>/edit', UpdateWarriorView.as_view()),
	path('warriors/', WarriorAPIView.as_view()),
	path('warriors_with_profession/', WarriorProfessionView.as_view()),
	path('warriors_with_skills/', WarriorSkillView.as_view()),
	path('profession/create', ProfessionCreateView.as_view()),
	path('skills/', SkillAPIView.as_view()),
	path('skill/create', SkillCreateView.as_view()),
]
