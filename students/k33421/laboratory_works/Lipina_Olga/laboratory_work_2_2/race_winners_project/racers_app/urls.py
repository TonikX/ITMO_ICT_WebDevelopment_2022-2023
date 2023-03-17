from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
   # path('registration/', RegisterUser.as_view(), name='reg'),
    path('registration/', register, name='reg'),
    path('user_list/', UserList.as_view()),
    path('race/list/', RaceList.as_view(), name='races'),
    path('race/<int:id_race>', get_race),
    path('main/', main_page, name='main'),

    path('reg_race/list/', reg_race_list_vies),
    path('reg_race/', login_required(RegRaceCreate.as_view()), name='reg-race'),
    path('reg_race/<int:pk>/update/', RegRaceUpdate.as_view()),
    path('reg_race/<int:pk>/delete/', RegRaceDelete.as_view()),

    path('comments/create/', make_comment, name='comment-create'),
    path('comments/list/', all_comments),

    path('login/', log_in, name='login'),
    path('logout/',  auth_views.LogoutView.as_view(template_name='logout_django.html'), name='logout')
]