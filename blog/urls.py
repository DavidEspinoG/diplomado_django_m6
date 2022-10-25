from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog.as_view(), name='blog_home' ),
]