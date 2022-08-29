from django.contrib import admin
from .models import categoriaProd, Producto

""" Register your models here. """

#To show the fields 'created' and 'updated' in the admin panel we need to create a new class establishing those fields as readonly

class categoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class productoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(categoriaProd,categoriaProdAdmin)
admin.site.register(Producto,productoAdmin)