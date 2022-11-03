from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_details),
    path('owners', views.owners_list),
    path('cars', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view())
]
