from django import forms
from .models import Feligres

class FeligresForm(forms.ModelForm):
    class Meta:
        model = Feligres
        fields = [
            'nombre',
            'cedula',
            'fecha_nacimiento',
            'estado_civil',
            'correo',
            'telefono',
            'direccion',
            'ciudad',
            'conyuge',
            'hijos',
            'fecha_ingreso',
            'cargo',
            'ministerio',
            'antecedentes',
            'observaciones',
            'foto',
        ]
