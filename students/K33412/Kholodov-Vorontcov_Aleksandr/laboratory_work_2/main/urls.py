from django.urls import path
from django.contrib.auth.decorators import login_required
from main import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.log_in, name='login'),
    path('log_out', views.log_out, name='logout'),
    path('class_grades', views.class_grades_list, name='class_grades'),
    path('homework', login_required(views.HomeworkList.as_view()),
         name='homework_list'),
    path('homework/<int:pk>', login_required(views.HomeworkDetail.as_view()),
         name='homework_detail'),
    path('handin/<int:pk>', login_required(views.hand_in), name='handin')
]
