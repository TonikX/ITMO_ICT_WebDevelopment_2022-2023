from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_page, name='main_page'),

]