from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions, generics, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from typography.auth import AuthorAuthentication, AMEProfilesAuthentication
from typography.exceptions import BadRequest
from typography.models import Author
from typography.serializers import PublicAuthorSerializer, UpdateAuthorSerializer, PrivateAuthorSerializer


class AuthorsApiView(generics.ListCreateAPIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Author.objects.all()
	serializer_class = PublicAuthorSerializer

	@swagger_auto_schema(
		responses={201: openapi.Response("Данные автора", PublicAuthorSerializer),
		           400: "Unable to create another author profile"}
	)
	def post(self, request):
		if self.get_queryset().filter(user=request.user).exists():
			raise BadRequest("Unable to create another author profile")

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save(user=request.user)
		return Response(serializer.data, status=201)


class GetAndPatchAuthorApiView(APIView):
	authentication_classes = [AuthorAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]

	@swagger_auto_schema(
		responses={200: openapi.Response("Данные автора", PublicAuthorSerializer)}
	)
	def get(self, request: Request, pk: int):
		author = Author.objects.get(user=pk)
		serializer = PublicAuthorSerializer(author)
		return Response(serializer.data)

	@swagger_auto_schema(
		request_body=UpdateAuthorSerializer,
		responses={200: openapi.Response("Отредактированные данные книги", PublicAuthorSerializer)}
	)
	def patch(self, request: Request, pk: int):
		author = Author.objects.get(user=pk)
		current_author: Author = request.auth
		if current_author != author:
			raise exceptions.AuthenticationFailed("You can only edit your own account")

		new_author = request.data
		serializer = UpdateAuthorSerializer(current_author, data=new_author, partial=True)
		serializer.is_valid(raise_exception=True)
		new_author = serializer.save()
		get_serializer = PublicAuthorSerializer(new_author)
		return Response(get_serializer.data)


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные автора", PrivateAuthorSerializer),
		401: "You can only see full information about your own account"
	}
)
@api_view(["GET"])
@authentication_classes([AMEProfilesAuthentication])
@permission_classes([IsAuthenticated])
def get_author_full(request: Request, pk: int):
	author = Author.objects.get(user=pk)
	if isinstance(request.auth, Author):
		current_author: Author = request.auth
		if current_author != author:
			raise exceptions.AuthenticationFailed("You can only see full information about your own account")

	serializer = PrivateAuthorSerializer(author)
	return Response(serializer.data)
