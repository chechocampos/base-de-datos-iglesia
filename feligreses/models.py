from django.db import models
from datetime import date

class Feligres(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estado_civil = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    correo = models.EmailField(blank=True)
    conyuge = models.CharField(max_length=100, blank=True)
    hijos = models.IntegerField(default=0)
    fecha_ingreso = models.DateField(null=True, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    ministerio = models.CharField(max_length=100, blank=True)
    antecedentes = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            return today.year - self.fecha_nacimiento.year - (
                (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
            )
        return None

    def __str__(self):
        return self.nombre
