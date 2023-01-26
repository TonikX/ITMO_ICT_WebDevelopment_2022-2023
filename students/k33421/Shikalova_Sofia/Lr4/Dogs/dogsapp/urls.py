from django.urls import path
from .views import *


app_name = "dogsapp"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participation/', ParticipationAPIList.as_view()),
    path('participants/', ParticipantAPIList.as_view()),

    path('participant_ring/<int:pk>', RingParticipationAPIView.as_view()),
    path('club_breeds/<int:pk>', ClubBreedsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('breed_experts/', BreedExpertsAPIView.as_view()),
    path('breeds_count/', BreedCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]
