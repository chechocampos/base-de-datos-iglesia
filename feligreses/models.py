from django.db import models

class Iglesia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Feligres(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    cargo = models.CharField(max_length=50)
    antecedentes = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    iglesia = models.ForeignKey(Iglesia, on_delete=models.CASCADE, null=True, blank=True)  # Permitir valores nulos temporalmente

    def __str__(self):
        return self.nombre
