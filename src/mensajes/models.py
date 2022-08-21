from django.db import models

# Models
# Mensajes
class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField(max_length=300)

    def __str__(self):
        return f"Mensaje de: {self.nombre}"
    
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
