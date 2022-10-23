from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('main/', main_page, name='main_page'),
    path('conferences/', get_conferences, name='get_all_conferences'),
    path('conference/<int:id>/', get_conference_by_id, name='get_conference_by_id'),
    #path("registration/", views.register_request, name="register"),
   # path("registration/", views.registr_user, name="register"),
    path("registration/", views.Reg_user.as_view(), name="register"),
    path("conference_apply/<int:id>/", views.conference_apply, name="conference_apply"),
    path("applies", views.applies, name='applies'),
    path("applies/<str:email>/", views.user_applies, name='user_applies'),
    path("delete_apply/<str:email>/<int:id>", views.delete_apply, name='delete_apply'),
    path("create_comment/<int:id>", views.create_comment, name='create_comment')



]