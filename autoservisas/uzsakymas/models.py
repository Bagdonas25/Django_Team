from django.db import models

# Create your models here.

class Paslauga (models.Model):
    pavadinimas = models.CharField(max_length=255)
    kaina = models.IntegerField()

class Uzsakymo_eilute (models.Model):
      Paslauga = models.ForeignKey(Paslauga)
    # Uzsakymas = models.ForeignKey(Uzsakymas)
    Kiekis = models.CharField(max_length=255)
    Kaina = models.CharField(max_length=255)

