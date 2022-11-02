from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Actividad, EtiquetaImportancia, EtiquetaEstado
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
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
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        param_get = '&'.join([f'{p}={k}' for p,k in self.request.GET.items() if p != 'page'])
        context["param_get"] = param_get
        return context
    def get_queryset(self):
        importancia_pk = self.request.GET.get('ipk', None)
        estado_pk = self.request.GET.get('epk', None)
        objetos = Actividad.objects.all()
        if importancia_pk: 
            objetos = objetos.filter(importancia=importancia_pk)
        if estado_pk: 
            objetos = objetos.filter(estado=estado_pk)
        return objetos
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

class ActividadesDetalle(DetailView):
    model = Actividad
    template_name = 'actividades/detalle.html'
class ActividadesCrear(CreateView):
    extra_context = {'importancias':EtiquetaImportancia.objects.all(),
        'estados':EtiquetaEstado.objects.all(),
        'accion': 'crear'}
    template_name = 'actividades/crear.html'
    model = Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    success_url = reverse_lazy('actividades:home')
class ActividadesEditar(UpdateView):
    extra_context = {'importancias':EtiquetaImportancia.objects.all(),
        'estados':EtiquetaEstado.objects.all(),
        'accion': 'editar'}
    template_name = 'actividades/crear.html'
    model = Actividad
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_limite', 'importancia', 'estado']
    def get_success_url(self):
        return reverse('actividades:detalle', args=(self.kwargs['pk'],))
class ActividadesEliminar(DeleteView):
    model = Actividad
    template_name = 'actividades/detalle.html'
    success_url = reverse_lazy('actividades:home')
    extra_context = {'confirmar_eliminar' : True}