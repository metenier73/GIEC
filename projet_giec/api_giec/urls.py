from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RapportClimatiqueViewSet

router = DefaultRouter()
router.register(r'rapports', RapportClimatiqueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
