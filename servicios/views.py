from django.shortcuts import render
from .models import servicio
# Create your views here.

def servicios_view(request):
    servicios=servicio.objects.all()
    return render(request,"servicios/servicios.html", {"servicios": servicios})