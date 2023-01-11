from django.urls import path
from project_first_app import views

urlpatterns = [
    path('owner/<int:pk>/', views.detail, name='view_owner'),
    path('owner/', views.list_view, name='view_owners'),
    path('owner/create', views.create_owner, name='create_owner'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='view_car'),
    path('car/', views.CarListView.as_view()),
    path('car/create', views.CarCreateView.as_view(), name='create_car'),
    path('car/<int:pk>/update', views.CarUpdateView.as_view(), name='update_car'),
    path('car/<int:pk>/delete', views.CarDeleteView.as_view(), name='delete_car'),
]
