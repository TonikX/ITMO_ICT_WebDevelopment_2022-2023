from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:motorist_id>/', views.detail),
    path('owners/', views.list_view),
    path('auto/list/', views.AutoList.as_view()),
    path('auto/<int:pk>/', views.AutoDetail.as_view()),
    path('owner_create', views.create_view),
    path('auto/<int:pk>/update/', views.AutoUpdateView.as_view()),
    path('auto/create/', views.AutoCreateView.as_view()),
    path('auto/<int:pk>/delete/', views.AutoDeleteView.as_view()),
]
