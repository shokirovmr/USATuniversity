from rest_framework.routers import DefaultRouter
from apps.USAT_uni.views import (
    GalleryViewSet,
    NewsViewSet,
)

router = DefaultRouter()

router.register(r"galleries", GalleryViewSet, basename="gallery")
router.register(r"news", NewsViewSet, basename="news")

urlpatterns = router.urls
