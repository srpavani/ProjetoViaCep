from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import ViaCepViewSet

router = DefaultRouter()
router.register(prefix="cep", viewset=ViaCepViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
