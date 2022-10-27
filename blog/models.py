from django.db import models

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=40, verbose_name="Título")
    contenido = models.TextField(max_length=256, verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    class Meta():
        verbose_name_plural = "Blogs"
        verbose_name = "Blog"
        ordering = ['fecha_creacion']
    def __str__(self): 
        return self.titulo



