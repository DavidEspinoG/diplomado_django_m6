from django.views.generic import ListView
from .models import Actividad, EtiquetaImportancia, EtiquetaEstado
from django.views import View
from django.shortcuts import render, redirect
import lorem
import datetime
import random
class ActividadesHome(ListView):   
    model = Actividad 
    #Nombre de la plantilla que django busca por defecto : actividad_list
    # Para cambiar el nombre de la plantilla se usa template_name = 

    template_name = 'actividades/home.html'
    #Nombre de los elementos del contexto: actividad_list
    # context_object_name= cambia el nombre de los elementos del contexto

class ActividadesGenerador(View):
    def get(self, request):
        return render(request, template_name='actividades/generador.html')
    
    def post(self, request):
        # Número de actividades indicadas en el formulario
        cantidad = int(request.POST.get('cantidad', 0))
        # Fecha mínima de inicio de las actividades
        fecha_base = datetime.date(year=2022, month=1, day=1)
        # Lista de etiquetas existentes
        et_importancia = EtiquetaImportancia.objects.all()
        et_estado = EtiquetaEstado.objects.all()
        for _ in range(cantidad):
            actividad = Actividad()
            actividad.titulo = lorem.sentence()
            actividad.descripcion = lorem.paragraph()
            actividad.fecha_inicio = fecha_base + datetime.timedelta(days=random.randint(0, 100))
            actividad.fecha_limite = actividad.fecha_inicio + datetime.timedelta(days=random.randint(30, 90))
            actividad.importancia = et_importancia[random.randint(0, len(et_importancia) - 1)]
            actividad.estado = et_estado[random.randint(0, len(et_estado) - 1)]
            actividad.save()
        return redirect('actividades:home')