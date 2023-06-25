from django.db import models

# Create your models here.

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaSeminario = models.DateField()
    empresaInstitucion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profesion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=200, blank=True)
