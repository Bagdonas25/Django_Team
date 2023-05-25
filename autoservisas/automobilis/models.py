from django.db import models

# Create your models here.
class Automobilio_modelis(models.Model):
    Marke = models.CharField(max_length=100)
    Modelis = models.CharField(max_length=100)


class Automobilis (models.Model):

    Valstybinis_NR = models.CharField (max_length=6, help_text="ABC123")
    Automobilio_modelis_id = models.ForeignKey (Automobilio_modelis,
                                                on_delete=models.CASCADE
    )
    VIN_kodas = models.CharField (max_length=30)
    klientas = models.CharField (max_length=100)

