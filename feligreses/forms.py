from django import forms
from .models import Feligres

class FeligresForm(forms.ModelForm):
    class Meta:
        model = Feligres
        fields = '__all__'
        widgets = {
    'hijos_menores': forms.Textarea(attrs={
        'rows': 3,
        'placeholder': 'Ej: Juan Pérez\nAna Gómez\nCarlos Díaz...'
    }),
    'cargo_eclesiastico': forms.TextInput(attrs={
        'placeholder': 'Ej: Pastor, Líder, Diácono...'
    }),
}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Campos obligatorios mínimos
        self.fields['nombres'].required = True
        self.fields['apellidos'].required = True
        self.fields['documento_identidad'].required = True
        self.fields['estado_civil'].required = True
        self.fields['tipo_sangre'].required = True
        self.fields['departamento_nacimiento'].label = "Ciudad de nacimiento"
        self.fields['departamento_nacimiento'].required = True

