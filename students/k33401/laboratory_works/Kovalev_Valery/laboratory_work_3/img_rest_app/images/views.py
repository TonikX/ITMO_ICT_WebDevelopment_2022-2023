import django_filters
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
from django.db.models import Count
import random
from rest_framework.permissions import IsAuthenticated

import images.serializers as serializers
import images.models as models


class PhotoListView(generics.ListAPIView):
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        queryset = models.Photo.objects.all()
        if self.request.query_params:
            width = self.request.query_params.get('width')
            color = self.request.query_params.get('color')
            keyword = self.request.query_params.get('keyword')
            count = self.request.query_params.get('count')
            height = self.request.query_params.get('height')
            random_seed = self.request.query_params.get('random')
            if keyword:
                keywords = models.Keyword.objects.all()
                keywords = keywords.filter(keyword__iregex=(r'\b' + keyword.lower() + r"\b"))
                photo_ids = keywords.values_list('photo', flat=True)
                queryset = queryset.filter(pk__in=photo_ids)
            if color:
                photo_ids = models.Color.objects.all().filter(keyword=str(color)).values_list("photo", flat=True)
                queryset = queryset.filter(pk__in=photo_ids)
            if count:
                queryset = queryset[:int(count)]
            if width:
                queryset = queryset.filter(photo_width=int(width))
            if height:
                queryset = queryset.filter(photo_height=int(height))
            if random_seed:
                queryset = list(queryset)
                random.seed(int(random_seed))
                random.shuffle(queryset)

        return queryset


class SearchPhotoListView(generics.ListAPIView):
    serializer_class = serializers.PhotoSerializer

    def get_queryset(self):
        queryset = models.Photo.objects.all()
        if self.request.query_params:
            photo_ids_keywords = []
            photo_ids_colors = []
            width = self.request.query_params.get('width')
            colors = self.request.query_params.getlist('colors[]')
            keywords = self.request.query_params.getlist('keywords[]')
            count = self.request.query_params.get('count')
            height = self.request.query_params.get('height')
            random_seed = self.request.query_params.get('random')
            if keywords:
                for keyword in keywords:
                    keywords_queryset = models.Keyword.objects.all()
                    keywords_queryset = keywords_queryset.filter(keyword__iregex=(r'\b' + keyword.lower() + r"\b"))
                    photo_ids_keywords.extend(keywords_queryset.values_list('photo', flat=True))
            if colors:
                colors_queryset = models.Color.objects.all()
                colors_queryset = colors_queryset.filter(keyword__in=colors)
                photo_ids_colors = colors_queryset.values_list("photo", flat=True)
            if photo_ids_keywords:
                queryset = queryset.filter(pk__in=photo_ids_keywords)
            if photo_ids_colors:
                queryset = queryset.filter(pk__in=photo_ids_colors)
            if count:
                queryset = queryset[:int(count)]
            if width:
                queryset = queryset.filter(photo_width=int(width))
            if height:
                queryset = queryset.filter(photo_height=int(height))
            if random_seed:
                queryset = list(queryset)
                random.seed(int(random_seed))
                random.shuffle(queryset)

        return queryset


class ColorView(APIView):
    def get(self, request):
        colors = models.Color.objects.all().values_list('keyword', flat=True).distinct()
        return Response({'colors': colors})


class KeywordView(generics.ListAPIView):
    queryset = models.Keyword.objects.values('keyword').annotate(total=Count("photo")).order_by("-total")
    serializer_class = serializers.KeywordsSerializer


class LikePhotoCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LikePhotoSerializer


class LikePhotoDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.LikePhotoSerializer

    def get_queryset(self):
        return models.LikePhoto.objects.all().filter(user=self.request.user)


class CollectionView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionSerializer
    pagination_class = None

    def get_queryset(self):
        return models.Collection.objects.all().filter(user=self.request.user)


class CollectionCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionSerializer


class CollectionExpandedView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionSerializerExpanded
    pagination_class = None

    def get_queryset(self):
        return models.Collection.objects.all().filter(user=self.request.user)


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionSerializer

    def get_queryset(self):
        return models.Collection.objects.all().filter(user=self.request.user)


class CollectionPhotoCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionPhotoSerializer


class CollectionPhotoDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CollectionPhotoSerializer

    def get_queryset(self):
        return models.CollectionPhoto.objects.all().filter(user=self.request.user)
