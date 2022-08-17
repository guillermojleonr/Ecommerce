from django.shortcuts import render
from blog.models import post, categoria

# Create your views here.

def blog_view(request):
    posts=post.objects.all()
    return render(request,"blog/blog.html", {"posts":posts})

def post_categorizados(request, categoria_id):
    categorias_seleccionada=categoria.objects.get(id=categoria_id)
    posts=post.objects.filter(categorias=categorias_seleccionada)
    return render(request,"blog/post_categorizados.html", {'categoria':categorias_seleccionada, "posts":posts})