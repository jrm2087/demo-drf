from rest_framework import viewsets, mixins
from apps.dominio.models import Tipo
from apps.dominio.api.serializers import DominioSerializer
from apps.permissions import CustomPermission


class DominioApiViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Información de Parámetro
    ----------
    dominio : str
        Opciones - TIPO

    """
    permission_classes = [CustomPermission]
    serializer_class = DominioSerializer
    http_method_names = ['get']

    def get_queryset(self):
        query = {}
        if self.request.query_params.get('dominio') == 'TIPO':
            query = Tipo.objects.obtener_dominio()
        # elif self.request.query_params.get('dominio') == 'SESION':
        #     query = Sesion.objects.obtener_dominio()

        return query

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
