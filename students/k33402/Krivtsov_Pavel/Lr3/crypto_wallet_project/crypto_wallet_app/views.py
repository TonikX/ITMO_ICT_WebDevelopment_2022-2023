from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework import filters
from .models import Currency, Ownership, Transaction, Discussion, Tag, Comment
from . import serializers


class CurrenciesListApiView(generics.ListAPIView):
    """
    Displaying all currencies
    """
    serializer_class = serializers.CurrencySerializer
    queryset = Currency.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "abbreviation"]
    ordering_fields = ['price', 'date_added']


class PopularCurrenciesListApiView(generics.ListAPIView):
    """
    Displaying first three currencies
    """
    serializer_class = serializers.CurrencySerializer
    queryset = Currency.objects.filter(id__lte=3)


class CurrencyInfoApiView(generics.RetrieveAPIView):
    """
    Displaying information about the currency by id
    """
    serializer_class = serializers.CurrencySerializer
    queryset = Currency.objects.all()


class CurrencyCreateApiView(generics.CreateAPIView):
    """
    Creates currency
    """
    serializer_class = serializers.CurrencySerializer
    permission_classes = (permissions.IsAdminUser,)


class AllOwnershipListApiView(generics.ListAPIView):
    """
    Displaying all ownerships for admins
    """
    serializer_class = serializers.OwnershipSerializer
    queryset = Ownership.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UserOwnershipsListApiView(generics.ListAPIView):
    """
    Displaying user ownerships
    """
    serializer_class = serializers.OwnershipSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied()

        return Ownership.objects.filter(user=user)


class OwnershipCreateApiView(APIView):
    """
    Creates ownership
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied()

        request_data = request.data.copy()
        request_data["user"] = user.id

        serializer = serializers.OwnershipSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OwnershipUpdateApiView(generics.UpdateAPIView):
    """
    Updates ownership
    """
    queryset = Ownership.objects.all()
    serializer_class = serializers.OwnershipUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TransactionCreateApiView(APIView):
    """
    Creates transaction
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied()

        request_data = request.data.copy()
        request_data["user"] = user.id

        serializer = serializers.TransactionSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllTransactionListApiView(generics.ListAPIView):
    """
    Displaying all transaction for admins
    """
    serializer_class = serializers.TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UserTransactionsListApiView(generics.ListAPIView):
    """
    Displaying user transactions
    """
    serializer_class = serializers.TransactionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied()

        return Transaction.objects.filter(user=user)


class DiscussionCreateApiView(APIView):
    """
    Creates discussion
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied()

        request_data = request.data.copy()
        request_data["user"] = user.id

        serializer = serializers.DiscussionSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscussionsListApiView(generics.ListAPIView):
    """
    Show all discussions
    """
    serializer_class = serializers.DiscussionSerializer
    queryset = Discussion.objects.all()


class TagCreateApiView(generics.CreateAPIView):
    """
    Creates tag
    """
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.IsAdminUser,)


class TagsListApiView(generics.ListAPIView):
    """
    Show all tags
    """
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()


class CommentCreateApiView(APIView):
    """
    Creates comment
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            raise PermissionDenied()

        request_data = request.data.copy()
        request_data["user"] = user.id

        serializer = serializers.CommentSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsListApiView(APIView):
    """
    Show comments for special discussion
    """
    def get_objects(self, discussion_id):
        return Comment.objects.filter(discussion=discussion_id)

    def get(self, request, pk):
        comments = self.get_objects(pk)
        serializer = serializers.CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
