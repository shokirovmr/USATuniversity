from django.db import models
from django.utils.text import slugify
from apps.shared.models import AbstractBaseModel
from ckeditor.fields import RichTextField


class GalleryModel(AbstractBaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="gallery/")

    def __str__(self):
        return f"{self.title}: image: {self.image}"


class NewsModel(AbstractBaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="news/")
    # description = models.CharField(max_length=255)
    description = RichTextField()
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
