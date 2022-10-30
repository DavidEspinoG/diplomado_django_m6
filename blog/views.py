from datetime import datetime
from django.views.generic import ListView
from . import models
from django.views import View
from django.shortcuts import render, redirect
import lorem
class BlogHome(ListView): 
    model = models.EntradaBlog
    template_name= 'blog/blog_home.html'
    context_object_name = 'blogs'

class BlogGenerator(View):
    def get(self, request):
        return render(request, template_name=('blog/blog_generator.html'))
    def post(self, request): 
        cantidad = int(request.POST.get('cantidad', 0))
        # fecha = datetime.now()
        for _ in range(cantidad):
            blog = models.EntradaBlog()
            blog.titulo = lorem.sentence()
            blog.contenido = lorem.paragraph()
            blog.save()
        return redirect('blog:home')