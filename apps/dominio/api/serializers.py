from rest_framework import serializers

from apps.dominio.models import Tipo


class DominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = (
            'id',
            'descripcion',
            'orden',
        )
