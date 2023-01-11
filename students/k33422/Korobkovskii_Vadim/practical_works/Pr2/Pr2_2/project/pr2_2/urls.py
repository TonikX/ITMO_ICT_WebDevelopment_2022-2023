from django.urls import path

from . import views

urlpatterns = [
    #path("owner/<int:owner_id>/", views.get_info_owner),
    #path("all_owners/", views.get_info_all_owners),
    #path("car/<int:car_id>/", views.get_info_car),
    #path("all_cars/", views.get_info_all_cars),
    path("", views.IndexView.as_view()),

    path('owner/<int:pk>/', views.OwnerRetrieveView.as_view()),
    path("owner/list/", views.OwnerListView.as_view()),
    path("owner/<int:pk>/update/", views.OwnerUpdateView.as_view()),
    path("owner/create/", views.OwnerCreateView.as_view()),
    path("owner_create/", views.create_view),
    path("owner/<int:pk>/delete/", views.OwnerDeleteView.as_view()),

    path("car/<int:pk>/", views.CarRetrieveView.as_view()),
    path("car/list/", views.CarListView.as_view()),
    path("car/<int:pk>/update/", views.CarUpdateView.as_view()),
    path("car/create/", views.CarCreateView.as_view()),
    path("car/<int:pk>/delete/", views.CarDeleteView.as_view()),
]