
from django.urls import path, include
from rest_framework import routers
from .views import ImageDataView
from django.conf import settings
from django.conf.urls.static import static 

router=routers.DefaultRouter()
router.register('image', ImageDataView)
urlpatterns = [
    path("",include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)