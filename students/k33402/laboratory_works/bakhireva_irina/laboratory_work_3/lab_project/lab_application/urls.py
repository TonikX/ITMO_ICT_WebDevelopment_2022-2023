from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from lab_application.views import SpecializationsListView, VacanciesListView, VacancyView, MyCVGetUpdateView, \
	CoursesListView, CoursesForCVListView, SpecializationsForCVListView, CompaniesListView, CompanyView, MyCompanyView, \
	GetListAndCreateVacancyListView, GetAndUpdateVacancyView, GetCVSForVacancyListView, VacanciesForCVListView, \
	CVSListView, CVView, UserView

schema_view = get_schema_view(
	openapi.Info(
		title="Лабораторная работа №3",
		default_version='v3',
		description="Лабораторная работа №3",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@snippets.local"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=[permissions.AllowAny],
)

urlpatterns = [
	path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path("auth/", include("djoser.urls")),
	re_path("^auth/", include("djoser.urls.authtoken")),
	path("specializations/", SpecializationsListView.as_view()),
	path("courses/", CoursesListView.as_view()),
	path("vacancys/", VacanciesListView.as_view()),
	path("vacancy/<pk>/", VacancyView.as_view()),
	path("companys/", CompaniesListView.as_view()),
	path("cv/my/", MyCVGetUpdateView.as_view()),
	path("cv/my/courses_for_me/", CoursesForCVListView.as_view()),
	path("cv/my/specializations/", SpecializationsForCVListView.as_view()),
	path("cv/my/vacancys/", VacanciesForCVListView.as_view()),
	path("company/my/", MyCompanyView.as_view()),
	path("company/my/vacancys/", GetListAndCreateVacancyListView.as_view()),
	path("company/my/vacancy/<pk>/", GetAndUpdateVacancyView.as_view()),
	path("company/my/vacancy/<pk>/cvs", GetCVSForVacancyListView.as_view()),
	path("company/<pk>/", CompanyView.as_view()),
	path("cvs/", CVSListView.as_view()),
	path("cv/<pk>/", CVView.as_view()),
	path("user/", UserView.as_view()),
]
