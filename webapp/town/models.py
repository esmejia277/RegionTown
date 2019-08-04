from django.db import models

# Create your models here.

class Town(models.Model):

    INACTIVE = 0
    ACTIVE = 1
    STATUS_CHOICES = (
    (INACTIVE, 'Ináctivo'),
    (ACTIVE, 'Activo'),)

    code = models.IntegerField(verbose_name="Código", unique=True)
    name_town = models.CharField(max_length=100, verbose_name='Nombre')
    status = models.SmallIntegerField(choices = STATUS_CHOICES, default = INACTIVE, verbose_name='Estado')

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipio"
        ordering = ["-name_town"]

    def __str__(self):
        return f'{self.code} - {self.name_town}'