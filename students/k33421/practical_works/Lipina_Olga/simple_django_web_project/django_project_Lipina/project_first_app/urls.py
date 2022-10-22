from django.contrib import admin
from django.urls import path

from .views import get_car_owner, get_all_owners, AutoList, AutoRetrieveView, create_owner, AutoCreate, AutoDelete, \
    AutoUpdate, CreateOwnerForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('owners/<int:id_owner>', get_car_owner),
    path('owners/', get_all_owners),
    path('owners/create', create_owner),

    path('autos/<int:pk>', AutoRetrieveView.as_view()),
    path('autos/', AutoList.as_view()),
    path('autos/create', AutoCreate.as_view()),
    path('autos/<int:pk>/delete', AutoDelete.as_view()),
    path('autos/<int:pk>/update', AutoUpdate.as_view()),

    path("owners/create/new", CreateOwnerForm.as_view()),
]
