from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import authentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from typography.serializers import UserProfilesSerializer


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные пользователя", UserProfilesSerializer),
	}
)
@api_view(["GET"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profiles(request: Request):
	serializer = UserProfilesSerializer(request.user)
	return Response(serializer.data)
