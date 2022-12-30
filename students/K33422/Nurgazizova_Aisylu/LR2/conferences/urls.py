from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('conferences', views.conferences, name='conferences'),
    path('conf/<str:pk>', views.conf, name='conf'),
    path('reg_to_conf/<str:pk>', views.reg_to_conf, name='registration_to_conference'),
    path('profile', views.profile, name='profile'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('comment/<str:pk>', views.add_comment, name='add_comment'),
    path('table', views.make_table, name='table'),
    path('search', views.search, name='search'),
]