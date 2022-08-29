from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto_view(request):
    formulario_contacto=formularioContacto()
    if request.method == 'POST':
        formulario_contacto=formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            email = EmailMessage("Mensaje desde App Djando","El usuario con nombre {} con la dirección {} escribe lo siguiente".format(nombre,email,contenido),"",["email@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    return render(request,"contacto/contacto.html",{"miFormulario":formulario_contacto})
    

