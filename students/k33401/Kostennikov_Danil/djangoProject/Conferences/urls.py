from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name='main_page'),
    path('conferences/', get_conferences, name='get_all_conferences'),
    path('conference/<int:id>/', get_conference_by_id, name='get_conference_by_id')

]