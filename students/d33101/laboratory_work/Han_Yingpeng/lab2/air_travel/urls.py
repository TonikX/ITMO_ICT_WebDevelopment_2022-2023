from django.urls import path
from . import views

urlpatterns = [
    path('', views.hellow, name='hellow'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('home/<int:user_id>', views.list_air_travel, name='list_air_travel'),
    path('my_travels/<int:user_id>', views.list_my_air_travel, name='my_list_air_travel'),
    path('passenger/<int:travel_id>', views.list_passenger, name='list_passenger'),
    path('passenger_create/<int:user_id>/<int:travel_id>', views.create_passenger, name='create_passenger'),
    path('passenger_edit/<int:user_id>/<int:travel_id>', views.edit_passenger, name='edit_passenger'),
    path('comment/<int:user_id>/<int:travel_id>', views.list_comment, name='list_comment'),
    path('create_comment/<int:user_id>/<int:travel_id>', views.create_comment, name='create_comment'),
    path('logout/', views.user_logout, name='user_logout'),
]
