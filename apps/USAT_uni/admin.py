from django.contrib import admin
from .models import GalleryModel, NewsModel
from modeltranslation.admin import TabbedTranslationAdmin

# Import the translation module
from . import translation


@admin.register(GalleryModel)
class GalleryAdmin(TabbedTranslationAdmin):
    list_display = (
        "image",
    )
    search_fields = ("title",)


@admin.register(NewsModel)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
    )
    search_fields = ("title",)
    prepopulated_fields = {'slug': ('title', )}
