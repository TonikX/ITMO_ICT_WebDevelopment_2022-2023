from django.urls import path
from .views import *


app_name = "warriors_app"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participants/<int:pk>', ParticipantAPIView.as_view()),

    path('participant_ring/<int:pk>', ParticipantRingRetrieveAPIView.as_view()),
    path('club_breeds/<int:pk>', ClubBreedsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('breed_experts/', BreedExpertsAPIView.as_view()),
    path('breeds_count/', BreedCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]
