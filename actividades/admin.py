from django.contrib import admin
from . import models
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    
admin.site.register(models.Actividad, ActividadAdmin)
admin.site.register(models.EtiquetaImportancia)
admin.site.register(models.EtiquetaEstado)