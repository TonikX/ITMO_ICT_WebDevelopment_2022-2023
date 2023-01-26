from django.urls import path
from . import views
urlpatterns = [
    path('owner/<int:driver_id>/', views.detail),
    path('allowners/', views.all_owners),
    path('allcars/', views.all_cars),
    path('crate/owner', views.DriverCreateView.as_view()),
    path('crate/car', views.CarCreateView.as_view()),
    path('update/car/<int:pk>', views.CarUpdateView.as_view()),
    path('delete/car/<int:pk>', views.CarDeleteView.as_view()),
]