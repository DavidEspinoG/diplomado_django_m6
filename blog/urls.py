from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.BlogHome.as_view(), name='home' ),
    path('generator/', views.BlogGenerator.as_view(), name='generator'),
]