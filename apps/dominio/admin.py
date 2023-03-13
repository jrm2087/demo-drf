from django.contrib import admin
from apps.dominio.models import Tipo


@admin.register(Tipo)
class ModalidadProgramaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'orden', 'estado']
