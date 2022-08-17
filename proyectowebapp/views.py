from django.shortcuts import render, HttpResponse


# Create your views here.
def home_view(request):
    return render(request,"proyectowebapp/home.html")

def tienda_view(request):
    return render(request,"proyectowebapp/tienda.html")