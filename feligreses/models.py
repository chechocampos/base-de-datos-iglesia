from django.db import models

class Feligres(models.Model):
    # Datos personales
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=50)
    carnet = models.CharField(max_length=50, blank=True, null=True)
    departamento_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=50)
    tipo_sangre = models.CharField(max_length=5)  # RH
    cargo_eclesiastico = models.CharField(max_length=100, blank=True, null=True)

    # Información adicional
    fecha_ingreso = models.DateField()
    primaria = models.CharField(max_length=100, blank=True, null=True)
    secundaria = models.CharField(max_length=100, blank=True, null=True)
    universitaria = models.CharField(max_length=100, blank=True, null=True)
    otros_titulos = models.TextField(blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)

    # Contacto
    domicilio = models.CharField(max_length=255)
    celular = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    nombre_familiar = models.CharField(max_length=100, blank=True, null=True)
    celular_familiar = models.CharField(max_length=50, blank=True, null=True)

    # Bautismo
    bautismo_fecha = models.DateField(blank=True, null=True)
    bautismo_lugar = models.CharField(max_length=100, blank=True, null=True)

    # Matrimonio
    matrimonio_civil_fecha = models.DateField(blank=True, null=True)
    matrimonio_civil_lugar = models.CharField(max_length=100, blank=True, null=True)
    matrimonio_civil_archivo = models.FileField(upload_to="matrimonio_civil/", blank=True, null=True)

    matrimonio_eclesiastico_fecha = models.DateField(blank=True, null=True)
    matrimonio_eclesiastico_lugar = models.CharField(max_length=100, blank=True, null=True)
    matrimonio_eclesiastico_archivo = models.FileField(upload_to="matrimonio_eclesiastico/", blank=True, null=True)

    # Conyugue
    conyugue_nombre = models.CharField(max_length=100, blank=True, null=True)
    conyugue_celular = models.CharField(max_length=50, blank=True, null=True)

    # Hijos
    hijos_menores = models.TextField(blank=True, null=True)

    # Otros
    observaciones = models.TextField(blank=True, null=True)
    antecedentes = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to="fotos/", blank=True, null=True)
    fotocopia_id = models.FileField(upload_to="documentos/id/", blank=True, null=True)
    membresia = models.FileField(upload_to="documentos/membresia/", blank=True, null=True)

    def __str__(self):
        return self.nombres + " " + self.apellidos
