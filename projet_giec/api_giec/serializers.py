from rest_framework import serializers
from .models import RapportClimatique

class RapportClimatiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapportClimatique
        fields = '__all__'
