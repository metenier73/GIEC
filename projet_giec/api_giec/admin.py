from django.contrib import admin

# Register your models here.

from .models import RapportClimatique

# Enregistrement du modèle de rapport climatique
@admin.register(RapportClimatique)
class RapportClimatiqueAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication')  # Colonnes affichées dans la liste d'objets
    search_fields = ('titre',)  # Ajoute une barre de recherche sur le champ 'titre'
    list_filter = ('date_publication',)  # Filtre par date de publication