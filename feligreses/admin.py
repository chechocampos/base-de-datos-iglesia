from django.contrib import admin
from .models import Feligres

@admin.register(Feligres)
class FeligresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'telefono', 'ciudad', 'cargo', 'fecha_ingreso')
    search_fields = ('nombre', 'cedula', 'telefono', 'ciudad', 'cargo')
