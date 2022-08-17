from django.contrib import admin
from .models import post, categoria

""" Register your models here. """

#To show the fields 'created' and 'updated' in the admin panel we need to create a new class establishing those fields as readonly

class postAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class categoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(post,postAdmin) #register the classes in the admin panel
admin.site.register(categoria,categoriasAdmin)