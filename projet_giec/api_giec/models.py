from django.db import models

# Create your models here.


class RapportClimatique(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_publication = models.DateField()

    def __str__(self):
        return self.titre
