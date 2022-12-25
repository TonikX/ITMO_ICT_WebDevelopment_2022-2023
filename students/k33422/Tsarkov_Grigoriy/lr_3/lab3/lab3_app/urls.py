from django.urls import path
from .views import *


app_name = "lab3_app"


urlpatterns = [
    path('experts/<int:pk>', ExpertAPIView.as_view()),
    path('participation/', ParticipationAPIList.as_view()),
    path('participants/', ParticipantAPIList.as_view()),

    path('participant_stage/<int:pk>', StageParticipationAPIView.as_view()),
    path('club_fandoms/<int:pk>', ClubFandomsRetrieveAPIView.as_view()),
    path('dismissed_count/<int:pk>', DismissedCountAPIView.as_view()),
    path('fandom_experts/', FandomExpertsAPIView.as_view()),
    path('fandoms_count/', FandomCountAPIView.as_view()),
    path('report/<int:year>', ReportAPIView.as_view()),
]
