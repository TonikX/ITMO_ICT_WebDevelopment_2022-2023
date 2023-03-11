from django.urls import path

from . import views

urlpatterns = [
    path("owners/<int:owner_id>", views.owner),
    path("owners/", views.owners),
    path("owners/create", views.create_owner),

    path("cars", views.CarList.as_view()),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view()),
    path('cars/create', views.CarCreate.as_view(success_url="/cars")),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view()),
]