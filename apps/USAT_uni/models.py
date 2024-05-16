from django.db import models
from django.utils.text import slugify
from apps.shared.models import AbstractBaseModel


class GalleryModel(AbstractBaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="gallery/")


class NewsModel(AbstractBaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="news/")
    description = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
