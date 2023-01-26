from django.urls import path

from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login_route'),
    path('signup', SignupView.as_view(), name='signup_route'),
    path('conflist', ConferenceView.as_view(), name='conflist_route'),

    path('logout', logout_view, name='logout_route'),
    path('join_conf/<int:conf_pk>/<int:user_pk>/', join_or_leave_conf_view, name='join_or_leave_conf_route'),
    path('user_confs/<str:username>/', user_confs_view, name='user_confs_route'),

    path('conf/<int:conf_pk>/', DetailConfView.as_view(), name='detail_conf_route'),

    path('comment/create/<int:conf_pk>/', comment_view, name='add_comment_route'),
    path('comment/delete/<int:conf_pk>/<int:comment_pk>/', remove_comment_view, name='remove_comment_route'),
    path('conf/<int:conf_pk>/members', conf_members_view, name='conf_members_route')
]
