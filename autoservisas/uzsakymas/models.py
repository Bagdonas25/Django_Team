from django.db import models

from automobilis.models import Automobilis


# Create your models here.

class Uzsakymas(models.Model):

    data = models.CharField(max_length=255)
    automobilis_id = models.ForeignKey(Automobilis, on_delete=models.CASCADE
    )
    suma = models.IntegerField()

    def __str__(self):
        return f"{self.data} {self.automobilis_id} {self.suma}"

    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Užsakymai"

class Paslauga(models.Model):

    pavadinimas = models.CharField(max_length=255)
    kaina = models.IntegerField()

    def __str__(self):
        return f"{self.pavadinimas} {self.kaina}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

class Uzsakymo_eilute(models.Model):

    Paslauga = models.ForeignKey(Paslauga, on_delete=models.CASCADE)
    Uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE)
    Kiekis = models.CharField(max_length=255)
    Kaina = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Paslauga} {self.Uzsakymas} {self.Kiekis} {self.Kaina}"
    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutės"