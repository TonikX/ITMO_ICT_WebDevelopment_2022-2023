from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from typography.auth import EditorAuthentication, AMEProfilesAuthentication
from typography.models import Book, Author, Editor
from typography.serializers import PublicBookSerializer, UpdateBookSerializer, PrivateBookSerializer


class BooksApiView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = PublicBookSerializer


class GetAndPatchBookApiView(APIView):
	authentication_classes = [EditorAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly]

	@swagger_auto_schema(
		responses={200: openapi.Response("Данные книги", PublicBookSerializer)}
	)
	def get(self, request: Request, pk: int):
		book = Book.objects.get(id=pk)
		serializer = PublicBookSerializer(book)
		return Response(serializer.data)

	@swagger_auto_schema(
		request_body=UpdateBookSerializer,
		responses={200: openapi.Response("Отредактированные данные книги", PrivateBookSerializer)}
	)
	def patch(self, request: Request, pk: int):
		book = Book.objects.get(id=pk)
		if isinstance(request.auth, Editor):
			editor: Editor = request.auth
			if editor not in book.editors.all():
				raise exceptions.AuthenticationFailed(f"This book doesn't belong to you")

		new_book = request.data
		serializer = UpdateBookSerializer(book, data=new_book, partial=True)
		serializer.is_valid(raise_exception=True)
		book_saved = serializer.save()
		get_serializer = PrivateBookSerializer(book_saved)
		return Response(get_serializer.data)


@swagger_auto_schema(
	method="GET",
	responses={
		200: openapi.Response("Данные книги", PrivateBookSerializer),
		401: "This book doesn't belong to you"
	}
)
@api_view(["GET"])
@authentication_classes([AMEProfilesAuthentication])
@permission_classes([IsAuthenticated])
def get_book_full(request: Request, pk: int):
	book = Book.objects.get(id=pk)

	if isinstance(request.auth, Author):
		author: Author = request.auth
		if book not in author.books.all():
			raise exceptions.AuthenticationFailed("This book doesn't belong to you")

	serializer = PrivateBookSerializer(book)
	return Response(serializer.data)
