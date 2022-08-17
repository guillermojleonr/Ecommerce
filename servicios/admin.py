from django.contrib import admin
from .models import servicio

""" Register your models here. """

#To show the fields 'created' and 'updated' in the admin panel we need to create a new class establishing those fields as readonly

class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicio,servicioAdmin) #register the classes in the admin panel