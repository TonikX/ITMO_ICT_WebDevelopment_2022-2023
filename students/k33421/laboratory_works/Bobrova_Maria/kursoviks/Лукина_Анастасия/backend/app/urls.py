from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.exhibition_info, name="home"),
    path('exhibition/', ViewAllExhibition.as_view(), name='exhibition'),
    path('exhibition_info/', views.exhibition_info, name="exhibition_info"),
    path('exhibition_add/', views.exhibition_add, name="exhibition_add"),
    path('exhibition_my/', views.exhibition_my, name="exhibition_my"),
    path('one_exhibition_info/<int:pk>/', views.one_exhibition_info, name="one_exhibition_info"),
    path('experts_output/', views.experts_output, name="experts_output"),
    path('set_experts/', views.set_experts, name="set_experts"),
    path('competition_add/', views.competition_add, name="competition_add"),
    path('dog_to_comp/', views.dog_to_comp, name="dog_to_comp"),
    path('dog_reg/', views.dog_reg, name="dog_reg"),
    path('query/<int:query_number>/', views.query, name="query"),
]