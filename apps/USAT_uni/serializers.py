from rest_framework import serializers
from .models import GalleryModel, NewsModel


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = ["id", "title", "image"]


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = ["id", "title", "image", "description", "slug"]
