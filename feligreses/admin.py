from django.contrib import admin
from .models import Feligres

@admin.register(Feligres)
class FeligresAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'documento_identidad', 'celular', 'fecha_ingreso')
    search_fields = ('nombres', 'apellidos', 'documento_identidad', 'celular')


