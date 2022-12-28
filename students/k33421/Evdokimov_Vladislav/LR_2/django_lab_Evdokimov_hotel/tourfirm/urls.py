from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('profile/', views.profile),
    path('login/', views.user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', views.log_out),
    path('reservedtour/', views.reservedtourlist),
    path('comments/', views.commentlist),
    path('createcomment/<int:pk>/', CreateComment.as_view()),
    path('tours/', views.tourlist),
    path('tours_for_notauth/', show_tours_not_auth),
    path('tours/<int:pk>/reservation', CreateReservation.as_view(), name='reservation'),
    path('profilereservations/', listreservations.as_view(), name='listreservations'),
    path('profilereservations/deletereservation/<int:pk>/', views.DeleteReserveView.as_view()),
    path('profilereservations/updatereservation/<int:pk>/', views.UpdateReserveView.as_view())
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



