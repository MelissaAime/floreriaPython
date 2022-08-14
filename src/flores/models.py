from tabnanny import verbose
from django.db import models

# Models
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    precio = models.FloatField()
    cuidados = models.CharField(max_length=300)

    def __str__(self):
        return f"Producto {self.id}: {self.nombre}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
