from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_details),
    path('owners', views.owners_list),
    path('cars', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('owner/create', views.create_owner),
    path('car/create', views.CarCreate.as_view()),
    path('car/<int:pk>/update/', views.CarUpdate.as_view()),
]
