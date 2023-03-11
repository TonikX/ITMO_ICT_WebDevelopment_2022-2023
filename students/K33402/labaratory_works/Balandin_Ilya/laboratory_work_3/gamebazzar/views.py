import datetime

from django.db.models import Count, Sum
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class GenreListAPIView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class PlatformListAPIView(generics.ListAPIView):
    serializer_class = PlatfomSerializer
    queryset = Platform.objects.all()


class GameListAPIView(generics.ListAPIView):
    serializer_class = GameSerializer

    def get_queryset(self):
        game_list = Game.objects.all()
        genre = self.request.query_params.get('genre')
        if genre:
            game_list = game_list.filter(genre=genre)
        return game_list


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_list = Product.objects.all()
        platform = self.request.query_params.get('platform')
        genre = self.request.query_params.get('genre')
        if platform:
            product_list = product_list.filter(platform=platform)
        if genre:
            product_list = product_list.filter(game__genre=genre)
        return product_list


class ProductUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductShortSerializer
    queryset = Product.objects.all()


class ProductAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SellListAPIView(generics.ListAPIView):
    serializer_class = SellSerializer
    queryset = Sell.objects.all()


class SellSummaryListAPIView(APIView):
    def get(self, request):
        try:
            sells = Sell.objects.values('date').annotate(amount=Sum('product__price')).order_by('date')
            data = []
            mindate = sells[0]['date']
            for s in sells:
                while mindate != s['date']:
                    data.append({'date': mindate, 'amount': 0})
                    mindate += datetime.timedelta(days=1)
                data.append(s)
            return Response(data)
        except Exception as e:
            print(e)
            return Response()


class UserAPIView(APIView):
    def get(self, request):
        try:
            user = User.objects.filter(username=request.user)
            serializer = UserOwnSerializer(user[0])
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserOwnSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserOwnSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
