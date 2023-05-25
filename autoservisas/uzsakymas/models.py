from django.db import models

import automobilis


# Create your models here.

class Uzsakymas(models.Model):

    data = models.CharField(max_length=255)
    automobilis_id = models.ForeignKey(

        automobilis, on_delete=models.CASCADE
    )
    suma = models.IntegerField()


class Paslauga (models.Model):
    pavadinimas = models.CharField(max_length=255)
    kaina = models.IntegerField()

class Uzsakymo_eilute (models.Model):

    Paslauga = models.ForeignKey(Paslauga, on_delete=models.CASCADE)
    Uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE)
    Kiekis = models.CharField(max_length=255)
    Kaina = models.CharField(max_length=255)
