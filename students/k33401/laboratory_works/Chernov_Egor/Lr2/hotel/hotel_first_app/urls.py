from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
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
