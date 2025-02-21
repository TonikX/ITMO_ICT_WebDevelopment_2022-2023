from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import *
from .models import Timetable


def group_timetable_by_days(timetable, timetable_serializer_class):
    timetable_by_days = {}
    for week_day, _ in WEEK_DAYS:
        timetable_by_days[week_day] = timetable_serializer_class(timetable.filter(week_day=week_day).first()).data

    return timetable_by_days


class ProfilePageAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        doctor = request.user
        doctor_serializer = DoctorShortSerializer(doctor)

        doctor_timetable = Timetable.objects.filter(doctor=doctor)
        return Response({'Doctor': doctor_serializer.data,
                        'Timetable': group_timetable_by_days(doctor_timetable, TimetableShortSerializer)})


class DoctorsPageAPIView(generics.ListAPIView):
    serializer_class = DoctorShortSerializer
    queryset = Doctor.objects.filter(is_superuser=False)


class OneDoctorPageAPIView(APIView):

    def get(self, request, *args, **kwargs):
        doctor = Doctor.objects.filter(pk=kwargs['pk']).first()
        doctor_serializer = DoctorFullSerializer(doctor)

        doctor_timetable = Timetable.objects.filter(doctor=doctor)

        return Response({'Doctor': doctor_serializer.data,
                        'Timetable': group_timetable_by_days(doctor_timetable, TimetableShortSerializer)})

class CabinetsPageAPIView(generics.ListAPIView):
    serializer_class = CabinetShortSerializer
    queryset = Cabinet.objects.all()


class CabinetCreatePageAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CabinetFullSerializer
    queryset = Cabinet.objects.all()


class CabinetUpdatePageAPIView(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CabinetFullSerializer
    queryset = Cabinet.objects.all()


class CabinetDestroyPageAPIView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Cabinet.objects.all()


class OneCabinetPageAPIView(APIView):

    def get(self, request, *args, **kwargs):
        cabinet = Cabinet.objects.filter(pk=kwargs['pk']).first()
        cabinet_serializer = CabinetFullSerializer(cabinet)

        cabinet_timetable = Timetable.objects.filter(cabinet=cabinet)

        return Response({'Cabinet': cabinet_serializer.data,
                        'Timetable': group_timetable_by_days(cabinet_timetable, TimetableFullSerializer)})


class PatientsPageAPIView(generics.ListAPIView):
    serializer_class = PatientShortSerializer
    queryset = Patient.objects.all()


class PatientCreatePageAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientCreateSerializer
    queryset = Patient.objects.all()


class PatientUpdatePageAPIView(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientCreateSerializer
    queryset = Patient.objects.all()


class PatientDestroyPageAPIView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()


class OnePatientPageAPIView(generics.RetrieveAPIView):
    serializer_class = PatientFullSerializer
    queryset = Patient.objects.all()


class AppoitmentPageAPIView(generics.RetrieveAPIView):
    serializer_class = AppointmentFullSerializer
    queryset = Appointment.objects.all()


class AppoitmentCreatePageAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentCreateSerializer
    queryset = Appointment.objects.all()


class AppoitmentUpdatePageAPIView(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentCreateSerializer
    queryset = Appointment.objects.all()


class AppoitmentDestroyPageAPIView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Appointment.objects.all()


class TimetableCreatePageAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TimetableCreateSerializer
    queryset = Timetable.objects.all()


class TimetableUpdatePageAPIView(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TimetableCreateSerializer
    queryset = Timetable.objects.all()


class TimetableDestroyPageAPIView(generics.DestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Timetable.objects.all()