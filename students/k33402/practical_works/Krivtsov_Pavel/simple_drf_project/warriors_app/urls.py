from django.urls import path
from .views import WarriorAPIView, ProfessionCreateView


app_name = "warriors_app"


urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateView.as_view())
]
