from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

# from backend.api.app.serializers import PostSerializer
from backend.profiles.models import Profile
from .serializers import ProfileSer, EditAvatar


class ProfileUser(APIView):
    """Вывод профиля пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = ProfileSer(Profile.objects.get(user=request.user))
        #i_follow = Profile.objects.filter(follow=request.user).values_list('id', flat=True)
        #print(i_follow)
        return Response(ser.data)


class UpdateProfile(APIView):
    """Редактирование профиля"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        prof = Profile.objects.get(user=request.user)
        ser = EditAvatar(prof, data=request.data)
        if ser.is_valid():
            if "avatar" in request.FILES:
                ser.save(avatar=request.FILES["avatar"])
                return Response(status=201)
        else:
            return Response(status=400)


