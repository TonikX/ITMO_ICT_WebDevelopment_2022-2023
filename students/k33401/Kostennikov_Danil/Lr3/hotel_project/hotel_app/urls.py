from django.urls import path, include, re_path
from .views import *

app_name = "hotel_app"

urlpatterns = [
    path("living_clients/<int:room>/<str:checkInDate>/<str:checkOutDate>", ClientsLivingPeriod.as_view()),
    path("client/<str:homeTown>", ClientsCountByCity.as_view()),
    path("free_rooms/<str:date>", FreeRoomsCount.as_view()),
    path("clients_same/<str:client>", ClientsSamePeriods.as_view()),
    path("employees/<str:day>/<str:client>", EmployeesCleaning.as_view()),
    path("report/<int:quarter>", Report.as_view()),
    path("admin_/create_booking", CreateBooking.as_view()),
    path("admin_/delete_booking", DeleteBooking.as_view()),
    path("admin_/update_booking", UpdateBooking.as_view()),
    path("admin_/cr eate_employee", CreateEmployee.as_view()),
    path("admin_/delete_employee", DeleteEmployee.as_view()),
    path("admin_/update_employee", UpdateEmployee.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginView.as_view()),
]