from django.db import models
from apps.dominio.managers import DominioManager


class AbstractDominio(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    orden = models.PositiveIntegerField(default=0)
    estado = models.BooleanField('Activo', default=True)

    objects = DominioManager()

    def __str__(self):
        return f'({self.id}) {self.descripcion}'

    class Meta:
        abstract = True


class Tipo(AbstractDominio):
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['orden']
