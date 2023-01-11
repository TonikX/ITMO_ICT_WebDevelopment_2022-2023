from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="my@n.ru"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

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
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]
