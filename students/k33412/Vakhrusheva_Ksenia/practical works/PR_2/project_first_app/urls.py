from django.urls import path

from project_first_app import views

urlpatterns = [
	path('owner/<int:pk>/', views.detail, name='detail'),
	path('owner/', views.list_view, name='list_view'),
	path('vehicle/<int:pk>/', views.VehicleDetail.as_view(), name='vehicle_detail'),
	path('vehicle/', views.VehicleList.as_view()),
	path('owner/create', views.create_owner, name='owner_create'),
	path('vehicle/create', views.VehicleCreate.as_view(), name='vehicle_create'),
	path('vehicle/<int:pk>/update', views.VehicleUpdate.as_view(), name='vehicle_update'),
	path('vehicle/<int:pk>/delete', views.VehicleDelete.as_view(), name='vehicle_delete'),
]
