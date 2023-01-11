from django.urls import path
from .views import *


urlpatterns = [
   path('guest/list', GuestListView.as_view()),
   path('guest/create', GuestCreateView.as_view()),
   path('guest/<int:pk>/update', GuestUpdateView.as_view()),
   path('guest/<int:pk>/delete', GuestDestroyView.as_view()),

   path('employee/list', EmployeeListView.as_view()),
   path('employee/create', EmployeeCreateView.as_view()),
   path('employee/<int:pk>/update', EmployeeUpdateView.as_view()),
   path('employee/<int:pk>/delete', EmployeeDestroyView.as_view()),

   path('cleaning/list', CleaningListView.as_view()),
   path('cleaning/create', CleaningCreateView.as_view()),
   path('cleaning/<int:pk>/update', CleaningUpdateView.as_view()),
   path('cleaning/<int:pk>/delete', CleaningDestroyView.as_view()),

   path('room/list', RoomListView.as_view()),
   path('room/create', RoomCreateView.as_view()),
   path('room/<int:pk>/update', RoomUpdateView.as_view()),
   path('room/<int:pk>/delete', RoomDestroyView.as_view()),

   path('booking/list', BookingListView.as_view()),
   path('booking/create', BookingCreateView.as_view()),
   path('booking/<int:pk>/update', BookingUpdateView.as_view()),
   path('booking/<int:pk>/delete', BookingDestroyView.as_view()),

]