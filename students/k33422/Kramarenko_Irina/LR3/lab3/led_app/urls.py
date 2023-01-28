from django.urls import path
from .views import *

API_PREFIX = 'api/v1'
app_name = "led_app"


urlpatterns = [
    path('worker/create/', WorkerCreate.as_view()),
    path('worker/fire/<int:pk>/', WorkerDelete.as_view()),
    path('worker/update/<int:pk>/', WorkerUpdate.as_view()),
    path('workers/', WorkerListView.as_view()),
    path('brand_route/', FrequentPlane.as_view()),
    path('repair/', RepairAirplanes.as_view()),
    path('company/workers/', WorkersNumber.as_view()),
    path('company/airplanes/', AirplaneBrand.as_view()),
]