from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegView.as_view(), name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.mlogin, name='login'),
    path('logout/', views.mlogout, name='logout'),
]

# Просмотр отелей и номеров
# catalog/hotels/
# catalog/hotel/<int:id>
# catalog/hotel/<int:id>/rooms/
# catalog/hotel/<int:id>/room/<int:id>

# Вход/рег
# account/login/
# account/registration/

# Личный акк
# account/user/<int:id>

# Написание отзыва
# catalog/hotel/<int:id>/room/<int:id>/review

# username: test1
# mail: test1@mail.ru
# password: test112345678