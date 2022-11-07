from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_details),
    path('owners', views.owners_list),
    path('owner/create', views.create_owner),
    path('cars', views.CarList.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('car/create', views.CarCreateView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view())
]
