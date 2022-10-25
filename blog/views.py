from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class blog(TemplateView): 
    template_name= 'blog/blog_home.html'