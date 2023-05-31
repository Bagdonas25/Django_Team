from django.db import models




# Create your models here.


class Automobilio_modelis(models.Model):
    Marke = models.CharField(max_length=100)
    Modelis = models.CharField(max_length=100)



    def __str__(self):
        return f"{self.Marke} {self.Modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilių modeliai"


class Automobilis(models.Model):

    Valstybinis_NR = models.CharField (max_length=6, help_text="ABC123")
    Automobilio_modelis_id = models.ForeignKey (Automobilio_modelis, on_delete=models.CASCADE
    )
    VIN_kodas = models.CharField (max_length=30)
    klientas = models.CharField (max_length=100)

    def __str__(self):
        return f"{self.Valstybinis_NR}" \
               f" {self.Automobilio_modelis_id}" \
               f" {self.VIN_kodas} " \
               f"{self.klientas}"
    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

