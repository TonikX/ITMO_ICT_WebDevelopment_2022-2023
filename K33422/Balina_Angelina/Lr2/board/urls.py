from django.urls import path
from .views import *

urlpatterns = [
    path('', find_home, name='home'),
    path('register', register, name='register'),
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('all_hw', AllHomework.as_view()),
    path('hw/<int:pk>', OneHomework.as_view()),
    path('hw/<int:pk>/submit', AddSubmission.as_view(success_url="/all_hw")),
    path('our_grades', OurGrades.as_view()),
    ]
