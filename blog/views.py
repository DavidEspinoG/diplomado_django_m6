from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.
class blog(ListView): 
    model = models.EntradaBlog
    template_name= 'blog/blog_home.html'