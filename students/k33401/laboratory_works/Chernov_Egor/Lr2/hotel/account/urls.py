from django.urls import path, include
from .views import *

urlpatterns = [
    path('', RegView.as_view(), name='index'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('hotels/', include('hotel_first_app.urls')),
]

# Вход/рег
# account/login/
# account/registration/

# Личный акк
# account/user/<int:id>
