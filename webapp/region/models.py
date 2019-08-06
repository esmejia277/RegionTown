from django.db import models
from town.models import Town

# Create your models here.

class Region(models.Model):
    code = models.IntegerField(verbose_name="Código", unique=True)
    name_region = models.CharField(max_length=100, verbose_name='Nombre')
    town = models.ManyToManyField(Town, verbose_name="Municipio", blank=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        ordering = ["-name_region"]

    def __str__(self):
        return f'{self.code} - {self.name_region}'