
from django.http import HttpResponse
from rest_framework import viewsets
from .models import RapportClimatique
from .serializers import RapportClimatiqueSerializer


# Create your views here.
def home(request):
    return HttpResponse("Bienvenue sur l'API GIEC ! Accédez à /api/ pour voir les données.")




class RapportClimatiqueViewSet(viewsets.ModelViewSet):
    queryset = RapportClimatique.objects.all()
    serializer_class = RapportClimatiqueSerializer
