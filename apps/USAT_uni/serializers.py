from rest_framework import serializers
from .models import GalleryModel, NewsModel


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryModel
        fields = ["id", "title_uz", "title_ru", "title_en", "image"]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ["id", "title_uz", "title_ru", "title_en", "image", "description", "description_ru", "description_en",
                  "slug"]
