from django.db import models
from django.utils import timesince
class EtiquetaImportancia(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name="título")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")

    def __str__(self):
        return self.titulo
    class Meta: 
        verbose_name_plural="Etiquetas de importancia"

class EtiquetaEstado(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name="título")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")
    
    def __str__(self):
        return self.titulo
    class Meta: 
        verbose_name_plural="Etiquetas de estado"

class Actividad(models.Model):
    titulo = models.CharField(max_length=256, null=False, verbose_name="título")
    descripcion = models.TextField(verbose_name="descripción")
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField(verbose_name="fecha límite")
    importancia = models.ForeignKey(EtiquetaImportancia, on_delete=models.CASCADE)
    estado = models.ForeignKey(EtiquetaEstado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="fecha actualización")

    def __str__(self):
        return self.titulo
    @property
    def time_since(self):
        return timesince.timesince(self.fecha_creacion)
    class Meta: 
        verbose_name_plural="Actividades"
        ordering = ['fecha_creacion']