from django.urls import path
from .views import *

app_name = 'clinic'

urlpatterns = [
    path('profile/', ProfilePageAPIView.as_view()),
    path('doctors/', DoctorsPageAPIView.as_view()),
    path('doctors/<int:pk>/', OneDoctorPageAPIView.as_view()),
    path('cabinets/', CabinetsPageAPIView.as_view()),
    path('cabinets/create/', CabinetCreatePageAPIView.as_view()),
    path('cabinets/<int:pk>/', OneCabinetPageAPIView.as_view()),
    path('cabinets/<int:pk>/update', CabinetUpdatePageAPIView.as_view()),
    path('cabinets/<int:pk>/delete', CabinetDestroyPageAPIView.as_view()),
    path('patients/', PatientsPageAPIView.as_view()),
    path('patients/create/', PatientCreatePageAPIView.as_view()),
    path('patients/<int:pk>/', OnePatientPageAPIView.as_view()),
    path('patients/<int:pk>/update', PatientUpdatePageAPIView.as_view()),
    path('patients/<int:pk>/delete', PatientDestroyPageAPIView.as_view()),
    path('appointments/create/', AppoitmentCreatePageAPIView.as_view()),
    path('appointments/<int:pk>/', AppoitmentPageAPIView.as_view()),
    path('appointments/<int:pk>/update', AppoitmentUpdatePageAPIView.as_view()),
    path('appointments/<int:pk>/delete', AppoitmentDestroyPageAPIView.as_view()),
    path('timetable/create', TimetableCreatePageAPIView.as_view()),
    path('timetable/<int:pk>/update', TimetableUpdatePageAPIView.as_view()),
    path('timetable/<int:pk>/delete', TimetableDestroyPageAPIView.as_view()),
]