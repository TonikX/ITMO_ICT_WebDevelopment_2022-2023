from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home_page, name='home'),
    path('registration/', register, name='reg'),
    path('user_list/', UserList.as_view()),
    path('race/list/', RaceList.as_view(), name='races'),
    path('race/<int:id_race>', get_race),

    path('reg_list/', RegList.as_view()),
    path('reg_race/', login_required(RegRaceCreate.as_view()), name='reg-race'),
    path('reg_race/<int:pk>/update/', RegRaceUpdate.as_view()),
    path('reg_race/<int:pk>/delete/', RegRaceDelete.as_view()),

    path('comments/create/', comment, name='comment-create'),
    path('comments/list/', all_comments),

    path('login/', log_in, name='login'),
    path('logout/',  auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')
]