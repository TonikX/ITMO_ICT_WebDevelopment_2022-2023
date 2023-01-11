from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *

app_name = "dogs_app"

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v2",
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vkorobkovskiy@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path("owner/", OwnerListAPIView.as_view()),
    path("owner/<int:pk>/", OwnerAPIView.as_view()),
    path("owner/create/", OwnerCreateAPIView.as_view()),
    path("club/", ClubListAPIView.as_view()),
    path("club/<int:pk>/", ClubAPIView.as_view()),
    path("club/create/", ClubCreateAPIView.as_view()),
    path("dog/", DogListAPIView.as_view()),
    path("dog/<int:pk>/", DogAPIView.as_view()),
    path("dog/create/", DogCreateAPIView.as_view()),
    path("show/", ShowListAPIView.as_view()),
    path("show/<int:pk>/", ShowAPIView.as_view()),
    path("show/create/", ShowCreateAPIView.as_view()),
    path("dog_reg/", DogParticipationListAPIView.as_view()),
    path("dog_reg/<int:pk>/", DogParticipationAPIView.as_view()),
    path("dog_reg/create/", DogParticipantCreateAPIView.as_view()),
    path("expert/", ExpertListAPIView.as_view()),
    path("expert/<int:pk>/", ExpertAPIView.as_view()),
    path("expert/create/", ExpertCreateAPIView.as_view()),
    path("expert_reg/", ExpertParticipationListAPIView.as_view()),
    path("expert_reg/<int:pk>/", ExpertParticipationAPIView.as_view()),
    path("expert_reg/create/", ExpertParticipationCreateAPIView.as_view()),
    path("sponsor/", SponsorListAPIView.as_view()),
    path("sponsor/<int:pk>/", SponsorAPIView.as_view()),
    path("sponsor/create/", SponsorCreateAPIView.as_view()),
    path("sponsorship/", SponsorshipListAPIView.as_view()),
    path("sponsorship/<int:pk>/", SponsorshipAPIView.as_view()),
    path("sponsorship/create/", SponsorshipCreateAPIView.as_view()),
    path("schedule/", ShowScheduleListAPIView.as_view()),
    path("schedule/<int:pk>/", ShowScheduleAPIView.as_view()),
    path("schedule/create/", ShowScheduleCreateAPIView.as_view()),
    path("grading/", GradingListAPIView.as_view()),
    path("grading/<int:pk>/", GradingAPIView.as_view()),
    path("grading/create", GradingCreateAPIView.as_view()),

    path("dog_ring/<int:id>/", DogRingAPIView.as_view()),
    path("club_breeds/<int:id>/", ClubBreedAPIView.as_view()),
    path("miss_count/<int:id>/", DogNotAllowedOrSuspendedCountAPIView.as_view()),
    path("breed_experts/", BreedExpertsAPIView.as_view()),
    path("breeds_count/", BreedCountAPIView.as_view()),
    path("report/<int:id>/", ReportAPIView.as_view()),

    path("doc/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("doc/redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
