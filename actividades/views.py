from django.views.generic import ListView
from .models import Actividad

class ActividadesHome(ListView):   
    model = Actividad 
    #Nombre de la plantilla que django busca por defecto : actividad_list
    # Para cambiar el nombre de la plantilla se usa template_name = 

    template_name = 'actividades/home.html'
    #Nombre de los elementos del contexto: actividad_list
    # context_object_name= cambia el nombre de los elementos del contexto