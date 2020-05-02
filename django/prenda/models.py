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

    imagen = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.marca} - {self.modelo}"


class Match(models.Model):
    prenda_1 = models.ForeignKey(
        'prenda.Prenda',
        on_delete=models.CASCADE,
        related_name='prenda_1'
    )

    prenda_2 = models.ForeignKey(
        'prenda.Prenda',
        on_delete=models.CASCADE,
        related_name='prenda_2'
    )

    positivos = models.IntegerField(
        default=0
    )

    negativos = models.IntegerField(
        default=0
    )

    neutrales = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.prenda_1} --- {self.prenda_2}: ({self.total_matches})"

    @property
    def total_matches(self):
        return self.positivos + self.negativos + self.neutrales

    @property
    def porcentaje_like(self):
        return int((self.positivos / self.total_matches) * 100)
