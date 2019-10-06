from django.db import models


CAMISA = 'camisa'
CAMISETA = 'camiseta'
PANTALON = 'pantalon'
CALZADO = 'calzado'

TIPO_PRENDA = [
    (CAMISA, 'camisa'),
    (CAMISETA, 'camiseta'),
    (PANTALON, 'pantalon'),
    (CALZADO, 'calzado')
]


class Prenda(models.Model):
    marca = models.CharField(
        max_length=200
    )

    modelo = models.CharField(
        max_length=200
    )

    tipo = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        choices=TIPO_PRENDA,
        default=None
    )

    def __str__(self):
        return f"{self.marca} - {self.modelo}"