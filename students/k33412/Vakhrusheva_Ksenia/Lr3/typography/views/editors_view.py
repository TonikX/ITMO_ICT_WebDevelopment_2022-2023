from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, exceptions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from typography.auth import MEProfilesAuthentication
from typography.models import Editor
from typography.serializers import PublicEditorSerializer, PrivateEditorSerializer


class EditorsApiView(generics.ListAPIView):
	queryset = Editor.objects.all()
	serializer_class = PublicEditorSerializer


class GetEditorApiView(generics.RetrieveAPIView):
	queryset = Editor.objects.all()
	serializer_class = PublicEditorSerializer


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные редактора", PrivateEditorSerializer),
		401: "You can only see full information about your own account"
	}
)
@api_view(["GET"])
@authentication_classes([MEProfilesAuthentication])
@permission_classes([IsAuthenticated])
def get_editor_full(request: Request, pk: int):
	editor = Editor.objects.get(user=pk)
	if isinstance(request.auth, Editor):
		current_editor: Editor = request.auth
		if current_editor != editor:
			raise exceptions.AuthenticationFailed("You can only see full information about your own account")

	serializer = PrivateEditorSerializer(editor)
	return Response(serializer.data)
