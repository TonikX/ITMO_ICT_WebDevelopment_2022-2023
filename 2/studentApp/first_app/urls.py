from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:pk>/', views.OwnersRetrieveList.as_view()),
    path('owners/', views.OwnersList.as_view(), name="owners"),
    path('car/<int:pk>/', views.CarsRetrieveList.as_view()),
    path('cars/', views.CarsList.as_view(), name="cars"),
    path('create/', views.addOwner),
    path('cars/create', views.Create.as_view(success_url="/cars/")),
    path('car/<int:pk>/delete', views.Delete.as_view()),
    path('car/<int:pk>/edit', views.Edit.as_view())
]
