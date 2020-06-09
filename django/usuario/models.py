from django.contrib.auth.models import User
from django.db import models


class Usuario(User):

    prendas = models.ManyToManyField(
        'prenda.Prenda',
        blank=True,
        related_name='prendas_usuario'
    )

    nombre = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    apellidos = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
