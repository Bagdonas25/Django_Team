from django.db import models
from automobilis_id.models import automobilis

# Create your models here.
class Uzsakymas(models.Model):

    data = models.CharField(max_length=255)
    automobilis_id = models.ForeignKey(
        automobilis,

    )
    suma = models.IntegerField()
