from django.urls import path, include
from .views import ActividadesHome
app_name= "actividades"
urlpatterns = [
    path('', ActividadesHome.as_view() , name="home"),
]