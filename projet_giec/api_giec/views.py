# Create your views here.
from rest_framework import viewsets

from .models import RapportClimatique
from .serializers import RapportClimatiqueSerializer


class RapportClimatiqueViewSet(viewsets.ModelViewSet):
    queryset = RapportClimatique.objects.all()
    serializer_class = RapportClimatiqueSerializer
