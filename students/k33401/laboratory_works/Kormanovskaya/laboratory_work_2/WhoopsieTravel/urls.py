from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('countries/', countries_list, name='countries_list_url'),
    path('countries/<str:slug>/', country_details, name='country_details_url'),

    path('tours/', tours_list, name='tours_list_url'),
    path('tours/<str:slug>/', tour_details, name='tour_details_url'),

    path('registration/', registration, name='registration_url'),
    path('login/', login_page, name='login_url'),
    path('logout/', logout_user, name='logout_url'),

    path('profile/', profile, name='profile_url'),
    path('sells/', sells, name='sells_url'),

    path('profile/<int:pk>/review/update/', ReviewUpdate.as_view()),

    path('profile/<int:pk>/delete/', TourConductingDelete.as_view()),
    path('profile/<int:pk>/update/', TourConductingUpdate.as_view()),
]
