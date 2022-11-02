from django.urls import path, include
from .views import ActividadesHome
from . import views
from django.contrib import admin
app_name= "actividades"
urlpatterns = [
    path('', ActividadesHome.as_view() , name="home"),
    path('admin/', admin.site.urls , name="admin"),
    path('generador/', views.ActividadesGenerador.as_view() , name="generador"),
    path('detalle/<int:pk>/', views.ActividadesDetalle.as_view(), name='detalle' ),
    path('crear/', views.ActividadesCrear.as_view(), name="crear"),
    path('editar/<int:pk>/', views.ActividadesEditar.as_view(), name="editar"),
    path('eliminar/<int:pk>/', views.ActividadesEliminar.as_view(), name="eliminar"),
]