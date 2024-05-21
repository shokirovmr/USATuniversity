from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.USAT_uni.views import GalleryViewSet, NewsViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register(r'galleries', GalleryViewSet, basename='gallery')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)