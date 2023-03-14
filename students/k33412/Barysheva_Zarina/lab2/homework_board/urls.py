from django.urls import path, include
from .views import *

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('report_card/', get_report_card),
    path('assignments/', get_all_tasks),
    path('assignments/<int:task_id>/', get_task),
    path('assignments/<int:task_id>/send/', send_new_donetask),
    path('reg/', create_new_user, name='reg'),
    path('assignments/create/', create_new_task),
    path('exit/', exit),
]