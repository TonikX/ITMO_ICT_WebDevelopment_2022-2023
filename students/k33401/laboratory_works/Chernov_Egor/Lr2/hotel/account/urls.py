from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.RegView.as_view(), name='index'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('hotels/', include('hotel_first_app.urls')),
]
