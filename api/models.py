from django.db import models
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    completada = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return 'El titulo es %s la tarea es %s y es actualizada %s' % (self.titulo, self.nombre, self.actualizado)

    class Meta:
        ordering = ['-creado']
        

