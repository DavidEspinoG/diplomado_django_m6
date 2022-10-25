from django.urls import path, include
from .views import ActividadesHome
from . import views
app_name= "actividades"
urlpatterns = [
    path('', ActividadesHome.as_view() , name="home"),
    path('generador/', views.ActividadesGenerador.as_view() , name="generador"),
]