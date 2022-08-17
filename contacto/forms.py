from socket import fromshare
from django import forms

class formularioContacto(forms.Form):
    nombre= forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="email",required=True)
    contenido=forms.CharField(label="contenido")