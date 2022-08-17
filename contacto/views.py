from django.shortcuts import render
from .forms import formularioContacto


# Create your views here.

def contacto_view(request):
    formulario_contacto=formularioContacto()
    return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})
    

