from rest_framework import serializers
from .models import *


class DoctorFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'specialty', 'education', 
                   'date_of_birth', 'start_work_date', 'finish_work_date', 'contract_number']


class DoctorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'specialty']


class CabinetFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'


class CabinetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ['id', 'number']


class AppointmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentType
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentFullSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField('get_doctor')
    cabinet = CabinetShortSerializer()
    type = serializers.StringRelatedField()

    def get_doctor(self, appointment):
        week_day = appointment.finish_time.weekday()
        doctor = Doctor.objects.filter(
            timetable__cabinet=appointment.cabinet,
            timetable__week_day=WEEK_DAYS[week_day][0]
        ).first()

        return DoctorShortSerializer(doctor).data

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'cabinet', 'patient', 'finish_time', 'start_time', 'type', 'diagnosis',
                     'health_status', 'recommendations', 'payed', 'form_of_payment']


class PatientFullSerializer(serializers.ModelSerializer):
    appointments = AppointmentFullSerializer(many=True)

    class Meta:
        model = Patient
        fields = '__all__'


class PatientShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'middle_name', 'last_name']


class PatientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class TimetableShortSerializer(serializers.ModelSerializer):
    cabinet = CabinetShortSerializer()

    class Meta:
        model = Timetable
        fields = ['cabinet']


class TimetableCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = '__all__'


class TimetableFullSerializer(serializers.ModelSerializer):
    doctor = DoctorShortSerializer()
    cabinet = serializers.StringRelatedField()

    class Meta:
        model = Timetable
        fields = '__all__'