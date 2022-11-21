from django.urls import path

from homework_app import views

urlpatterns = [
    path('student/register/', views.StudentSignUpView.as_view(), name='register'),
    path('teacher/register/', views.TearchSignUpView.as_view(), name='Tregister'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('class_grades/', views.class_grades_list, name='class_grades'),
    path('homework/create/', views.HomeworkCreate.as_view(),name='homework_create'),
    path('homeworks/', views.HomeworkList.as_view(),name='homework_list'),
    path('homework/<int:pk>', views.HomeworkDetail.as_view(),
         name='homework_detail'),
    path('handin/<int:pk>', views.hand_in, name='handin'),
    path('mygrade/', views.AssignmentView.as_view(),name='mygrade'),
]