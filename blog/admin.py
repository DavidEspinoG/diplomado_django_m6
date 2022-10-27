from django.contrib import admin
from . import models

class AdminEntradaBlog(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'fecha_creacion', 'fecha_actualizacion')

admin.site.register(models.EntradaBlog, AdminEntradaBlog)