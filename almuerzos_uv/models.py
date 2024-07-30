from django.db import models
from django.utils import timezone

# Create your models here.

class Almuerzo(models.Model):
    fecha = models.DateField(default=timezone.now)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.fecha} - {self.cantidad} almuerzos"
    


class Estudiante(models.Model):
    codigo_estudiante = models.CharField(max_length=20, unique=True)
    nombre_estudiante = models.CharField(max_length=50)
    apellido_estudiante = models.CharField(max_length=50)
    plan_estudiante = models.CharField(max_length=50)
    correo_estudiante = models.EmailField()

    def __str__(self):
        return f"{self.nombre_estudiante} {self.apellido_estudiante}"