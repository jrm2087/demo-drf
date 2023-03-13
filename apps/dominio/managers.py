from django.db import models


class DominioManager(models.Manager):
    def obtener_dominio(self):
        return self.filter(estado=True)
