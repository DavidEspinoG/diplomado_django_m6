from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import models
from django.views import View
from django.shortcuts import render, redirect
import lorem
from django.urls import reverse_lazy
class BlogHome(ListView): 
    model = models.EntradaBlog
    template_name= 'blog/blog_home.html'
    context_object_name = 'blogs'
    paginate_by = 5
class BlogGenerator(CreateView):
    def get(self, request):
        return render(request, template_name=('blog/blog_generator.html'))
    def post(self, request): 
        cantidad = int(request.POST.get('cantidad', 0))
        for _ in range(cantidad):
            models.EntradaBlog.objects.create(
                titulo = lorem.sentence(), 
                contenido = lorem.paragraph()
            ).save()
        return redirect('blog:home')
class BlogDetail(DetailView):
    model = models.EntradaBlog
    template_name = 'blog/detail.html'
class BlogCreate(CreateView):
    template_name = 'blog/crear.html'
    model = models.EntradaBlog
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('blog:home')
class BlogUpdate(UpdateView):
    template_name = 'blog/update.html'
    model = models.EntradaBlog
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('blog:home')