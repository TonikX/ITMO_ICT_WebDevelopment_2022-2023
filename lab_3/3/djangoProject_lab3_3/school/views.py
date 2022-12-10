
from rest_framework import serializers, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *


# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','age','sex','role']


class School_class_Serializer(serializers.ModelSerializer):
    class Meta:
        model = School_class
        fields = "__all__"


class Student_class_teacher_Serializer(serializers.ModelSerializer):
    book = School_class_Serializer()
    user = UserSerializer()

    class Meta:
        model = Student_class_teacher
        fields = "__all__"


class User_APIView(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class User_UpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class School_class_CreateAPIView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = School_class_Serializer
    queryset = School_class.objects.all()


class School_class_APIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = School_class_Serializer
    queryset = School_class.objects.all()



class Student_class_teacher_CreateAPIView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = Student_class_teacher_Serializer
    queryset = Student_class_teacher.objects.all()


class SStudent_class_teacher_APIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = Student_class_teacher_Serializer
    queryset = Student_class_teacher.objects.all()

