from django.urls import path, include
from .views import *


urlpatterns = [
    path('', RegView.as_view(), name='index'),
    path('error/', error, name='error'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('hotels/', include('hotel_first_app.urls')),
    path('account/<int:pk>/', AccountUserView.as_view(), name='account'),
    path('account/<int:id_user>/update/<int:pk>', UpdateReserveView.as_view(), name='update_reserve'),
    path('account/<int:id_user>/delete/<int:pk>', ReserveDeleteView.as_view(), name='delete_reserve'),
]

# Вход/рег
# account/login/
# account/registration/

# Личный акк
# account/user/<int:id>
