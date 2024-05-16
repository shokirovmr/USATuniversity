from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import GalleryModel, NewsModel
from .serializers import GallerySerializer, NewsSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = GalleryModel.objects.all()
    serializer_class = GallerySerializer
    http_method_names = ["get"]


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all().order_by("-created_at")
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    http_method_names = ["get"]
    lookup_field = 'slug'
