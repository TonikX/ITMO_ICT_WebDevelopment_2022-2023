from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='reg'),
    path('user_list/', UserList.as_view()),
    path('race/list/', RaceList.as_view(), name='races'),
    path('race/<int:id_race>', get_race),
    path('main/', main_page, name='main'),

    path('reg_race/list/', RegRaceList.as_view()),
    path('reg_race/', RegRaceCreate.as_view()),
    path('reg_race/<int:pk>/update/', RegRaceUpdate.as_view()),
    path('reg_race/<int:pk>/delete/', RegRaceDelete.as_view()),

    path('comments/create/', make_comment),
    path('comments/list/', all_comments),
]