from modeltranslation.translator import register, TranslationOptions
from apps.USAT_uni.models import NewsModel, GalleryModel


@register(NewsModel)
class NewsModelTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(GalleryModel)
class GalleryModelTranslationOptions(TranslationOptions):
    fields = ("title",)
